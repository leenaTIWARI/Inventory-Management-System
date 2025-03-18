import sqlite3
import bcrypt

# Register User
def register_user(username, password, role="staff"):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                       (username, hashed_pw, role))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    
    conn.close()

# Login User
def login_user(username, password):
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    
    if user and bcrypt.checkpw(password.encode(), user[0]):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

    conn.close()
