"""
Sample Data for PySpark Practice
Run this to create practice DataFrames
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
from datetime import date

# Create Spark session
spark = SparkSession.builder \
    .appName("DS Practice") \
    .master("local[*]") \
    .getOrCreate()

# Sample data for employees
employees_data = [
    (1, "John Doe", "Engineering", 120000, 30),
    (2, "Jane Smith", "Engineering", 150000, 35),
    (3, "Bob Johnson", "Sales", 80000, 28),
    (4, "Alice Williams", "Engineering", 130000, 32),
    (5, "Charlie Brown", "Sales", 90000, 29),
    (6, "Diana Prince", "Marketing", 100000, 31),
    (7, "Eve Adams", "Sales", 85000, 27),
    (8, "Frank Miller", "Engineering", 140000, 38),
]

employees_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("salary", IntegerType(), True),
    StructField("age", IntegerType(), True),
])

employees_df = spark.createDataFrame(employees_data, schema=employees_schema)

# Sample data for sales
sales_data = [
    (1, date(2024, 1, 15), 1, 1000.00, 5),
    (2, date(2024, 1, 16), 2, 1500.00, 3),
    (3, date(2024, 1, 17), 1, 800.00, 2),
    (4, date(2024, 1, 18), 3, 2000.00, 4),
    (5, date(2024, 1, 19), 2, 1200.00, 3),
    (6, date(2024, 1, 20), 1, 900.00, 2),
    (7, date(2024, 1, 21), 4, 2500.00, 5),
    (8, date(2024, 1, 22), 3, 1800.00, 4),
]

sales_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("date", DateType(), True),
    StructField("employee_id", IntegerType(), True),
    StructField("amount", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
])

sales_df = spark.createDataFrame(sales_data, schema=sales_schema)

# Sample data for products
products_data = [
    (1, "Laptop", 999.99, "Electronics"),
    (2, "Mouse", 29.99, "Electronics"),
    (3, "Desk Chair", 199.99, "Furniture"),
    (4, "Monitor", 249.99, "Electronics"),
    (5, "Keyboard", 79.99, "Electronics"),
]

products_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("category", StringType(), True),
])

products_df = spark.createDataFrame(products_data, schema=products_schema)

# Sample data with NULLs for cleaning practice
data_with_nulls = [
    (1, "John", 25, 50000.0),
    (2, None, 30, 60000.0),
    (3, "Bob", None, 55000.0),
    (4, "Alice", 28, None),
    (5, "Charlie", 35, 70000.0),
]

data_with_nulls_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True),
])

data_with_nulls_df = spark.createDataFrame(data_with_nulls, schema=data_with_nulls_schema)

print("Sample DataFrames created:")
print("\nEmployees DataFrame:")
employees_df.show()

print("\nSales DataFrame:")
sales_df.show()

print("\nProducts DataFrame:")
products_df.show()

print("\nData with NULLs DataFrame:")
data_with_nulls_df.show()

# Note: Don't call spark.stop() here - keep session alive for exercises

