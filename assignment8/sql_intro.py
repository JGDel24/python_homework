import sqlite3
import os

def create_connection():
    conn = None
    try:
        os.makedirs("../db", exist_ok=True)
        conn = sqlite3.connect("../db/magazines.db")
        conn.execute("PRAGMA foreign_keys = 1")  
        print('connection established')

        cursor = conn.cursor()

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        """)

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(id)
            );
        """)

       
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                UNIQUE(name, address)
            );
        """)

      
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                UNIQUE(subscriber_id, magazine_id),
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id)
            );
        """)

        conn.commit()
        print("tables created successfully")

        return conn  

    except sqlite3.Error as e:
        print(f'sqlite3 error {e}')
    return conn




def add_publisher(conn, name):
    try:
        conn.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.Error as e:
        print(f"Error inserting publisher {name}: {e}")

def add_magazine(conn, name, publisher_id):
    try:
        conn.execute(
            "INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id),
        )
    except sqlite3.Error as e:
        print(f"Error inserting magazine {name}: {e}")

def add_subscriber(conn, name, address):
    try:
        conn.execute(
            "INSERT OR IGNORE INTO subscribers (name, address) VALUES (?, ?)",
            (name, address),
        )
    except sqlite3.Error as e:
        print(f"Error inserting subscriber {name}: {e}")

def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        conn.execute(
            """INSERT OR IGNORE INTO subscriptions 
               (subscriber_id, magazine_id, expiration_date) 
               VALUES (?, ?, ?)""",
            (subscriber_id, magazine_id, expiration_date),
        )
    except sqlite3.Error as e:
        print(f"Error inserting subscription: {e}")

def get_all_subscribers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers;")
    rows = cursor.fetchall()
    print("\nAll Subscribers:")
    for row in rows:
        print(row)

def get_all_magazines_sorted(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines ORDER BY name;")
    rows = cursor.fetchall()
    print("\nAll Magazines (sorted by name):")
    for row in rows:
        print(row)

def get_magazines_by_publisher(conn, publisher_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.id, m.name 
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.id
        WHERE p.name = ?;
    """, (publisher_name,))
    rows = cursor.fetchall()
    print(f"\nMagazines published by {publisher_name}:")
    for row in rows:
        print(row)




if __name__ == '__main__':
    conn = create_connection()
    if conn:
       
        add_publisher(conn, "Time Inc")
        add_publisher(conn, "Condé Nast")
        add_publisher(conn, "Hearst Communications")

        
        add_magazine(conn, "Time Magazine", 1)
        add_magazine(conn, "Vogue", 2)
        add_magazine(conn, "Cosmopolitan", 3)

       
        add_subscriber(conn, "Alice Johnson", "123 Main St")
        add_subscriber(conn, "Bob Smith", "456 Oak Ave")
        add_subscriber(conn, "Charlie Davis", "789 Pine Rd")

        
        add_subscription(conn, 1, 1, "2025-12-31")
        add_subscription(conn, 2, 2, "2025-11-30")
        add_subscription(conn, 3, 3, "2025-10-15")

        get_all_subscribers(conn)
        get_all_magazines_sorted(conn)
        get_magazines_by_publisher(conn, "Condé Nast")

        conn.commit()
        print("sample data inserted successfully")

        conn.close()
        print("connection closed")
