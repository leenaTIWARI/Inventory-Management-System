import sqlite3

# Generate low-stock alerts
def check_low_stock(threshold=5):
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity FROM products WHERE quantity < ?", (threshold,))
    low_stock_items = cursor.fetchall()
    conn.close()
    
    if not low_stock_items:
        print("No low-stock items.")
    else:
        print("Low Stock Alert:")
        for item in low_stock_items:
            print(f"{item[0]} - Only {item[1]} left!")

# Generate sales report
def generate_sales_report():
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, SUM(quantity_sold), SUM(total_price) FROM sales GROUP BY product_id")
    report = cursor.fetchall()
    conn.close()
    
    print("Sales Report:")
    for item in report:
        print(f"Product ID: {item[0]} | Sold: {item[1]} | Revenue: ${item[2]:.2f}")
