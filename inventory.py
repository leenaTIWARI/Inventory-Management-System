import sqlite3

# Add a new product
def add_product(name, quantity, price):
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", 
                   (name, quantity, price))
    conn.commit()
    conn.close()
    print(f"Product '{name}' added successfully!")

# Update product quantity
def update_product(product_id, quantity):
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, product_id))
    conn.commit()
    conn.close()
    print("Product updated successfully!")

# Delete a product
def delete_product(product_id):
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("Product deleted successfully!")
