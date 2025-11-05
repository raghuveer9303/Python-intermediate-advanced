"""
PySpark Joins & Aggregations - Hands-On Exercises
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, max, min

# Exercise 1: Inner Join
# Join employees and sales on employee_id
def join_employees_sales(employees_df, sales_df):
    """
    Input: employees_df, sales_df
    Output: Joined DataFrame with employee and sales info
    """
    # TODO: Your code here
    pass


# Exercise 2: Left Join
# Join employees and sales (keep all employees)
def left_join_employees_sales(employees_df, sales_df):
    """
    Input: employees_df, sales_df
    Output: All employees with their sales (NULL if no sales)
    """
    # TODO: Your code here
    pass


# Exercise 3: Group By Department
# Calculate total salary per department
def salary_by_department(employees_df):
    """
    Input: employees_df
    Output: DataFrame with department and total_salary
    """
    # TODO: Your code here
    pass


# Exercise 4: Multiple Aggregations
# Calculate total, average, max, min salary per department
def department_stats(employees_df):
    """
    Input: employees_df
    Output: DataFrame with department and multiple salary stats
    """
    # TODO: Your code here
    pass


# Exercise 5: Join with Aggregation
# Calculate total sales per employee department
def sales_by_department(employees_df, sales_df):
    """
    Input: employees_df, sales_df
    Output: Total sales amount per department
    """
    # TODO: Your code here
    pass


# Exercise 6: Count Employees per Department
# Count number of employees in each department
def count_by_department(employees_df):
    """
    Input: employees_df
    Output: Department and employee count
    """
    # TODO: Your code here
    pass


# Exercise 7: Average Age by Department
# Calculate average age per department
def avg_age_by_department(employees_df):
    """
    Input: employees_df
    Output: Department and average age
    """
    # TODO: Your code here
    pass


# Exercise 8: Top N Employees by Salary
# Find top 3 employees by salary in each department
def top_employees_by_department(employees_df, n=3):
    """
    Input: employees_df, n
    Output: Top n employees per department by salary
    Hint: Use window functions
    """
    # TODO: Your code here
    pass


# Exercise 9: Sales Summary
# Calculate total sales, count, and average per employee
def employee_sales_summary(employees_df, sales_df):
    """
    Input: employees_df, sales_df
    Output: Employee name, total_sales, sale_count, avg_sale
    """
    # TODO: Your code here
    pass


# Exercise 10: Complex Join
# Join employees, sales, and products to get complete sales info
def complete_sales_info(employees_df, sales_df, products_df):
    """
    Input: employees_df, sales_df, products_df
    Output: DataFrame with employee name, product name, sale amount
    """
    # TODO: Your code here
    pass


# Test your functions
if __name__ == "__main__":
    print("Run sample_data.py first, then test your functions here")

