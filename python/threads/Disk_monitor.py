# Clase Disc hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso del Disc
# de momento almacena en un Log

import psutil, time, threading
from utils import Connection

class Disk(threading.Thread):
    """
    Clase Disc hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso del Disc
    """
    _FIELDS_DISK = "INSERT INTO disk_stat VALUES "

    def __init__(self,  group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        """
        constructor of the Class Disk
        :param group: 
        :param target: 
        :param name: 
        :param args: id of the pc
        :param kwargs: 
        :param daemon: 
        """
        super().__init__(group = group, target=target, name=name, daemon=daemon)
        self.db = Connection.DataBase()
        self.ref_pc = args


    def save_data(self, values):
        """
        method to save the data of the disc
        :param values: values of the query to insert in the db
        :return: 
        """

        if values is None or len(values) == 0:
            return

        sql = self._FIELDS_DISK
        sql += values

        self.db.insert_into(sql)

    def run(self):
        """
        method to run the thread
        :return: 
        """

        self.db.get_connection()
        paths = self.get_hds()

        for i in range(10):
            t = time.strftime("%Y/%m/%d %H:%M:%S")

            self.save_data(self.prepare_values(paths, t))

            time.sleep(3)  # TO-DO: sleep for 5 mins

        self.db.close_connection()


    def prepare_values(self, paths, date):
        """
        Method to prepare the values of the different disks
        :param paths: list with the path of the disk partitions
        :param date: date of the data
        :return: 
        """
        if paths is None or len(paths) == 0:
            return None

        values = []

        for i in paths:
            usage = psutil.disk_usage(i)
            str = "({},'{}',{},{},{},'{}')".format(self.ref_pc, i, usage.used, usage.free, usage.percent, date)
            values.append(str)

        return ", ".join(values)


    def get_hds(self):
        """
        auxiliar method to get the path of the hard disk partitions
        :return: 
        """
        rtn = []
        for n in psutil.disk_partitions(True):
            if (n.opts).find('fixed') != -1 or (n.opts).find('local') != -1:
                rtn.append(n.mountpoint.replace('\\', '/'))
        return rtn