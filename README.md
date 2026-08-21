# 💊 Pharmacy Billing System

A desktop-based **Pharmacy Billing System** developed using **Python, Tkinter, and MySQL**.

The application provides a simple interface for pharmacy staff to log in, manage products, view inventory, and generate customer bills while automatically updating product stock.

## ✨ Features

* 🔐 Admin login authentication
* 💵 Pharmacy billing system
* 👤 Customer management
* 📦 Add new products
* 📊 View product inventory
* 🔄 Automatic stock deduction after billing
* 🧾 Display billing information with date and time
* 🗄️ MySQL database integration
* 🖥️ Desktop GUI using Tkinter
* ⚠️ Error handling for insufficient stock and invalid products

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – Graphical User Interface
* **MySQL** – Database management
* **MySQL Connector/Python** – Python-to-MySQL connection
* **datetime** – Date and time handling

## 📂 Project Structure

```text
Pharmacy-Billing-System/
│
├── pharmacy.py
├── database.sql
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File               | Description                                 |
| ------------------ | ------------------------------------------- |
| `pharmacy.py`      | Main Python application                     |
| `database.sql`     | MySQL database and table creation script    |
| `requirements.txt` | Required Python packages                    |
| `README.md`        | Project documentation                       |
| `.gitignore`       | Files that should not be uploaded to GitHub |

## 🗄️ Database

The application uses a MySQL database named:

```text
pharmacy
```

### Customers Table

```text
Customers
├── customer_code
├── customer_name
└── phone_number
```

### Products Table

```text
Products
├── product_id
├── product_name
├── price
└── quantity_in_stock
```

## 🚀 Installation

### 1. Install Python

Download and install Python 3 from the official Python website.

Verify the installation:

```bash
python --version
```

## 2. Install MySQL

Install MySQL Server and MySQL Workbench if required.

Make sure the MySQL server is running before starting the application.

## 3. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Pharmacy-Billing-System.git
```

Move into the project directory:

```bash
cd Pharmacy-Billing-System
```

## 4. Install Python Dependencies

Run:

```bash
pip install -r requirements.txt
```

## 5. Create the Database

Open MySQL Workbench or MySQL Command Line and execute:

```bash
source database.sql;
```

Alternatively, copy and execute the contents of `database.sql` manually in MySQL Workbench.

## ⚙️ Database Configuration

The application connects to MySQL using:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="pharmacy"
)
```

Replace `YOUR_PASSWORD` with your local MySQL password.

> ⚠️ Never upload your real MySQL password to a public GitHub repository.

For a production version, database credentials should be stored using environment variables.

## 🔐 Login

The current application uses a simple administrator login.

```text
Username: ADMIN
Password: shree
```

> ⚠️ This is a demo authentication system. For a production application, passwords should be stored securely using password hashing instead of being directly written in the source code.

## 🧾 Billing

The billing module allows the user to:

1. Select a customer code.
2. Automatically retrieve the customer's name and phone number.
3. Select a product.
4. Enter the required quantity.
5. Check available stock.
6. Calculate the product's total price.
7. Add the transaction to the bill.
8. Automatically reduce the product stock in MySQL.

Example:

```text
Product      Quantity      Total
---------------------------------
Paracetamol     2          40.00
```

## 📦 Product Management

The **Add Product** section allows the administrator to enter:

* Product name
* Product price
* Stock quantity

The information is stored directly in the MySQL `Products` table.

## 📊 Inventory

The **View Inventory** section displays:

```text
Product Name | Price | Stock Quantity
```

This allows pharmacy staff to quickly check the available products and their current stock.

## 🔄 Stock Management

When a product is added to a bill, the application automatically updates the stock.

For example:

```text
Initial Stock = 100
Purchased     = 5
Remaining     = 95
```

The database is updated using an SQL `UPDATE` statement.

## 🖥️ Application Modules

### 🔐 Authentication Module

Provides administrator login functionality.

### 💰 Billing Module

Handles customer selection, product selection, quantity, price calculation, and stock updates.

### 📦 Product Module

Allows administrators to add products to the pharmacy inventory.

### 📊 Inventory Module

Displays available products, prices, and stock quantities.

## 🎯 Project Objectives

The main objectives of this project are:

* To develop a simple pharmacy management application.
* To practice Python GUI development using Tkinter.
* To understand database connectivity using MySQL.
* To implement CRUD-related database operations.
* To automate pharmacy billing.
* To maintain product stock automatically.
* To provide an easy-to-use desktop interface.

## 🔮 Future Improvements

Possible improvements for future versions include:

* [ ] Add customer registration interface
* [ ] Add customer update/delete functionality
* [ ] Add product update/delete functionality
* [ ] Add complete invoice generation
* [ ] Add PDF invoice printing
* [ ] Add billing history
* [ ] Add sales reports
* [ ] Add low-stock alerts
* [ ] Add search functionality
* [ ] Add multiple user accounts
* [ ] Add secure password hashing
* [ ] Add environment variables for database credentials
* [ ] Improve the user interface
* [ ] Add medicine expiry-date tracking
* [ ] Add medicine category management

## ⚠️ Important Notes

This project is intended primarily for **educational and demonstration purposes**.

The current version contains simplified authentication and database configuration. Before using it in a real pharmacy environment, proper security, authentication, transaction management, validation, audit logging, and regulatory requirements should be implemented.

## 📄 License

This project is open-source and can be used for educational and personal learning purposes.

## 👨‍💻 Author

**Your Name**

Built with ❤️ using **Python, Tkinter, and MySQL**.
