import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="pharmacy"
)
cursor = db.cursor()

# Authentication
def authenticate():
    def validate_login():
        username = user_entry.get()
        password = pass_entry.get()
        if username == "ADMIN" and password == "shree":
            login.destroy()
            main_menu()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    login = tk.Tk()
    login.title("Login")
    login.geometry("300x200")

    tk.Label(login, text="Username").pack(pady=10)
    user_entry = tk.Entry(login)
    user_entry.pack(pady=5)

    tk.Label(login, text="Password").pack(pady=10)
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack(pady=5)

    tk.Button(login, text="Login", command=validate_login).pack(pady=20)

    login.mainloop()

# Main Menu
def main_menu():
    root = tk.Tk()
    root.title("Pharmacy Billing System")
    root.geometry("500x400")
    root.configure(bg="#dff9fb")

    tk.Label(root, text="Pharmacy Billing System", font=("Arial", 20), bg="#dff9fb").pack(pady=20)

    tk.Button(root, text="Billing", command=billing_window, width=20).pack(pady=10)
    tk.Button(root, text="Add Product", command=add_product_window, width=20).pack(pady=10)
    tk.Button(root, text="View Inventory", command=view_inventory_window, width=20).pack(pady=10)

    root.mainloop()

# Billing Window
def billing_window():
    billing = tk.Toplevel()
    billing.title("Billing")
    billing.geometry("600x500")
    billing.configure(bg="#f6e58d")

    tk.Label(billing, text="Customer Code", bg="#f6e58d").grid(row=0, column=0, padx=10, pady=10)
    customer_code = ttk.Combobox(billing)
    customer_code.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(billing, text="Customer Name", bg="#f6e58d").grid(row=1, column=0, padx=10, pady=10)
    customer_name = tk.Entry(billing, state="readonly")
    customer_name.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(billing, text="Phone Number", bg="#f6e58d").grid(row=2, column=0, padx=10, pady=10)
    phone_number = tk.Entry(billing, state="readonly")
    phone_number.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(billing, text="Product", bg="#f6e58d").grid(row=3, column=0, padx=10, pady=10)
    product_name = ttk.Combobox(billing, state="readonly")
    product_name.grid(row=3, column=1, padx=10, pady=10)

    # Fetch product names for dropdown
    cursor.execute("SELECT product_name FROM Products")
    product_list = [row[0] for row in cursor.fetchall()]
    product_name["values"] = product_list

    tk.Label(billing, text="Quantity", bg="#f6e58d").grid(row=4, column=0, padx=10, pady=10)
    quantity = tk.Entry(billing)
    quantity.grid(row=4, column=1, padx=10, pady=10)

    bill_area = tk.Text(billing, height=15, width=50)
    bill_area.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Fetch customer codes for dropdown
    cursor.execute("SELECT customer_code FROM Customers")
    customer_list = [row[0] for row in cursor.fetchall()]
    customer_code["values"] = customer_list

    def fetch_customer_details(event):
        code = customer_code.get()
        cursor.execute("SELECT customer_name, phone_number FROM Customers WHERE customer_code = %s", (code,))
        result = cursor.fetchone()
        if result:
            customer_name.config(state="normal")
            phone_number.config(state="normal")
            customer_name.delete(0, tk.END)
            phone_number.delete(0, tk.END)
            customer_name.insert(0, result[0])
            phone_number.insert(0, result[1])
            customer_name.config(state="readonly")
            phone_number.config(state="readonly")

    customer_code.bind("<<ComboboxSelected>>", fetch_customer_details)

    def add_to_bill():
        cust_code = customer_code.get()
        prod_name = product_name.get()
        qty = int(quantity.get())

        # Fetch product details
        cursor.execute("SELECT price, quantity_in_stock FROM Products WHERE product_name = %s", (prod_name,))
        result = cursor.fetchone()

        if result:
            price, stock = result
            if qty <= stock:
                total_price = qty * price
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                bill_area.insert(tk.END, f"{current_time} | {prod_name} \t {qty} \t {total_price}\n")

                # Update stock in database
                cursor.execute("UPDATE Products SET quantity_in_stock = quantity_in_stock - %s WHERE product_name = %s", (qty, prod_name))
                db.commit()
            else:
                messagebox.showerror("Error", "Insufficient stock")
        else:
            messagebox.showerror("Error", "Product not found")

    tk.Button(billing, text="Add to Bill", command=add_to_bill).grid(row=7, column=0, columnspan=2, pady=10)

# Add Product Window
def add_product_window():
    add_product = tk.Toplevel()
    add_product.title("Add Product")
    add_product.geometry("400x300")
    add_product.configure(bg="#badc58")

    tk.Label(add_product, text="Product Name", bg="#badc58").grid(row=0, column=0, padx=10, pady=10)
    product_name = tk.Entry(add_product)
    product_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_product, text="Price", bg="#badc58").grid(row=1, column=0, padx=10, pady=10)
    price = tk.Entry(add_product)
    price.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_product, text="Stock Quantity", bg="#badc58").grid(row=2, column=0, padx=10, pady=10)
    stock = tk.Entry(add_product)
    stock.grid(row=2, column=1, padx=10, pady=10)

    def add_product_to_db():
        name = product_name.get()
        prod_price = float(price.get())
        prod_stock = int(stock.get())

        cursor.execute("INSERT INTO Products (product_name, price, quantity_in_stock) VALUES (%s, %s, %s)", (name, prod_price, prod_stock))
        db.commit()
        messagebox.showinfo("Success", "Product added successfully")

    tk.Button(add_product, text="Add Product", command=add_product_to_db).grid(row=3, column=0, columnspan=2, pady=20)

# View Inventory Window
def view_inventory_window():
    inventory = tk.Toplevel()
    inventory.title("Inventory")
    inventory.geometry("600x400")
    inventory.configure(bg="#7ed6df")

    tk.Label(inventory, text="Product Name", font=("Arial", 12), bg="#7ed6df").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(inventory, text="Price", font=("Arial", 12), bg="#7ed6df").grid(row=0, column=1, padx=10, pady=10)
    tk.Label(inventory, text="Stock Quantity", font=("Arial", 12), bg="#7ed6df").grid(row=0, column=2, padx=10, pady=10)

    cursor.execute("SELECT product_name, price, quantity_in_stock FROM Products")
    for i, (name, price, stock) in enumerate(cursor.fetchall(), start=1):
        tk.Label(inventory, text=name, bg="#7ed6df").grid(row=i, column=0, padx=10, pady=5)
        tk.Label(inventory, text=price, bg="#7ed6df").grid(row=i, column=1, padx=10, pady=5)
        tk.Label(inventory, text=stock, bg="#7ed6df").grid(row=i, column=2, padx=10, pady=5)

# Add Customer Database
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_code INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255),
    phone_number VARCHAR(15)
)
""")
db.commit()

# Start the application
authenticate()
