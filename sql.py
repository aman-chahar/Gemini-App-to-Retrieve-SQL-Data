import sqlite3

# connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# create the table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

cursor.execute(table_info)

# Insert some records
cursor.execute('''INSERT INTO STUDENT VALUES('Aman', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Himanshu', 'Machine Learning', 'A', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sudhanshu', 'DEVOPS', 'A', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Pipe', 'Life Science', 'C', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Didi', 'Biotech', 'B', 35)''')

# Display all the records
print("The inserted records are: ")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
