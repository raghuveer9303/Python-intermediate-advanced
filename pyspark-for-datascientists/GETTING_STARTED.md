# 🚀 Getting Started with PySpark for Data Scientists

## Quick Start Guide

### 1. Prerequisites
- Python 3.7+
- Basic Python and pandas knowledge
- Understanding of big data concepts

### 2. Setup

#### Install PySpark
```bash
pip install pyspark
```

#### Alternative: Use Databricks Community Edition
- Free cloud environment
- Pre-configured Spark
- Good for learning

### 3. Basic Setup Code

```python
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("DS Practice") \
    .master("local[*]") \
    .getOrCreate()

# Your code here

spark.stop()
```

### 4. Learning Order

**Week 1: Foundation**
1. Start with `01-dataframes-basics/`
   - Run `sample_data.py` to create DataFrames
   - Complete `exercises.py`
   - Review `solutions.py`
2. Understand lazy evaluation

**Week 2: Advanced Operations**
1. Move to `02-joins-aggregations/`
2. Practice joins and aggregations
3. Learn window functions

**Week 3-4: Optimization**
1. Learn partitioning
2. Understand broadcasting
3. Performance tuning
4. Real-world patterns

### 5. How to Use This Guide

1. **Run sample_data.py** - Create practice DataFrames
2. **Read README.md** - Understand concepts
3. **Attempt exercises.py** - Write your code
4. **Review solutions.py** - Compare approaches
5. **Practice on real datasets** - Apply to your work

### 6. Key Concepts

- **Lazy Evaluation**: Transformations don't execute until action
- **Actions**: `show()`, `collect()`, `count()` trigger computation
- **Transformations**: `select()`, `filter()`, `join()` are lazy
- **Partitioning**: Affects performance significantly
- **Caching**: Use when DataFrame used multiple times

### 7. Practice Tips

- ✅ Understand lazy evaluation
- ✅ Use `.explain()` to see execution plan
- ✅ Monitor Spark UI for performance
- ✅ Practice with large datasets
- ✅ Learn optimization techniques

### 8. Common Mistakes to Avoid

- ❌ Collecting large DataFrames to driver
- ❌ Not using partitioning effectively
- ❌ Forgetting to cache reused DataFrames
- ❌ Using Python UDFs when SQL functions work
- ❌ Not understanding lazy evaluation

---

**Remember**: PySpark is about distributed computing. Think in terms of transformations and actions!

