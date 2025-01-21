import sqlite3


# Initialize the database and create the necessary tables
def init_db():
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    # Create search_results table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            rank INTEGER,
            link TEXT,
            title TEXT,
            snippet TEXT,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            relevance INTEGER,
            UNIQUE (query, link)
        )
    """)

    # Create search_history table for tracking user searches
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# Function to insert search history for tracking
def insert_search_history(query):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO search_history (query) VALUES (?)", (query,))
    conn.commit()
    conn.close()


init_db()  # Initialize the database and create the tables
