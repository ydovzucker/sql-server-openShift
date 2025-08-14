from fastapi import FastAPI, HTTPException
import os
import mysql.connector
app = FastAPI()


class Connection:
    def _init_(self):
        self.host = os.getenv("MYSQL_ROOT_PASSWORD")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DATABASE")
        self.conn = None
        self.cursor = None
    def connect(self):
        self.conn = mysql.connector.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            database= self.database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor
    def close(self):
        self.cursor.close()
        self.conn.close()

    class GetData:
        def _init_(self):
            self.conn = Connection()
            self.table = os.getenv("MYSQL_TABLE")

        def get_all_table(self):
            conn = self.conn.connect()
            res = conn.execute(f"SELECT * FROM {self.table}")
            return res




