import tkinter as tk
from tkinter import messagebox
import inventory

def add_product_ui():
    def submit():
        name = name_entry.get()
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())
        inventory.add_product(name, quantity, price)
        messagebox.showinfo("Success", "Product added successfully!")

    window = tk.Tk()
    window.title("Add Product")

    tk.Label(window, text="Product Name:").grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    tk.Label(window, text="Quantity:").grid(row=1, column=0)
    quantity_entry = tk.Entry(window)
    quantity_entry.grid(row=1, column=1)

    tk.Label(window, text="Price:").grid(row=2, column=0)
    price_entry = tk.Entry(window)
    price_entry.grid(row=2, column=1)

    tk.Button(window, text="Add Product", command=submit).grid(row=3, columnspan=2)
    window.mainloop()

if __name__ == "__main__":
    add_product_ui()
