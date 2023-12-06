import sqlite3

conn =  sqlite3.connect('BasketballTeam.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS home_game(
               id INTEGER PRIMARY KEY,
               basketball_team_id INTEGER,
               create_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitor_game(
               id INTEGER PRIMARY KEY,
               basketball_team_id INTEGER,
               create_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS RMBC(
               id INTEGER PRIMARY KEY,
               team_id INTEGER,
               team_name TEXT NOT NULL,
               city_id INTEGER,
               create_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS city(
               id INTEGER PRIMARY KEY,
               city_name TEXT NOT NULL,
               create_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS basketball_team(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               coach_id INTEGER,
               coach_role TEXT NOT NULL,
               coach_role_id INTEGER,
               player_id INTEGER,
               city_id INTEGER,
               create_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS coaches(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               role_id INTEGER,
               role TEXT NOT NULL,
               create_at TIMESTAMP
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS coach_roles(
               id INTEGER PRIMARY KEY,
               role TEXT NOT NULL,
               create_at TIMESTAMP
        )
''')

conn.commit()

conn.close()