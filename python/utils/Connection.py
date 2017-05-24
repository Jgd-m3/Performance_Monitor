import pymysql, traceback

class DataBase:
   
    _usr = 'monitor'
    _psw = 'TFC_Monitor_2017!'
    _host = 'iesmaestre.sytes.net'
    _db = 'tfc_monitor'

    def __init__(self):
        self.conn = None

    def get_connection(self):
        if self.conn is None:
            self.conn = pymysql.connect(host = DataBase._host, user=DataBase._usr,
                    passwd =DataBase._psw, db = DataBase._db)

    
    def insert_into(self, query):
        num = 0
        if query is None or len(query) == 0:
            return 
        try:
            with self.conn.cursor() as cursor:
                num = cursor.execute(query)
                self.conn.commit()
        except:
            traceback.print_exc()
        finally:
            return num

    def get_unique_id(self, query):
        if query is None or len(query) == 0:
            return False

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                rtn = cursor.fetchone()[0]
        except:
            rtn = None
        finally:
            pass

        return rtn

    def get_data(self, query):
        if query is None or len(query) == 0:
            return False

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                rtn = cursor.fetchall()
        finally:
            pass

        return rtn

    def close_connection(self):
        self.conn.close()