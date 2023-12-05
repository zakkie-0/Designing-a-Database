import sqlite3

conn = sqlite3.connect('WeGotItAll.db')

cursor = conn.cursor()

#table creation for invoice
cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoice (
            id INTEGER PRIMARY KEY,
            sales_rep_id INTEGER,
            customer_id TEXT NOT NULL,
            product_id INTEGER,
            created_at TIMESTAMP
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_rep (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               created_at TIMESTAMP
        )
''')


cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               created_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
               id INTEGER PRIMARY KEY,
               product_name TEXT NOT NULL,
               product_vendor_id INTEGER,
               created_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendor (
               id INTEGER PRIMARY KEY,
               vendor_name TEXT NOT NULL,
               created_at TIMESTAMP
        )
''')

conn.commit()

conn.close()