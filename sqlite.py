import sqlite3

def initialize_database():
    # Establish connection to the SQLite database
    connection = sqlite3.connect("student.db")

    # Create a cursor object to execute SQL commands and interact with the database
    cursor = connection.cursor()

    # Check if the STUDENT table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='STUDENT'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Define the table structure
        table_info = """
        CREATE TABLE STUDENT (
            NAME VARCHAR(25),
            CLASS VARCHAR(25),
            SECTION VARCHAR(25),
            MARKS INT
        );
        """
        # Execute the SQL command to create the table
        cursor.execute(table_info)


        # Insert sample records into the table
        cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Data Science', 'B', 100)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'A', 86)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'DEVOPS', 'A', 50)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Maria', 'Data Science', 'C', 75)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('John', 'DEVOPS', 'B', 65)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Lila', 'Data Science', 'A', 95)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Raj', 'Data Science', 'B', 78)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Priya', 'DEVOPS', 'C', 40)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Michael', 'DEVOPS', 'B', 60)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Aisha', 'Data Science', 'A', 85)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('Neha', 'Data Science', 'B', 80)''')
        cursor.execute('''INSERT INTO STUDENT VALUES ('James', 'DEVOPS', 'A', 55)''')


        # Commit the changes made to the database
        connection.commit()

        print("Database initialized and sample data inserted.")
    else:
        print("Database and table already exist. Skipping initialization.")

    # Close the connection
    connection.close()

def main():
    initialize_database()

if __name__ == "__main__":
    main()
