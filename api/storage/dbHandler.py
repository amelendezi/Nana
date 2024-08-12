
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