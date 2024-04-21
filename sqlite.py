import sqlite3

# Establish connection to the SQLite database
connection = sqlite3.connect("student.db")

# Create a cursor object to execute SQL commands and interact with the database
cursor = connection.cursor()

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

# Insert some sample records into the table
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)''')

# Display all the records in the table
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit the changes made to the database
connection.commit()

# Close the connection
connection.close()
