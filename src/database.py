from singleton import Singleton

import sqlite3


@Singleton
class DatabaseManager:

    conn = None
    cursor = None
    ponged = 0

    def connect(self):

        self.conn = sqlite3.connect("db/producer.db")
        self.cursor = self.conn.cursor()
        print("Connected to database!")

    def ping(self):

        print("pong! " + str(self.ponged))
        self.ponged += 1

    def show_projects(self):
        rows = self.cursor.execute("select * from projects")

        for row in rows:
            print(row[0], row[1], row[2])
