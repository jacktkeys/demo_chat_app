import psycopg2
from psycopg2 import errors
from src import config

_postgres_config = config.POSTGRES

class Database:
    def __init__(self):
        self.host = _postgres_config["host"]
        self.username = _postgres_config["user"]
        self.password = _postgres_config["pw"]
        self.port = _postgres_config["port"]
        self.dbname = _postgres_config["db"]
        self.conn = None
    
    def connect(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as e:
                raise e
            finally:
                print('Connection opened successfully.')

    def all(self, command_text):
        data = None
        self.connect()
        with self.conn.cursor() as curr:
            curr.execute(command_text)
            data = curr.fetchall()
        
        self.conn.close()
        self.conn = None
        return data

    def many(self, command_text, limit=1):
        data = None
        self.connect()
        with self.conn.cursor() as curr:
            curr.execute(command_text)
            data = curr.fetchmany(limit)
        
        self.conn.close()
        self.conn = None
        return data

    def one(self, command_text):
        data = None
        self.connect()
        with self.conn.cursor() as curr:
            curr.execute(command_text)
            data = curr.fetchone()
        
        self.conn.close()
        self.conn = None
        return data

    def update(self, command_text):
        data = None
        self.connect()
        with self.conn.cursor() as curr:
            try:
                curr.execute(command_text)
                data = curr.fetchone()
            except errors.UniqueViolation as e:
                data = False
            
        self.conn.commit()
        self.conn.close()
        self.conn = None
        return data
