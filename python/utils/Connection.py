import pymysql, traceback
from threading import Lock


class DataBase:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = cls.__DataBase_Instance()
        return cls.__instance


    class __DataBase_Instance:

        _usr = 'monitor'
        _psw = 'TFC_Monitor_2017!'
        _host = 'iesmaestre.sytes.net'
        _db = 'tfc_monitor'


        def __init__(self):
            self.conn = None
            self.__locker = Lock()

        def __get_connection(self):
            self.__locker.acquire()
            self.conn = pymysql.connect(host = self._host, user=self._usr,
                    passwd = self._psw, db = self._db)


        def insert_into(self, query):
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
            self.conn.close()
            self.__locker.release()

