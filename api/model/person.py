import psycopg2

def getAll_person():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname="nana",
            user="nana_user",
            password="000000",
            host="localhost",
            port="5432"
        )
        
        cursor = connection.cursor()
        
        # Execute the SQL query
        cursor.execute("SELECT Id, Name, Lastname, DateOfBirth FROM person")
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
        # Format the results into a list of dictionaries
        persons = [
            {
                "Id": row[0],
                "Name": row[1],
                "Lastname": row[2],
                "DateOfBirth": row[3]
            }
            for row in rows
        ]
        
        return persons
    
    except Exception as error:
        print(f"Error fetching data from PostgreSQL table: {error}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()