# 🔥 PySpark for Data Scientists - Interview Preparation
## 80-20 Learning Plan - Hands-On Focus

**Expert Principal Data Scientist Perspective**

This guide focuses on the **20% of PySpark concepts that solve 80% of data science problems**.

---

## 📋 Learning Path Overview

### Phase 1: Foundation (Week 1)
1. **DataFrames & Basics** - Core PySpark operations
2. **Data Transformation** - Filter, select, groupby
3. **Data Cleaning** - Handling NULLs, duplicates, data types

### Phase 2: Advanced Operations (Week 2)
4. **Joins** - Combining DataFrames
5. **Window Functions** - Ranking, moving averages
6. **Aggregations** - Complex aggregations

### Phase 3: Optimization (Week 3)
7. **Partitioning** - Performance optimization
8. **Broadcasting** - Small table optimization
9. **Caching** - Memory optimization

### Phase 4: Real-World Patterns (Week 4)
10. **Common DS Patterns** - Feature engineering, ETL
11. **Performance Tuning** - Optimization techniques
12. **Interview Patterns** - Common interview questions

---

## 🎯 Why These Topics? (80-20 Analysis)

### High Frequency in DS Interviews:
- **DataFrames**: 60% of problems
- **Transformations**: 50% of problems
- **Joins**: 40% of problems
- **Window Functions**: 30% of problems
- **Aggregations**: 35% of problems

### Data Science Specific:
- **Large-scale data processing**
- **Feature engineering**
- **ETL pipelines**
- **Data quality checks**

---

## 📁 Structure

Each topic folder contains:
- `README.md` - Concepts, API, examples
- `exercises.py` - Hands-on practice problems
- `solutions.py` - Complete solutions with explanations
- `sample_data.py` - Sample data creation

---

## 🚀 Quick Start

1. Install PySpark:
```bash
pip install pyspark
```

2. Set up Jupyter notebook or Python environment
3. Start with **Phase 1** topics
4. Run `sample_data.py` to create practice DataFrames
5. Complete exercises **without** looking at solutions
6. Review solutions and understand patterns

---

## 📊 Success Metrics

- ✅ Can create and manipulate DataFrames
- ✅ Understand lazy evaluation
- ✅ Can optimize Spark jobs
- ✅ Write efficient joins and aggregations
- ✅ Handle large datasets efficiently

---

## 🛠️ Setup

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

---

**Remember**: PySpark uses lazy evaluation. Actions trigger computation!

