import psutil, time, threading
from utils import Connection

class Cpu(threading.Thread):
    """
    Clase Cpu hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso del Cpu
    """
    _FIELDS_CPU = "INSERT INTO cpu_stat VALUES "
    _FIELDS_DETAILS = "INSERT INTO cpu_details_stat VALUES "

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        """
        Constructor of Class Cpu
        :param group: 
        :param target: 
        :param name: 
        :param args: Ref of the PC's ID 
        :param kwargs: 
        :param daemon: 
        """
        super().__init__(group = group, target=target, name=name,daemon=daemon)
        self.db = Connection.DataBase()
        self.ref_pc = args


    def save_data(self, times, perc, date):
        """
        Method to save the data in the DB
        :param times: list with the times of the Cpu
        :param perc: percentage of cpu's usage
        :param date: date of the data
        """
        sql = self._FIELDS_CPU
        sql += "({},{},{},{},{},'{}')".format( self.ref_pc, times.user,
                                    times.system, times.idle, perc, date)

        self.db.insert_into(sql)

    def save_detailed_data(self, values):
        """
        method to save the detailed data of the different cores and threads of the CPU
        :param values: string with the values to insert in the DB
        """
        if values is not None:
           sql = self._FIELDS_DETAILS
           sql += values
           self.db.insert_into(sql)



    def run(self):
        """
        Method to run the thread
        """
        self.db.get_connection()

        for i in range(10):
            t = time.strftime("%Y/%m/%d %H:%M:%S")
            self.save_data(psutil.cpu_times(), psutil.cpu_percent(), t)
            self.save_detailed_data(self.prepare_values(psutil.cpu_times(True),
                                                        psutil.cpu_percent(None, True), t))
            time.sleep(1.5)      # TO-DO: sleep for 1 min

        self.db.close_connection()

    def prepare_values(self, data, perc, date):
        """
        Auxiliar method to prepare the different values of the query to add data in the table of different cores
        :param data: list with the times of the different cores
        :param perc: list with the percentages of the different cores
        :param date: date of the data
        """
        if data is None or len(data) == 0 or perc is None or len(perc) == 0:
            return None

        values = []
        for i in range(len(data)):
            values.append("({},{},{},{},{},{},'{}')".format(
                    self.ref_pc, i, data[i].user, data[i].system, data[i].idle,
                    perc[i], date))


        return ", ".join(values)