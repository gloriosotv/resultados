import sqlite3

conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team1 TEXT,
        team2 TEXT,
        prediction TEXT
    )
''')
cursor.execute('''
    INSERT INTO games (team1, team2, prediction)
    VALUES ('Team A', 'Team B', 'Team A wins'),
           ('Team C', 'Team D', 'Draw')
''')
conn.commit()
conn.close()

