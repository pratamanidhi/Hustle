import sqlite3
import os
from typing import  Type, List

class ConnectionWarehouse():
    def __init__(self):
        self.db_path = "DbFile/HustleWarehouse.db"

    def Execute(self, query, param=None):
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            print(query)
            if param and isinstance(param, (list, tuple, dict)):
                cur.execute(query, param)
            else:
                cur.execute(query)
            return cur.fetchall()

    def FetechAll(self, query, dtoClass: Type = None) -> List:
        if not isinstance(query, str):
            raise ValueError("SQL query invalid")
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            if dtoClass:
                return [dtoClass(**dict(row)) for row in rows]
            return [dict(row) for row in rows]

