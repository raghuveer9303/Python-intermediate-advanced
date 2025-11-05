"""
PySpark DataFrame Basics - Hands-On Exercises
Run sample_data.py first to create DataFrames
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, upper, lower, round

# Create or get Spark session
spark = SparkSession.builder \
    .appName("DS Practice") \
    .master("local[*]") \
    .getOrCreate()

# Import sample data (run sample_data.py first or import here)
# For this exercise, assume employees_df, sales_df, products_df exist

# Exercise 1: Select Specific Columns
# Select only name and salary from employees DataFrame
def select_columns(df):
    """
    Input: employees_df
    Output: DataFrame with only name and salary columns
    """
    # TODO: Your code here
    pass


# Exercise 2: Filter Rows
# Filter employees with salary > 100000
def filter_high_salary(df):
    """
    Input: employees_df
    Output: DataFrame with employees having salary > 100000
    """
    # TODO: Your code here
    pass


# Exercise 3: Add New Column
# Add a column "bonus" that is 10% of salary
def add_bonus_column(df):
    """
    Input: employees_df
    Output: DataFrame with new "bonus" column
    """
    # TODO: Your code here
    pass


# Exercise 4: Conditional Column
# Add column "experience_level" based on age:
# - "senior" if age >= 35
# - "mid" if age >= 30
# - "junior" otherwise
def add_experience_level(df):
    """
    Input: employees_df
    Output: DataFrame with "experience_level" column
    """
    # TODO: Your code here
    pass


# Exercise 5: Rename Column
# Rename "department" to "dept"
def rename_column(df):
    """
    Input: employees_df
    Output: DataFrame with renamed column
    """
    # TODO: Your code here
    pass


# Exercise 6: Handle NULLs
# Fill NULL values in name with "Unknown", age with 0, salary with 0.0
def fill_nulls(df):
    """
    Input: data_with_nulls_df
    Output: DataFrame with NULLs filled
    """
    # TODO: Your code here
    pass


# Exercise 7: Drop NULLs
# Drop rows where name is NULL
def drop_null_names(df):
    """
    Input: data_with_nulls_df
    Output: DataFrame without NULL names
    """
    # TODO: Your code here
    pass


# Exercise 8: Drop Duplicates
# Remove duplicate rows based on all columns
def remove_duplicates(df):
    """
    Input: DataFrame (may have duplicates)
    Output: DataFrame without duplicates
    """
    # TODO: Your code here
    pass


# Exercise 9: Cast Data Types
# Convert salary column to IntegerType
def cast_salary_to_int(df):
    """
    Input: employees_df
    Output: DataFrame with salary as integer
    """
    # TODO: Your code here
    pass


# Exercise 10: String Operations
# Convert name column to uppercase
def uppercase_names(df):
    """
    Input: employees_df
    Output: DataFrame with uppercase names
    """
    # TODO: Your code here
    pass


# Test your functions
if __name__ == "__main__":
    # Run sample_data.py first to create DataFrames
    # Then test your functions
    
    # Example:
    # result = select_columns(employees_df)
    # result.show()
    
    print("Run sample_data.py first, then test your functions here")

