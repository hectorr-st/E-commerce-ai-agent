import pandas as pd
import sqlite3

# STEP 1: Load Excel files
eligibility_df = pd.read_excel('Product-Level Eligibility Table (mapped).xlsx')
total_sales_df = pd.read_excel('Product-Level Total Sales and Metrics (mapped).xlsx')
ad_sales_df = pd.read_excel('Product-Level Ad Sales and Metrics (mapped).xlsx')

# STEP 2: Create SQLite database
conn = sqlite3.connect('ecommerce.db')

# STEP 3: Save dataframes as SQL tables
eligibility_df.to_sql('eligibility_table', conn, if_exists='replace', index=False)
total_sales_df.to_sql('total_sales_metrics', conn, if_exists='replace', index=False)
ad_sales_df.to_sql('ad_sales_metrics', conn, if_exists='replace', index=False)

# STEP 4: Confirm table creation
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables created in the database:", cursor.fetchall())

# STEP 5: Close connection
conn.close()