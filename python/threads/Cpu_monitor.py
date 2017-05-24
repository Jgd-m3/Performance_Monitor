# Clase Cpu hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso del Cpu
# de momento almacena en un Log
import psutil, time, threading
from utils import Connection

class Cpu(threading.Thread):

    _FIELDS_CPU = "INSERT INTO cpu_stat VALUES "
    _FIELDS_DETAILS = "INSERT INTO cpu_details_stat VALUES "

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group = group, target=target, name=name,daemon=daemon)
        self.db = Connection.DataBase()
        self.ref_pc = args


    def save_data(self, times, perc, date):

        sql = self._FIELDS_CPU
        sql += "({},{},{},{},{},'{}')".format( self.ref_pc, times.user,
                                    times.system, times.idle, perc, date)

        self.db.insert_into(sql)

    def save_detailed_data(self, values):

       if values is not None:
           sql = self._FIELDS_DETAILS
           sql += values
           self.db.insert_into(sql)



    def run(self):

        self.db.get_connection()

        for i in range(10):
            t = time.strftime("%Y/%m/%d %H:%M:%S")
            self.save_data(psutil.cpu_times(), psutil.cpu_percent(), t)
            self.save_detailed_data(self.prepare_values(psutil.cpu_times(True),
                                                        psutil.cpu_percent(None, True), t))
            time.sleep(1.5)      # TO-DO: sleep for 1 min

        self.db.close_connection()

    def prepare_values(self, data, perc, date):

        if data is None or len(data) == 0 or perc is None or len(perc) == 0:
            return None

        values = []
        for i in range(len(data)):
            values.append("({},{},{},{},{},{},'{}')".format(
                    self.ref_pc, i, data[i].user, data[i].system, data[i].idle,
                    perc[i], date))


        return ", ".join(values)