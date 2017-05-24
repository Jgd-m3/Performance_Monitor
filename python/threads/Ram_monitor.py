# Clase Ram hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso de la Ram
# de momento almacena en un Log

import psutil, time, threading
from utils import Connection

class Ram(threading.Thread):

    _FIELDS_RAM = "INSERT INTO ram_stat VALUES "

    def __init__(self,  group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group = group, target=target, name=name, daemon=daemon)
        self.db = Connection.DataBase()
        self.ref_pc = args

    def save_data(self, virtual, date):

        if virtual is None or len(virtual) == 0:
            return

        tot = virtual.total
        used = virtual.used
        sql = self._FIELDS_RAM
        sql += "({},{},{},{},{},'{}')".format(self.ref_pc, used, virtual.available, virtual.free,
                                              round(used*100/tot, 3), date)
        self.db.insert_into(sql)

    def run(self):

        self.db.get_connection()

        for i in range(10):
            t = time.strftime("%Y/%m/%d %H:%M:%S")
            self.save_data(psutil.virtual_memory(), t)
            time.sleep(1.5)      # TO-DO: sleep for 1 min

        self.db.close_connection()
