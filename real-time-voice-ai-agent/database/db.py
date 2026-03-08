import sqlite3

conn = sqlite3.connect("appointments.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
id INTEGER PRIMARY KEY,
patient TEXT,
doctor TEXT,
date TEXT,
time TEXT
)
""")

conn.commit()