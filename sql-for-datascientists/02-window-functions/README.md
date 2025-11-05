# 🪟 Window Functions - Advanced Analytics

## Why This Matters (80-20)

**Window Functions appear in 30% of DS interview problems!**
- Time series analysis
- Ranking and percentiles
- Moving averages
- Essential for data science

---

## 🎯 Types of Window Functions

### 1. Ranking Functions
- `ROW_NUMBER()` - Sequential numbering
- `RANK()` - Ranking with gaps
- `DENSE_RANK()` - Ranking without gaps
- `NTILE(n)` - Divide into n groups

### 2. Aggregate Window Functions
- `SUM() OVER()` - Running sum
- `AVG() OVER()` - Moving average
- `COUNT() OVER()` - Running count
- `MAX() OVER()` / `MIN() OVER()` - Running max/min

### 3. Value Functions
- `LAG()` - Previous row value
- `LEAD()` - Next row value
- `FIRST_VALUE()` - First value in window
- `LAST_VALUE()` - Last value in window

---

## 📝 Syntax

```sql
SELECT 
    column,
    FUNCTION() OVER (
        PARTITION BY column
        ORDER BY column
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as result
FROM table;
```

---

## 🔑 Common Patterns

### Pattern 1: Running Total
```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;
```

### Pattern 2: Moving Average
```sql
SELECT 
    date,
    amount,
    AVG(amount) OVER (
        ORDER BY date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as moving_avg_7days
FROM daily_sales;
```

### Pattern 3: Ranking
```sql
SELECT 
    name,
    score,
    RANK() OVER (ORDER BY score DESC) as rank
FROM students;
```

### Pattern 4: Previous/Next Value
```sql
SELECT 
    date,
    amount,
    LAG(amount, 1) OVER (ORDER BY date) as prev_amount,
    LEAD(amount, 1) OVER (ORDER BY date) as next_amount
FROM transactions;
```

---

## 🎓 Interview Tips

1. **PARTITION BY** - Creates separate windows for each group
2. **ORDER BY** - Defines order within window
3. **ROWS vs RANGE** - ROWS is physical, RANGE is logical
4. **Frame specification** - Controls window size
5. **Performance** - Window functions can be slow on large datasets

---

## 📚 Next Steps

- Complete `exercises.sql`
- Review `solutions.sql`
- Practice window function problems
- Move to Aggregations

