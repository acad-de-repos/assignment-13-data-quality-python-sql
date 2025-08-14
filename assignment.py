import pandas as pd
from sqlalchemy import text

def perform_mixed_data_quality_checks(db_connection):
  """
  Performs data quality checks using a mix of SQL and Pandas.

  Args:
    db_connection: An active database connection object.

  Returns:
    A dictionary summarizing the data quality issues found.
  """
  dq_report = {}

  # Task 1 (SQL): Check for null values in product_name
  # Hint: Use COUNT(*) with a WHERE clause to count null values
  # Your code here

  # Task 2 (SQL): Check for duplicate product_id values
  # Hint: Use GROUP BY and HAVING COUNT(*) > 1 to find duplicates
  # Your code here

  # Load products table into Pandas DataFrame for Python checks
  products_df = pd.read_sql_table('products', db_connection)

  # Task 3 (Python/Pandas): Check if price column is numeric
  # Hint: Use pd.to_numeric(errors='coerce') to identify non-numeric values
  # Your code here

  # Task 4 (Python/Pandas): Check for invalid category values
  # Hint: Use df['category'].isin(accepted_categories) to check valid categories
  # Your code here

  return dq_report 