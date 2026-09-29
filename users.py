import sqlite3


def create_users_table():
    connection = sqlite3.connect("lost_found.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def register_user():
    name = input("Enter your name: ")
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    while email == "":
        print("Email cannot be empty.")
        email = input("Enter your email: ").strip()
    while "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        email = input("Enter your email: ").strip()    

    connection = sqlite3.connect("lost_found.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )

        connection.commit()
        print("\nUser registered successfully!")

    except sqlite3.IntegrityError:
        print("\nThis email is already registered.")

    connection.close()