-- JOIN Exercises - Complete these to master JOINs

-- Exercise 1: Basic INNER JOIN
-- Write a query to get customer names and their order IDs
-- Tables: customers, orders
-- Expected: Show customer name and order id for all orders

-- TODO: Your query here


-- Exercise 2: LEFT JOIN
-- Write a query to get all customers and their order count (even if 0 orders)
-- Tables: customers, orders
-- Expected: Show customer name and count of orders (0 if no orders)

-- TODO: Your query here


-- Exercise 3: Multiple JOINs
-- Write a query to get order details with customer name and product name
-- Tables: orders, customers, order_items, products
-- Expected: Show order_id, customer_name, product_name, quantity, price

-- TODO: Your query here


-- Exercise 4: Self JOIN
-- Write a query to show employees and their manager names
-- Tables: employees (self-join)
-- Expected: Show employee_name, manager_name (NULL if no manager)

-- TODO: Your query here


-- Exercise 5: JOIN with WHERE
-- Write a query to find customers from 'New York' who placed orders
-- Tables: customers, orders
-- Expected: Show customer name and order details for NY customers only

-- TODO: Your query here


-- Exercise 6: JOIN with Aggregation
-- Write a query to find total revenue per customer
-- Tables: customers, orders
-- Expected: Show customer_name, total_revenue

-- TODO: Your query here


-- Exercise 7: Complex JOIN
-- Write a query to find customers who never placed an order
-- Tables: customers, orders
-- Expected: Show customer names who have no orders

-- TODO: Your query here


-- Exercise 8: Multiple Conditions in JOIN
-- Write a query to find orders placed in the last 30 days with customer details
-- Tables: customers, orders
-- Expected: Show order details for recent orders

-- TODO: Your query here
-- Hint: Use CURRENT_DATE or NOW() for date comparison


-- Exercise 9: JOIN with Subquery
-- Write a query to find customers who placed orders above average order value
-- Tables: customers, orders
-- Expected: Show customer names and order amounts above average

-- TODO: Your query here


-- Exercise 10: CROSS JOIN
-- Write a query to create all possible combinations of products and customers
-- Tables: customers, products
-- Expected: Show all customer-product combinations

-- TODO: Your query here

