import json
import psycopg2

class SQLHandler:
        
    def __init__(self, config_path='api/db_config.json') -> None:
        with open(config_path, 'r') as config_file:
            self.db_config = json.load(config_file)
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(**self.db_config)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, format_function, query_statement):
        try:
            self.connect()
            # Execute the SQL query
            self.cursor.execute(query_statement)
            # Fetch all rows from the executed query
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
            # Execute the insert statement
            self.cursor.execute(insert_statement)
            self.connection.commit()
            return {"Message": "Insert successful"}
        except Exception as error:
            print(f"Error inserting data into PostgreSQL table: {error}")
            return {"Message": "Insert failed"}
        finally:
            self.close()
            
    # Function to execute a truncate statement
    def execute_truncate(self, truncateStatement):
        try:            
            self.connect()                        
            # Execute the truncate statement
            self.cursor.execute(truncateStatement)
            self.connection.commit()            
            return {"Message": "Truncate successful"}        
        except Exception as error:
            print(f"Error truncating PostgreSQL table: {error}")
            return {"Message": "Truncate failed"}        
        finally:
            self.close()