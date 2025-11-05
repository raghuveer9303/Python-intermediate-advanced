-- Solutions to JOIN Exercises

-- Solution 1: Basic INNER JOIN
SELECT c.name, o.id as order_id
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id;

-- Alternative (implicit join - not recommended)
-- SELECT c.name, o.id FROM customers c, orders o WHERE c.id = o.customer_id;


-- Solution 2: LEFT JOIN
SELECT c.name, COUNT(o.id) as order_count
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.name
ORDER BY order_count DESC;


-- Solution 3: Multiple JOINs
SELECT 
    o.id as order_id,
    c.name as customer_name,
    p.name as product_name,
    oi.quantity,
    oi.price
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;


-- Solution 4: Self JOIN
SELECT 
    e.name as employee_name,
    m.name as manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;


-- Solution 5: JOIN with WHERE
SELECT 
    c.name,
    o.id as order_id,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
WHERE c.city = 'New York';


-- Solution 6: JOIN with Aggregation
SELECT 
    c.name as customer_name,
    COALESCE(SUM(o.total_amount), 0) as total_revenue
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.name
ORDER BY total_revenue DESC;


-- Solution 7: Customers who never placed an order
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;

-- Alternative using NOT IN (less efficient)
-- SELECT name FROM customers WHERE id NOT IN (SELECT customer_id FROM orders WHERE customer_id IS NOT NULL);


-- Solution 8: Multiple Conditions in JOIN
SELECT 
    c.name,
    o.id as order_id,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY o.order_date DESC;

-- PostgreSQL version:
-- WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'

-- MySQL version:
-- WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)


-- Solution 9: JOIN with Subquery
SELECT 
    c.name,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
WHERE o.total_amount > (
    SELECT AVG(total_amount) 
    FROM orders
);


-- Solution 10: CROSS JOIN
SELECT 
    c.name as customer_name,
    p.name as product_name
FROM customers c
CROSS JOIN products p
ORDER BY c.name, p.name;

-- Alternative syntax:
-- SELECT c.name, p.name FROM customers c, products p;

