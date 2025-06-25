import sqlite3
import os
from typing import Type, List

class Connection:
    def __init__(self):
        self.db_path = "DbFile/Hustle.db"

    def Execute(self, query, param=None):
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            if param:
                cur.execute(query, param)
            else:
                cur.execute(query)
            con.commit()
            return cur.fetchall()

    def FetchAll(self, query, dtoClass: Type = None) -> List:
        if not isinstance(query, str):
            raise ValueError("The SQL query must be a string.")
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            if dtoClass:
                return [dtoClass(**dict(row)) for row in rows]
            return [dict(row) for row in rows]

    def CloseConnection(self):
        with sqlite3.connect(self.db_path) as con:
            con.close()
