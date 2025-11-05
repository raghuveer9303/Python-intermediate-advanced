-- Sample Data for JOIN Practice
-- Run this first to create practice tables

-- Customers table
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'John Doe', 'john@example.com', 'New York'),
(2, 'Jane Smith', 'jane@example.com', 'Los Angeles'),
(3, 'Bob Johnson', 'bob@example.com', 'Chicago'),
(4, 'Alice Williams', 'alice@example.com', 'New York'),
(5, 'Charlie Brown', 'charlie@example.com', 'Boston');

-- Orders table
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO orders VALUES
(1, 1, '2024-01-15', 150.00),
(2, 1, '2024-02-20', 200.00),
(3, 2, '2024-01-10', 75.50),
(4, 3, '2024-03-05', 300.00),
(5, NULL, '2024-03-10', 50.00);  -- Order without customer

-- Products table
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    category VARCHAR(50)
);

INSERT INTO products VALUES
(1, 'Laptop', 999.99, 'Electronics'),
(2, 'Mouse', 29.99, 'Electronics'),
(3, 'Desk Chair', 199.99, 'Furniture'),
(4, 'Monitor', 249.99, 'Electronics'),
(5, 'Keyboard', 79.99, 'Electronics');

-- Order Items table
CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO order_items VALUES
(1, 1, 1, 1, 999.99),
(2, 1, 2, 2, 29.99),
(3, 2, 3, 1, 199.99),
(4, 3, 4, 1, 249.99),
(5, 4, 1, 1, 999.99),
(6, 4, 4, 2, 249.99);

-- Employees table (for self-join practice)
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT,
    salary DECIMAL(10, 2),
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

INSERT INTO employees VALUES
(1, 'CEO', NULL, 200000),
(2, 'VP Engineering', 1, 150000),
(3, 'VP Sales', 1, 140000),
(4, 'Senior Engineer', 2, 120000),
(5, 'Junior Engineer', 2, 80000),
(6, 'Sales Manager', 3, 100000),
(7, 'Sales Rep', 6, 60000);

