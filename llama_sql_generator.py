import sqlite3
import requests

# ✅ Dynamically get table schemas from SQLite
def get_all_table_columns(db_path="ecommerce.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    tables = ['eligibility_table', 'total_sales_metrics', 'ad_sales_metrics']
    schema = []

    for table in tables:
        try:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            if not columns:
                schema.append(f"{table}: ⚠️ No columns found")
                continue
            formatted_columns = "\n   - ".join([f"{col[1]} ({col[2]})" for col in columns])
            schema.append(f"{table}:\n   - {formatted_columns}")
        except Exception as e:
            schema.append(f"{table}: ⚠️ Error: {str(e)}")
    
    conn.close()
    return "\n\n".join(schema)

# ✅ Strip markdown formatting from LLM responses
def clean_sql(sql_query: str) -> str:
    if "```sql" in sql_query:
        return sql_query.split("```sql")[1].split("```")[0].strip()
    elif "```" in sql_query:
        return sql_query.split("```")[1].split("```")[0].strip()
    return sql_query.strip()

# ✅ Generates SQL from natural language using LLaMA 3 and SQLite-safe rules
def generate_sql_with_llama(question: str, db_path="ecommerce.db") -> str:
    # 1. Load current schema
    table_schema = get_all_table_columns(db_path)

    # 2. Build prompt with strict instructions
    prompt = f"""
You are an expert SQL assistant. Convert the following natural language question into a valid SQLite SQL query.

Database Schema:
{table_schema}

Instructions:
- Use only the columns listed above. DO NOT invent any new columns.
- For RoAS use: SUM(ads.ad_sales) / SUM(ads.ad_spend).
- For CPC use: ads.ad_spend / ads.clicks. (Filter for ads.clicks > 0)
- For CTR use: ads.clicks / ads.impressions. (Filter for ads.impressions > 0)
- Use strftime('%Y-%m', date) to group by month.
- Do NOT use unsupported functions like DATE_TRUNC or TO_CHAR.
- Use aliases:
    - e = eligibility_table
    - ts = total_sales_metrics
    - ads = ad_sales_metrics
- ALWAYS use these aliases when referencing columns (e.g., ads.date not just date).
- Avoid nested aggregates like AVG(SUM(...)).
- Use HAVING instead of WHERE when filtering aggregated values.
- Group by all non-aggregated columns.
- Add ORDER BY and LIMIT when appropriate.
- Only return a single valid SQLite SELECT statement.

Question: {question}

SQL:
"""

    # 3. Call LLaMA 3 locally via Ollama
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()

        # Clean markdown and return raw SQL
        return clean_sql(result.get("response", ""))

    except Exception as e:
        return f"-- ❌ Error generating SQL from LLaMA: {e}"