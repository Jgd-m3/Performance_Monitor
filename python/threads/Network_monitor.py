#!/usr/bin/env python3

import psutil, time, threading
from utils import Connection

class Net(threading.Thread):
    """
    Clase Net hereda de la clase Thread para realizar la recopilacion y almacenamiento de datos del uso de red
    """
    _FIELDS_NET = "INSERT INTO net_stat VALUES "
    _FIELDS_DETAILS = "INSERT INTO net_details_stat VALUES "

    def __init__(self,  group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        """
        constructor of the class Net
        :param group: 
        :param target: 
        :param name: 
        :param args: ref of the pc
        :param kwargs: 
        :param daemon: 
        """
        super().__init__(group = group, target = target, name = name, daemon = daemon)
        self.db = Connection.DataBase()
        self.ref_pc = args

    def save_data(self, counter, date):
        """
        method to save the data in the DB
        :param counter: list with the counters of the network
        :param date: date of the data
        :return: 
        """
        b_sent = counter.bytes_sent
        b_recv = counter.bytes_recv
        tot = b_recv+b_sent
        bal = 0 if tot == 0 else round(b_recv*100 / tot, 3)

        sql = self._FIELDS_NET
        sql += "({},{},{},{},{},{},'{}')".format(self.ref_pc,b_sent, b_recv, counter.packets_sent,
                                                counter.packets_recv, bal, date)

        self.db.insert_into(sql)


    def save_nets_data(self, values):
        """
        method to save the different networks' data
        :param values: String with te values of the query to insert in the table of detailed network
        :return: 
        """
        if values is not None:
            sql = self._FIELDS_DETAILS
            sql += values
            try:
                self.db.insert_into(sql)
            except Exception:
                print(Exception)
    def run(self):
        """
        Method to run the thread
        :return: 
        """
        for i in range(10):
            t = time.strftime("%Y/%m/%d %H:%M:%S")
            self.save_data(psutil.net_io_counters(), t)
            self.save_nets_data(self.prepare_values(psutil.net_io_counters(True), t))
            time.sleep(1.5)         # TO-DO: change to 5mins


    def prepare_values(self, data, date):
        """
        method to prepare the values of the query to insert in DB
        :param data: list with the counters of each network
        :param date: date of the list
        :return: 
        """
        if data is None or len(data) == 0:
            return None

        values = []
        for i in data:
            values.append("({},'{}',{},{},{},{},'{}')".format(
                self.ref_pc, i, data[i].bytes_sent, data[i].bytes_recv,
                data[i].packets_sent, data[i].packets_recv, date))

        return ", ".join(values)