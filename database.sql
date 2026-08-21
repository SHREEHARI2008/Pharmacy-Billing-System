CREATE DATABASE IF NOT EXISTS pharmacy;

USE pharmacy;

CREATE TABLE IF NOT EXISTS Customers (
    customer_code INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255),
    phone_number VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity_in_stock INT NOT NULL
);

INSERT INTO Products (product_name, price, quantity_in_stock)
VALUES
('Paracetamol', 20.00, 100),
('Amoxicillin', 50.00, 50),
('Vitamin C', 30.00, 75);

INSERT INTO Customers (customer_name, phone_number)
VALUES
('John', '9876543210'),
('Arun', '9876501234');