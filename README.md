Inventory Management System 🏪🚀

📌 Overview
The Inventory Management System is a Python-based application designed to help businesses efficiently manage their inventory. It provides an intuitive GUI, supports secure authentication, and offers powerful reporting features to streamline inventory tracking.

💡 Whether you're a small business owner or managing a large warehouse, this system helps you keep everything organized and under control.

✨ Features
✔️ User Authentication – Secure login system with password hashing 🔑
✔️ CRUD Operations – Add, update, delete, and view inventory items 📦
✔️ Inventory Tracking – Keep track of stock levels in real-time 📊
✔️ Reporting – Generate sales reports and low-stock alerts 📉
✔️ Graphical User Interface (GUI) – Simple and interactive interface using Tkinter 🖥️

🛠 Technologies Used
🚀 Python – Core programming language
🛢️ SQLite – Lightweight database for storing inventory data
🎨 Tkinter – GUI framework for user-friendly interactions
🔐 bcrypt – Secure password hashing for authentication
📊 Pandas – Data manipulation and report generation

⚡ Installation Guide
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/Ridhima1605/inventory-management.git
cd inventory-management
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv env
# Activate Virtual Environment
source env/bin/activate  # For Mac/Linux
env\Scripts\activate  # For Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🚀 Usage Guide
1️⃣ Run the Application
bash
Copy code
python main.py
2️⃣ Add Products
📌 Open the GUI and click on "Add Product"
📌 Enter product details such as name, quantity, and price

3️⃣ View Inventory
📌 Click on "Show Products" to view the current stock

4️⃣ Generate Reports
bash
Copy code
python reports.py
📌 This will create an inventory_report.csv file with sales and stock data

📂 Project Structure
bash
Copy code
inventory-management/
│── main.py            # Entry point
│── database.py        # Database setup
│── auth.py            # User authentication
│── inventory.py       # Inventory CRUD operations
│── gui.py             # GUI (Tkinter)
│── reports.py         # Report generation
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
│── .gitignore         # Ignored files
🚀 Future Improvements
🔹 Web-based UI – Upgrade from Tkinter to Flask/Django 🌍
🔹 Role-Based Access Control – Different permissions for admin & staff 🔑
🔹 Barcode Scanning – Faster product management 📷

📜 License
This project is open-source and available under the MIT License. Feel free to contribute and enhance it! 😊
