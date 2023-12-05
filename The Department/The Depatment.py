import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('TheDepartment.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Perform database operations...


#Employee Table Creation
cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               department_id INTEGER,
               project_id INTEGER,
               created_at TIMESTAMP
    )     
''')

#Department Table Creation
cursor.execute('''
        CREATE TABLE IF NOT EXISTS department (
               id INTEGER PRIMARY KEY,
               department_name TEXT NOT NULL,
               division_id INTEGER,
               manager_name TEXT NOT NULL,
               manager_id INTEGER,
               created_at TIMESTAMP
        )
               ''')

#Division Table Creation
cursor.execute('''
        CREATE TABLE IF NOT EXISTS division (
               id INTEGER PRIMARY KEY,
               division_name TEXT NOT NULL,
               manager_name TEXT NOT NULL,
               manager_id INTEGER,
               created_at TIMESTAMP
        )
               ''')

#Projects Table Creation
cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
               id INTEGER PRIMARY KEY,
               project_name TEXT NOT NULL,
               created_at TIMESTAMP
        )
               ''')

#Rovers Table Creation
cursor.execute('''
        CREATE TABLE IF NOT EXISTS rovers (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               project_id INTEGER,
               created_at TIMESTAMP
        )
               ''')

conn.commit()


# Close the connection when done
conn.close()