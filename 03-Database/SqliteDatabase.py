import sqlite3

connection = sqlite3.connect("lessons.db")

cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, lastname TEXT, number INT, grade INT)")
    connection.commit()
    connection.close()

def addStudent():
    cursor.execute("INSERT INTO students VALUES ('Ahmet','Bey',1234,25)")
    connection.commit()
    connection.close()

# createTable()
addStudent()