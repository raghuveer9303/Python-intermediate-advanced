-- Solutions to Window Functions Exercises

-- Solution 1: Running Total
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM sales
ORDER BY date;


-- Solution 2: Moving Average (3-day)
SELECT 
    date,
    amount,
    AVG(amount) OVER (
        ORDER BY date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3days
FROM sales
ORDER BY date;


-- Solution 3: Ranking Employees by Department
SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM employees
ORDER BY department, rank;


-- Solution 4: Previous Day Sales
SELECT 
    date,
    amount,
    LAG(amount, 1) OVER (ORDER BY date) as prev_amount
FROM sales
ORDER BY date;


-- Solution 5: Top 2 Employees Per Department
WITH ranked_employees AS (
    SELECT 
        name,
        department,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rn
    FROM employees
)
SELECT name, department, salary
FROM ranked_employees
WHERE rn <= 2
ORDER BY department, salary DESC;


-- Solution 6: Percentile Ranking
SELECT 
    name,
    subject,
    score,
    PERCENT_RANK() OVER (PARTITION BY subject ORDER BY score) * 100 as percentile_rank
FROM students
ORDER BY subject, percentile_rank DESC;


-- Solution 7: Difference from Average
SELECT 
    date,
    amount,
    AVG(amount) OVER () as avg_amount,
    amount - AVG(amount) OVER () as difference
FROM sales
ORDER BY date;


-- Solution 8: First and Last Value per Product
SELECT DISTINCT
    product_id,
    FIRST_VALUE(amount) OVER (
        PARTITION BY product_id 
        ORDER BY date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as first_amount,
    LAST_VALUE(amount) OVER (
        PARTITION BY product_id 
        ORDER BY date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as last_amount
FROM sales
ORDER BY product_id;

-- Alternative (simpler):
SELECT 
    product_id,
    FIRST_VALUE(amount) OVER (PARTITION BY product_id ORDER BY date) as first_amount,
    FIRST_VALUE(amount) OVER (PARTITION BY product_id ORDER BY date DESC) as last_amount
FROM sales;


-- Solution 9: Cumulative Percentage
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) * 100.0 / SUM(amount) OVER () as cumulative_percentage
FROM sales
ORDER BY date;


-- Solution 10: Row Number vs Rank vs Dense Rank
SELECT 
    name,
    score,
    ROW_NUMBER() OVER (ORDER BY score DESC) as row_number,
    RANK() OVER (ORDER BY score DESC) as rank,
    DENSE_RANK() OVER (ORDER BY score DESC) as dense_rank
FROM students
WHERE subject = 'Math'
ORDER BY score DESC;

-- Note differences:
-- ROW_NUMBER: Always unique, sequential (1, 2, 3, 4)
-- RANK: Allows gaps (1, 2, 2, 4)
-- DENSE_RANK: No gaps (1, 2, 2, 3)

