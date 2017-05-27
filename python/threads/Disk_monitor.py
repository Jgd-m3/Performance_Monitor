# Clase Disc hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso del Disc
# de momento almacena en un Log

import psutil, time, threading
from utils import Connection

class Disk(threading.Thread):

    _FIELDS_DISK = "INSERT INTO disk_stat VALUES "

    def __init__(self,  group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group = group, target=target, name=name, daemon=daemon)
        self.db = Connection.DataBase()
        self.ref_pc = args


    def save_data(self, values):

        if values is None or len(values) == 0:
            return

        sql = self._FIELDS_DISK
        sql += values

        self.db.insert_into(sql)

    def run(self):

        self.db.get_connection()
        paths = self.get_hds()

        for i in range(10):
            t = time.strftime("%Y/%m/%d %H:%M:%S")

            self.save_data(self.prepare_values(paths, t))

            time.sleep(3)  # TO-DO: sleep for 5 mins

        self.db.close_connection()


    def prepare_values(self, paths, date):
        if paths is None or len(paths) == 0:
            return None

        values = []

        for i in paths:
            usage = psutil.disk_usage(i)
            str = "({},'{}',{},{},{},'{}')".format(self.ref_pc, i, usage.used, usage.free, usage.percent, date)
            values.append(str)

        return ", ".join(values)


    def get_hds(self):

        rtn = []
        for n in psutil.disk_partitions(True):
            if (n.opts).find('fixed') != -1 or (n.opts).find('local') != -1:
                rtn.append(n.mountpoint.replace('\\', '/'))
        return rtn