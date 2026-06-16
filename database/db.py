import sqlite3

conn = sqlite3.connect("database/content.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS content(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fact TEXT,
    source TEXT,
    virality_score INTEGER,
    accuracy_score INTEGER,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created")