import sqlite3
from llama_sql_generator import generate_sql_with_llama, clean_sql

# Step 1: Define your natural language question
question = "What is my total sales?"

# Step 2: Generate SQL query using LLaMA 3
try:
    sql_query = generate_sql_with_llama(question)
except Exception as e:
    print(f"\n Error generating SQL from LLaMA:\n{e}")
    exit()

print("\n Generated SQL Query:\n")
print(sql_query)

# Step 3: Clean the SQL query (removes markdown/code formatting)
sql_query = clean_sql(sql_query)

# Step 4: Safety Check: Only allow SELECT queries
if not sql_query.strip().lower().startswith("select"):
    print("\n ❌ Only SELECT queries are allowed.")
    exit()

# Step 5: Connect to SQLite database
try:
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
except Exception as e:
    print(f"\n Error connecting to the database:\n{e}")
    exit()

# Step 6: Execute the SQL query
try:
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print("\n Query Result:\n")
    print(result)
except Exception as e:
    print(f"\n Error executing SQL query:\n{e}")

# Step 7: Close database connection
conn.close()