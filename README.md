# Implementing Data Quality Checks with Python and SQL Assignment

## Problem Description

In this assignment, you will implement data quality checks using a combination of Python (Pandas) and SQL. You will extract data from a database, perform various data quality checks using both SQL queries and Pandas functions, and report on the findings. This assignment emphasizes the practical application of data quality principles in a mixed technology environment.

## Learning Objectives

By completing this assignment, you will learn:
- How to use SQL to perform data quality checks (e.g., count nulls, check uniqueness)
- How to use Pandas to perform data quality checks (e.g., validate data types, check for outliers)
- How to integrate SQL and Python for comprehensive data quality assessment
- How to report on data quality issues found

## Setup Instructions

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have the following packages installed:
    -   pandas (>=1.3.0)
    -   sqlalchemy (>=1.4.0)

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `perform_mixed_data_quality_checks(db_connection)`.
3.  The function takes a database connection object as input.
4.  Your tasks are to:
    *   **Task 1 (SQL)**: Check for null values in the `product_name` column in the `products` table using a SQL query.
    *   **Task 2 (SQL)**: Check for duplicate `product_id` values in the `products` table using a SQL query.
    *   **Task 3 (Python/Pandas)**: Load the `products` table into a Pandas DataFrame and check if the `price` column is numeric. Report any non-numeric values.
    *   **Task 4 (Python/Pandas)**: Check if all `category` values in the DataFrame are from a predefined list ('Electronics', 'Books', 'Home Goods'). Report any invalid categories.
5.  The function should return a dictionary summarizing the results of all data quality checks.

## Hints

*   For SQL tasks, use `pd.read_sql_query()` to execute the query and get the result.
*   For Task 1 (SQL), use `COUNT(*) WHERE column IS NULL`.
*   For Task 2 (SQL), use `GROUP BY` and `HAVING COUNT(*) > 1`.
*   For Task 3 (Python/Pandas), iterate through the `price` column and use `pd.to_numeric(errors='coerce')` to identify non-numeric entries.
*   For Task 4 (Python/Pandas), use `df['category'].isin(accepted_categories)` to identify valid categories.

## Testing Your Solution

Run the test file to verify your implementation:

```bash
python test.py
```

The tests will check:

-   That the function returns a dictionary with the correct keys
-   That each data quality check correctly identifies issues in the test data

## Expected Output

The function should return a dictionary with the following keys and values:

-   `null_product_name_count`: Number of null `product_name` values.
-   `duplicate_product_id_count`: Number of duplicate `product_id` values.
-   `non_numeric_prices`: List of non-numeric price values.
-   `invalid_categories`: List of invalid category values.

## Sample Data Format

The database will contain a `products` table with the following columns:

-   `product_id` (INTEGER)
-   `product_name` (TEXT)
-   `price` (TEXT)
-   `category` (TEXT)

## Troubleshooting

### Common Errors

-   `DatabaseError`: Check your SQL syntax.
-   `ValueError`: Ensure correct data type conversions in Pandas.

## Further Exploration (Optional)

*   How would you implement a data quality dashboard to visualize these results?
*   Explore more advanced data quality dimensions like timeliness and conformity.
*   Can you write a function to automatically cleanse some of these issues (e.g., remove rows with null product names)?

## Resources

-   [Data Quality Management](https://www.ibm.com/cloud/learn/data-quality-management)
-   [SQL Data Quality Checks](https://www.sqlshack.com/implementing-data-quality-checks-in-sql-server/)
-   [Pandas Data Quality Checks](https://towardsdatascience.com/data-quality-checks-with-pandas-2020-a-practical-guide-2c3d2e7e7e7e)
