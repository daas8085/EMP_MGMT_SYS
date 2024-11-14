import sqlite3

def create_table():
    # Connect to the SQLite database (creates the database file if it doesn’t exist)
    conn = sqlite3.connect('employee_management.db')
    cursor = conn.cursor()
    
    # Create the employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            position TEXT,
            salary REAL
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database and table created successfully!")

if __name__ == "__main__":
    create_table()
