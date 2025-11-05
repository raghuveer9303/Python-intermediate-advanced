"""
Solutions to PySpark DataFrame Basics Exercises
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, upper, lower
from pyspark.sql.types import IntegerType

# Solution 1: Select Specific Columns
def select_columns(df):
    return df.select("name", "salary")

# Alternative:
# return df.select(col("name"), col("salary"))


# Solution 2: Filter Rows
def filter_high_salary(df):
    return df.filter(col("salary") > 100000)

# Alternative (SQL syntax):
# return df.filter("salary > 100000")


# Solution 3: Add New Column
def add_bonus_column(df):
    return df.withColumn("bonus", col("salary") * 0.1)


# Solution 4: Conditional Column
def add_experience_level(df):
    return df.withColumn(
        "experience_level",
        when(col("age") >= 35, "senior")
        .when(col("age") >= 30, "mid")
        .otherwise("junior")
    )


# Solution 5: Rename Column
def rename_column(df):
    return df.withColumnRenamed("department", "dept")


# Solution 6: Handle NULLs
def fill_nulls(df):
    return df.fillna({
        "name": "Unknown",
        "age": 0,
        "salary": 0.0
    })


# Solution 7: Drop NULLs
def drop_null_names(df):
    return df.filter(col("name").isNotNull())

# Alternative:
# return df.na.drop(subset=["name"])


# Solution 8: Drop Duplicates
def remove_duplicates(df):
    return df.dropDuplicates()

# Remove duplicates based on specific columns:
# return df.dropDuplicates(["col1", "col2"])


# Solution 9: Cast Data Types
def cast_salary_to_int(df):
    return df.withColumn("salary", col("salary").cast(IntegerType()))


# Solution 10: String Operations
def uppercase_names(df):
    return df.withColumn("name", upper(col("name")))

# Other string operations:
# lower(), substring(), trim(), length(), etc.


# Test solutions
if __name__ == "__main__":
    from sample_data import employees_df, data_with_nulls_df
    
    print("Testing Solutions:")
    
    print("\n1. Select Columns:")
    select_columns(employees_df).show()
    
    print("\n2. Filter High Salary:")
    filter_high_salary(employees_df).show()
    
    print("\n3. Add Bonus Column:")
    add_bonus_column(employees_df).show()
    
    print("\n4. Add Experience Level:")
    add_experience_level(employees_df).show()
    
    print("\n5. Rename Column:")
    rename_column(employees_df).show()
    
    print("\n6. Fill NULLs:")
    fill_nulls(data_with_nulls_df).show()
    
    print("\n7. Drop NULL Names:")
    drop_null_names(data_with_nulls_df).show()
    
    print("\n8. Remove Duplicates:")
    remove_duplicates(employees_df).show()
    
    print("\n9. Cast Salary to Int:")
    cast_salary_to_int(employees_df).show()
    
    print("\n10. Uppercase Names:")
    uppercase_names(employees_df).show()
    
    print("\n🎉 All solutions executed!")

