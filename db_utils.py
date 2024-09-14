import sqlite3

def create_tables(db_url):
    conn = sqlite3.connect(db_url.split('///')[-1])
    cursor = conn.cursor()
    
    # Check existing tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(f"Existing tables: {cursor.fetchall()}")  # Debug print
    
    with open('database/create_tables.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

