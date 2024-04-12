import base64
from util.singleton_meta import SingletonMeta
import psycopg2
import os

class PGSingleton(metaclass=SingletonMeta):
    """
    Singleton controlling the PostgreSQL connection
    """

    pg_conn: psycopg2.connection
    pg_cursor: psycopg2.cursor
    
    def __init__(self) -> None:
        cx_string = self.get_cx_string()
        self.pg_conn = psycopg2.connect(cx_string)
        self.pg_cursor = self.pg_conn.cursor()

    def __del__(self):
        self.pg_cursor.close()
        self.pg_conn.close()

    def get_cx_string(self) -> str:
        pg_user = os.environ.get("pg_user")
        pg_db = os.environ.get("pg_db")
        raw_pw = os.environ.get("pg_pw")
        
        pg_pw = " "
        if raw_pw != None:
            pg_pw = base64.b64decode(raw_pw)
        else:
            raise ReferenceError("PG-PW not found in environment config")
        
        return "dbname=%s user=%s password=%s" % (pg_db, pg_user, pg_pw)

    def execute(self, query: str):
        self.pg_cursor.execute(query)
        self.pg_conn.commit()
