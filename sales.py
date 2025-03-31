import sqlite3

# Record a sale
def record_sale(product_id, quantity_sold):
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()

    # Get product details
    cursor.execute("SELECT quantity, price FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    
    if not product:
        print("Product not found!")
        return
    
    current_quantity, price = product
    if quantity_sold > current_quantity:
        print("Not enough stock available!")
        return
    
    total_price = quantity_sold * price

    # Update stock
    new_quantity = current_quantity - quantity_sold
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))

    # Log sale
    cursor.execute("INSERT INTO sales (product_id, quantity_sold, total_price) VALUES (?, ?, ?)", 
                   (product_id, quantity_sold, total_price))
    
    conn.commit()
    conn.close()
    print("Sale recorded successfully!")
