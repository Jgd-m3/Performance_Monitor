import pymysql, traceback
from threading import Lock


class DataBase:
    """
    class DataBase to wrap a singleton of __DataBase_Instance
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        Overriding the __new__ constructor
        :param args: 
        :param kwargs: 
        :return: 
        """
        if cls.__instance is None:
            cls.__instance = cls.__DataBase_Instance()
        return cls.__instance


    class __DataBase_Instance:
        """
        Inner class __DataBase_Instance that allows to connect to the DB
        """

        _usr = 'monitor'
        _psw = 'TFC_Monitor_2017!'
        _host = 'iesmaestre.sytes.net'
        _db = 'tfc_monitor'


        def __init__(self):
            """
            Constructor of the __DataBase_Instance Object
            """
            self.conn = None
            self.__locker = Lock()

        def __get_connection(self):
            """
            Method to get the connection
            :return: 
            """
            self.__locker.acquire()
            self.conn = pymysql.connect(host = self._host, user=self._usr,
                    passwd = self._psw, db = self._db)


        def insert_into(self, query):
            """
            Method to insert the query into the DB
            :param query: string that contains the query to insert
            :return: num of rows inserted
            """
            self.__get_connection()
            num = 0
            if query is None or len(query) == 0:
                return
            try:
                # print(query)
                with self.conn.cursor() as cursor:
                    num = cursor.execute(query)
                    self.conn.commit()
            except:

                traceback.print_exc()
            finally:
                self.__close_connection()
            return num

        def get_unique_id(self, query):
            """
            Method to get One unique field when you are selecting just One specific field of the table
            :param query: query of select
            :return: field value
            """
            self.__get_connection()
            if query is None or len(query) == 0:
                return False

            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(query)
                    rtn = cursor.fetchone()[0]
            except Exception:
                rtn = None
            finally:
                self.__close_connection()

            return rtn

        def get_data(self, query):
            """
            method to get a cursor of data from the DB
            :param query: query to do the select
            :return: cursor with the select result
            """
            self.__get_connection()
            if query is None or len(query) == 0:
                return False

            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(query)
                    rtn = cursor.fetchall()
            finally:
                self.__close_connection()

            return rtn

        def __close_connection(self):
            """
            method to close the connection with the DB
            :return: 
            """
            self.conn.close()
            self.__locker.release()

