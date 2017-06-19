#!/usr/bin/env python3

import psutil, time, threading
from utils import Connection


class Process(threading.Thread):
    """
    Class Process to save the data of the process in the DB
    """

    _FIELDS_PROCS = "INSERT INTO process VALUES "

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        """
        Constructor of Class Process
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

    def save_data(self, values):
        """
        method to save the different process of the computer
        :param values: string with the values to insert in the DB
        """
        if values is not None:
           sql = self._FIELDS_PROCS
           sql += values
           self.db.insert_into(sql)


    def run(self):
        """
        Method to run the thread
        """

        for i in range(2):
            t = time.strftime("%Y/%m/%d %H:%M:%S")
            self.save_data(self.prepare_values(psutil.process_iter(), t))

            time.sleep(10)      # TO-DO: sleep for 30 min


    def prepare_values(self, data, date):
        """
        Auxiliar method to prepare the different values of the query to add data in the table of different process
        :param data: list with the process of the system (pid, name)
        :param date: date of the data
        """
        if data is None:
            return None

        values = []
        for i in data:
            values.append("({},{},'{}','{}')".format(self.ref_pc, i.pid, i.name(), date))

        return ", ".join(values)