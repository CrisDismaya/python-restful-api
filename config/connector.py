# db_connector/connector.py
import os
import psycopg2
from configparser import ConfigParser

class PostgreSQLConnector:
    def __init__(self, config_file="config.ini"):
        self.connection = None
        self.cursor = None
        self.config_file = config_file

    def read_config(self):
        config = ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), self.config_file))
        
        if 'database' not in config:
            print(f"Error: 'database' section not found in config file:")
        return config['database']

    def connect(self):
        try:
            db_config = self.read_config()
            self.connection = psycopg2.connect(
                host=db_config['host'],
                port=db_config.getint('port'),
                database=db_config['name'],
                user=db_config['user'],
                password=db_config['password']
            )
            self.cursor = self.connection.cursor()
            print("Connected to PostgreSQL database")
        except Exception as e:
            print(f"Error: Unable to connect to the database - {e}")

    def execute_query(self, query, params=None):
        try:
            if params is not None:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Exception as e:
            print(f"Error: Unable to execute the query - {e}")

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from PostgreSQL database")
