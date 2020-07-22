from mysql.connector import (connection)


class DB_Conn:

    def __init__(self):
        self.user = 'root'
        self.password = 'Juan1125?'
        self.host = 'localhost'
        self.database = 'myweight'

    def connect2shoppingdb(self):
        cnx = connection.MySQLConnection(user=self.user, password=self.password, host=self.host, database=self.database)
        return cnx

    def close_connecttion2shoppingdb(self, cnx):
        cnx.close()

