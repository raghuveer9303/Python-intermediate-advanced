"""
Solutions to PySpark Joins & Aggregations Exercises
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, max, min
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# Solution 1: Inner Join
def join_employees_sales(employees_df, sales_df):
    return employees_df.join(
        sales_df,
        employees_df.id == sales_df.employee_id,
        "inner"
    )

# Alternative (if column names match):
# return employees_df.join(sales_df, "employee_id", "inner")


# Solution 2: Left Join
def left_join_employees_sales(employees_df, sales_df):
    return employees_df.join(
        sales_df,
        employees_df.id == sales_df.employee_id,
        "left"
    )


# Solution 3: Group By Department
def salary_by_department(employees_df):
    return employees_df.groupBy("department").agg(
        sum("salary").alias("total_salary")
    )


# Solution 4: Multiple Aggregations
def department_stats(employees_df):
    return employees_df.groupBy("department").agg(
        sum("salary").alias("total_salary"),
        avg("salary").alias("avg_salary"),
        max("salary").alias("max_salary"),
        min("salary").alias("min_salary")
    )


# Solution 5: Join with Aggregation
def sales_by_department(employees_df, sales_df):
    joined = employees_df.join(
        sales_df,
        employees_df.id == sales_df.employee_id,
        "left"
    )
    return joined.groupBy("department").agg(
        sum("amount").alias("total_sales")
    )


# Solution 6: Count Employees per Department
def count_by_department(employees_df):
    return employees_df.groupBy("department").agg(
        count("*").alias("employee_count")
    )


# Solution 7: Average Age by Department
def avg_age_by_department(employees_df):
    return employees_df.groupBy("department").agg(
        avg("age").alias("avg_age")
    )


# Solution 8: Top N Employees by Salary
def top_employees_by_department(employees_df, n=3):
    window = Window.partitionBy("department").orderBy(col("salary").desc())
    ranked = employees_df.withColumn("rank", row_number().over(window))
    return ranked.filter(col("rank") <= n).drop("rank")


# Solution 9: Sales Summary
def employee_sales_summary(employees_df, sales_df):
    joined = employees_df.join(
        sales_df,
        employees_df.id == sales_df.employee_id,
        "left"
    )
    return joined.groupBy("name").agg(
        sum("amount").alias("total_sales"),
        count("amount").alias("sale_count"),
        avg("amount").alias("avg_sale")
    )


# Solution 10: Complex Join
def complete_sales_info(employees_df, sales_df, products_df):
    # Note: This assumes sales_df has product_id column
    # If not, you'll need to adjust based on your schema
    result = sales_df \
        .join(employees_df, sales_df.employee_id == employees_df.id) \
        .join(products_df, sales_df.product_id == products_df.id)
    
    return result.select(
        employees_df.name.alias("employee_name"),
        products_df.name.alias("product_name"),
        sales_df.amount.alias("sale_amount")
    )


# Test solutions
if __name__ == "__main__":
    from sample_data import employees_df, sales_df, products_df
    
    print("Testing Solutions:")
    
    print("\n1. Join Employees and Sales:")
    join_employees_sales(employees_df, sales_df).show()
    
    print("\n2. Left Join:")
    left_join_employees_sales(employees_df, sales_df).show()
    
    print("\n3. Salary by Department:")
    salary_by_department(employees_df).show()
    
    print("\n4. Department Stats:")
    department_stats(employees_df).show()
    
    print("\n5. Sales by Department:")
    sales_by_department(employees_df, sales_df).show()
    
    print("\n6. Count by Department:")
    count_by_department(employees_df).show()
    
    print("\n7. Average Age by Department:")
    avg_age_by_department(employees_df).show()
    
    print("\n8. Top 3 Employees by Department:")
    top_employees_by_department(employees_df, 3).show()
    
    print("\n9. Employee Sales Summary:")
    employee_sales_summary(employees_df, sales_df).show()
    
    print("\n🎉 All solutions executed!")

