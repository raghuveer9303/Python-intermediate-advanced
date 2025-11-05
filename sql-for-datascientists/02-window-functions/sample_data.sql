-- Sample Data for Window Functions Practice

-- Sales table
CREATE TABLE sales (
    id INT PRIMARY KEY,
    date DATE,
    product_id INT,
    amount DECIMAL(10, 2),
    quantity INT
);

INSERT INTO sales VALUES
(1, '2024-01-01', 1, 100.00, 2),
(2, '2024-01-02', 1, 150.00, 3),
(3, '2024-01-03', 2, 200.00, 1),
(4, '2024-01-04', 1, 120.00, 2),
(5, '2024-01-05', 2, 250.00, 2),
(6, '2024-01-06', 1, 180.00, 4),
(7, '2024-01-07', 3, 300.00, 1),
(8, '2024-01-08', 2, 220.00, 2),
(9, '2024-01-09', 1, 140.00, 3),
(10, '2024-01-10', 3, 350.00, 2);

-- Employees table (for ranking)
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees VALUES
(1, 'John', 'Engineering', 120000),
(2, 'Jane', 'Engineering', 150000),
(3, 'Bob', 'Sales', 80000),
(4, 'Alice', 'Engineering', 130000),
(5, 'Charlie', 'Sales', 90000),
(6, 'Diana', 'Marketing', 100000),
(7, 'Eve', 'Sales', 85000),
(8, 'Frank', 'Engineering', 140000);

-- Students table (for ranking)
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(50),
    score INT
);

INSERT INTO students VALUES
(1, 'Alice', 'Math', 95),
(2, 'Bob', 'Math', 87),
(3, 'Charlie', 'Math', 92),
(4, 'Diana', 'Math', 95),
(5, 'Eve', 'Science', 88),
(6, 'Frank', 'Science', 92),
(7, 'Grace', 'Science', 85),
(8, 'Henry', 'Science', 90);

