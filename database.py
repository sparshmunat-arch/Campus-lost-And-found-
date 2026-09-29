import sqlite3


def create_database():
    connection = sqlite3.connect("lost_found.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lost_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT DEFAULT 'LOST'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS found_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT DEFAULT 'FOUND'
        )
    """)

    connection.commit()
    connection.close()
def update_database():
    connection = sqlite3.connect("lost_found.db")
    cursor = connection.cursor()

    try:
        cursor.execute("ALTER TABLE lost_items ADD COLUMN status TEXT DEFAULT 'LOST'")
    except sqlite3.OperationalError:
        pass

    try:
        cursor.execute("ALTER TABLE found_items ADD COLUMN status TEXT DEFAULT 'FOUND'")
    except sqlite3.OperationalError:
        pass

    connection.commit()
    connection.close()    