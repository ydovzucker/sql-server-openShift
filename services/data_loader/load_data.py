from fastapi import FastAPI
import os
import mysql.connector

app = FastAPI()

class Connection:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST", "mysql")  # service name of MySQL pod
        self.user = os.getenv("MYSQL_USER", "myuser")
        self.password = os.getenv("MYSQL_PASSWORD", "mypassword")
        self.database = os.getenv("MYSQL_DATABASE", "mydb")
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

class GetData:
    def __init__(self):
        self.conn = Connection()
        self.table = os.getenv("MYSQL_TABLE", "data")

    def get_all_table(self):
        cursor = self.conn.connect()
        cursor.execute(f"SELECT * FROM {self.table}")
        res = cursor.fetchall()
        self.conn.close()
        return res

data_accessor = GetData()

@app.get("/sql")
def get_all_table():
    try:
        res = data_accessor.get_all_table()
        print("Data fetched:", res)   # <-- Debug print
        return {"result": res}
    except Exception as e:
        print("Error in /sql route:", e)  # <-- See what the error is
        return {"error": str(e)}