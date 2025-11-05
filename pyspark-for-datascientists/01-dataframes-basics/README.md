# 📊 PySpark DataFrames - Foundation

## Why This Matters (80-20)

**DataFrames are used in 60% of PySpark problems!**
- Structured data processing
- Lazy evaluation
- Catalyst optimizer
- Foundation for all operations

---

## 🎯 Core Concepts

### 1. Creating DataFrames
- From lists/dicts
- From CSV/Parquet files
- From existing DataFrames

### 2. Basic Operations
- `select()` - Choose columns
- `filter()` - Filter rows
- `withColumn()` - Add/modify columns
- `drop()` - Remove columns

### 3. Lazy Evaluation
- Transformations are lazy (not executed)
- Actions trigger computation
- Catalyst optimizer optimizes plan

---

## 📝 Key Operations

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit

# Create DataFrame
df = spark.createDataFrame([...])

# Select columns
df.select("col1", "col2")
df.select(col("col1"), col("col2").alias("new_name"))

# Filter
df.filter(col("age") > 25)
df.filter("age > 25")  # SQL syntax

# Add column
df.withColumn("new_col", col("col1") * 2)

# Conditional column
df.withColumn("category", when(col("age") > 30, "senior").otherwise("junior"))

# Drop column
df.drop("col1")

# Show data (action)
df.show()
df.show(10)  # First 10 rows
```

---

## 🔑 Common Patterns

### Pattern 1: Data Cleaning
```python
# Remove NULLs
df.filter(col("col1").isNotNull())

# Fill NULLs
df.fillna({"col1": 0, "col2": "unknown"})

# Drop duplicates
df.dropDuplicates()
df.dropDuplicates(["col1", "col2"])
```

### Pattern 2: Data Type Conversion
```python
from pyspark.sql.types import IntegerType, StringType

df.withColumn("age", col("age").cast(IntegerType()))
```

### Pattern 3: Rename Columns
```python
df.withColumnRenamed("old_name", "new_name")
```

---

## 🎓 Interview Tips

1. **Lazy evaluation**: Transformations don't execute until action
2. **Column references**: Use `col()` function or string
3. **SQL vs DataFrame API**: Both are valid, choose consistency
4. **Show()**: Action that triggers computation
5. **Caching**: Cache if DataFrame used multiple times

---

## 📚 Next Steps

- Complete `exercises.py`
- Review `solutions.py`
- Practice DataFrame operations
- Move to Data Transformations

