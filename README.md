# Inventory-Management-System🚀


## Overview
The **Inventory Management System** is a Python-based application designed to help businesses efficiently manage their inventory. It provides an intuitive GUI, supports secure authentication, and offers powerful reporting features to streamline inventory tracking.

💡 Whether you're a small business owner or managing a large warehouse, this system helps you keep everything organized and under control.



## Features
- **User Authentication**: Secure login system with password hashing.🔑
- **CRUD Operations**: Add, update, delete, and view inventory items.📦
- **Inventory Tracking**: Keep track of stock levels.📊
- **Reporting**: Generate reports for sales and low-stock alerts.📉
- **Graphical User Interface (GUI)**: Simple and interactive interface using Tkinter.🖥️

## Technologies Used
- **Python**: Core programming language.
- **SQLite**: Lightweight database for storing inventory data.
- **Tkinter**: GUI framework for creating the user interface.
- **bcrypt**: Secure password hashing for authentication.
- **Pandas**: Used for generating reports.

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/leenaTIWARI/inventory-management.git
cd inventory-management
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### 1. Run the Application
```sh
python main.py
```
### 2. Add Products
- Open the GUI and click on **"Add Product"**.
- Enter product details such as name, quantity, and price.

### 3. View Inventory
- Click on **"Show Products"** to view the current stock.

### 4. Generate Reports
```sh
python reports.py
```
This will create an `inventory_report.csv` file.

## Project Structure
```
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
```

## Future Improvements
- Implement a web-based UI using Flask or Django.
- Add role-based access control for users.
- Integrate barcode scanning for faster product management.

## License
This project is open-source and available under the **MIT License**.
