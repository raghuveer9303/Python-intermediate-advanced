# 🔗 JOINs - The Most Important SQL Concept

## Why This Matters (80-20)

**JOINs appear in 50% of DS interview problems!**
- Combining datasets
- Relational data
- Feature engineering
- Most common SQL operation

---

## 🎯 Types of JOINs

### 1. INNER JOIN
Returns only matching rows from both tables

```sql
SELECT *
FROM table1 t1
INNER JOIN table2 t2
ON t1.id = t2.id;
```

### 2. LEFT JOIN (LEFT OUTER JOIN)
Returns all rows from left table + matching rows from right

```sql
SELECT *
FROM table1 t1
LEFT JOIN table2 t2
ON t1.id = t2.id;
```

### 3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns all rows from right table + matching rows from left

```sql
SELECT *
FROM table1 t1
RIGHT JOIN table2 t2
ON t1.id = t2.id;
```

### 4. FULL OUTER JOIN
Returns all rows from both tables

```sql
SELECT *
FROM table1 t1
FULL OUTER JOIN table2 t2
ON t1.id = t2.id;
```

### 5. CROSS JOIN
Cartesian product (all combinations)

```sql
SELECT *
FROM table1
CROSS JOIN table2;
```

---

## 🔑 Common Patterns

### Pattern 1: Multiple JOINs
```sql
SELECT *
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN products p ON o.product_id = p.id;
```

### Pattern 2: Self JOIN
```sql
-- Find employees and their managers
SELECT e.name, m.name as manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

### Pattern 3: JOIN with Aggregation
```sql
SELECT c.name, COUNT(o.id) as order_count
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.name;
```

---

## 🎓 Interview Tips

1. **Default to LEFT JOIN** - Preserves all records from primary table
2. **Check for NULLs** - LEFT JOIN creates NULLs for non-matching rows
3. **Multiple conditions** - Use AND/OR in ON clause
4. **Performance** - INNER JOIN is usually faster than OUTER JOINs
5. **Aliases** - Always use table aliases for readability

---

## 📚 Next Steps

- Complete `exercises.sql`
- Review `solutions.sql`
- Practice JOIN problems
- Move to Aggregations

