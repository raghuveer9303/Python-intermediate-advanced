# 🔗 PySpark Joins & Aggregations

## Why This Matters (80-20)

**Joins and Aggregations appear in 75% of PySpark problems!**
- Combining datasets
- Grouping and summarizing
- Feature engineering
- Most common operations

---

## 🎯 Types of Joins

### 1. Inner Join
```python
df1.join(df2, df1.id == df2.id, "inner")
```

### 2. Left Join
```python
df1.join(df2, df1.id == df2.id, "left")
```

### 3. Right Join
```python
df1.join(df2, df1.id == df2.id, "right")
```

### 4. Full Outer Join
```python
df1.join(df2, df1.id == df2.id, "full")
```

### 5. Cross Join
```python
df1.crossJoin(df2)
```

---

## 📝 Aggregations

### Basic Aggregations
```python
from pyspark.sql.functions import sum, avg, count, max, min

df.groupBy("department").agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    count("*").alias("count")
)
```

### Window Functions
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, row_number

window = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("rank", rank().over(window))
```

---

## 🔑 Common Patterns

### Pattern 1: Join with Aggregation
```python
joined_df = employees_df.join(sales_df, "employee_id", "left")
result = joined_df.groupBy("department").agg(
    sum("amount").alias("total_sales")
)
```

### Pattern 2: Multiple Joins
```python
result = sales_df \
    .join(employees_df, "employee_id") \
    .join(products_df, "product_id")
```

### Pattern 3: Complex Aggregation
```python
df.groupBy("department", "category").agg(
    sum("amount").alias("total"),
    avg("amount").alias("average"),
    count("*").alias("count")
).orderBy("total", ascending=False)
```

---

## 🎓 Interview Tips

1. **Join keys**: Use consistent column names or specify join condition
2. **Broadcast join**: Use for small tables (< 2GB)
3. **GroupBy performance**: Use fewer groups when possible
4. **Null handling**: Be careful with NULLs in joins
5. **Aliases**: Use aliases to avoid column name conflicts

---

## 📚 Next Steps

- Complete `exercises.py`
- Review `solutions.py`
- Practice join and aggregation problems
- Move to Window Functions

