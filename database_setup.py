import sqlite3

def setup_database():
    conn = sqlite3.connect('inventory.db') 
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT,
                    role TEXT)''')

    # Create Products Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    quantity INTEGER,
                    price REAL)''')

    # Create Sales Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY,
                    product_id INTEGER,
                    quantity_sold INTEGER,
                    total_price REAL,
                    FOREIGN KEY (product_id) REFERENCES products(id))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete!")
