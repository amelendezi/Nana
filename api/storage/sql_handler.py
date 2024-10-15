import json
import psycopg2

class SQLHandler:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        with open('api/db_config.json', 'r') as config_file:
            config = json.load(config_file)
        self.connection = psycopg2.connect(**config)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, format_function, query_statement):
        try:
            self.connect()
            self.cursor.execute(query_statement)
            rows = self.cursor.fetchall()
            result = format_function(rows)
            return result
        except Exception as error:
            print(f"Error fetching data from PostgreSQL table: {error}")
            return []
        finally:
            self.close()

    def execute_insert(self, insert_statement):
        try:
            self.connect()
            self.cursor.execute(insert_statement)
            self.connection.commit()
            return {"Message": "Insert successful"}
        except Exception as error:
            print(f"Error inserting data into PostgreSQL table: {error}")
            return {"Message": "Insert failed"}
        finally:
            self.close()

    def execute_truncate(self, truncate_statement):
        try:
            self.connect()
            self.cursor.execute(truncate_statement)
            self.connection.commit()
            return {"Message": "Truncate successful"}
        except Exception as error:
            print(f"Error truncating PostgreSQL table: {error}")
            return {"Message": "Truncate failed"}
        finally:
            self.close()