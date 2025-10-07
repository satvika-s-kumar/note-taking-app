import sqlite3

# Connect (creates noteapp.db if it doesn’t exist)
conn = sqlite3.connect('noteapp.db')

# Create table
conn.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
''')

print("Database and table created successfully!")

conn.close()
