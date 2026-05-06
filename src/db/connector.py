import sqlite3

class DBConnector:
    def __init__(self, url):
        self.url = url

    def connect(self):
        return sqlite3.connect(self.url)
