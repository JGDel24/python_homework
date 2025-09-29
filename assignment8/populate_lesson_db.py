import sqlite3

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL
);
""")

# Create line_items table
cursor.execute("""
CREATE TABLE IF NOT EXISTS line_items (
    line_item_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

# Insert some sample products
cursor.executemany("""
INSERT INTO products (product_id, product_name, price) VALUES (?, ?, ?)
""", [
    (1, 'Notebook', 2.5),
    (2, 'Pen', 1.0),
    (3, 'Backpack', 25.0)
])

# Insert some sample line items
cursor.executemany("""
INSERT INTO line_items (line_item_id, product_id, quantity) VALUES (?, ?, ?)
""", [
    (1, 1, 3),
    (2, 2, 5),
    (3, 3, 1),
    (4, 1, 2)
])

conn.commit()
conn.close()
print("lesson.db created and populated!")
