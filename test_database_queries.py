import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect('ecommerce.db')

# Example Query 1: View first 5 rows from eligibility_table
query1 = "SELECT * FROM eligibility_table LIMIT 5;"
df1 = pd.read_sql_query(query1, conn)
print("\n--- eligibility_table sample data ---")
print(df1)

# Example Query 2: Count total rows in total_sales_metrics table
query2 = "SELECT COUNT(*) as total_rows FROM total_sales_metrics;"
df2 = pd.read_sql_query(query2, conn)
print("\n--- total_sales_metrics row count ---")
print(df2)

# Example Query 3: View first 5 rows from ad_sales_metrics
query3 = "SELECT * FROM ad_sales_metrics LIMIT 5;"
df3 = pd.read_sql_query(query3, conn)
print("\n--- ad_sales_metrics sample data ---")
print(df3)

# Close connection
conn.close()