import json
import psycopg2

# Function to execute the query and return the result
def executeQuery(format_function, queryStatement):
    try:
        
        with open('api/db_config.json', 'r') as config_file:
            db_config = json.load(config_file)        
        
        connection = psycopg2.connect(**db_config)        
        
        cursor = connection.cursor()
        
        # Execute the SQL query
        cursor.execute(queryStatement)
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
                        
        result = format_function(rows)
        
        return result
    
    except Exception as error:
        print(f"Error fetching data from PostgreSQL table: {error}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
# Function to execute an insert statement
def executeInsert(insertStatement):
    try:
        with open('api/db_config.json', 'r') as config_file:
            db_config = json.load(config_file)
        
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        
        # Execute the insert statement
        cursor.execute(insertStatement)
        connection.commit()
        
        return {"Message": "Insert successful"}
    
    except Exception as error:
        print(f"Error inserting data into PostgreSQL table: {error}")
        return {"Message": "Insert failed"}
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
# Function to execute a truncate statement
def executeTruncate(truncateStatement):
    try:
        with open('api/db_config.json', 'r') as config_file:
            db_config = json.load(config_file)
        
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        
        # Execute the truncate statement
        cursor.execute(truncateStatement)
        connection.commit()
        
        return {"Message": "Truncate successful"}
    
    except Exception as error:
        print(f"Error truncating PostgreSQL table: {error}")
        return {"Message": "Truncate failed"}
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()