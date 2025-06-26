import sqlite3
from typing import Type, List

class ConnectionLogs():
    def __init__(self):
        self.db_path = "DbFile/HustleLog.db"

    def Execute(self, query, param=None):
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            if param and isinstance(param, (list, tuple, dict)):
                cur.execute(query, param)
            else:
                cur.execute(query)
            return cur.fetchall()