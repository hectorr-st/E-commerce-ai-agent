from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import sqlite3
import requests
import json

# 🔄 Import your custom LLaMA SQL logic
from llama_sql_generator import generate_sql_with_llama, clean_sql, get_all_table_columns

app = FastAPI()

# 🎯 Request model
class QuestionRequest(BaseModel):
    question: str

# ✅ /ask endpoint — for SQL generation + execution
@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        # 1. Generate SQL from question
        raw_sql = generate_sql_with_llama(request.question)
        sql_query = clean_sql(raw_sql)

        # 2. Allow only SELECT or WITH queries
        if not sql_query.strip().lower().startswith(("select", "with")):
            raise ValueError("Only SELECT queries are allowed.")

        # 3. Connect to SQLite DB
        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()

        # 4. Run SQL
        cursor.execute(sql_query)
        rows = cursor.fetchall()

        # 5. Format results
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]

        return {
            "question": request.question,
            "sql_query": sql_query,
            "result": result
        }

    except Exception as e:
        return {
            "error": f"{type(e).__name__}: {str(e)}",
            "generated_sql": locals().get("sql_query", "N/A")
        }

    finally:
        try:
            conn.close()
        except:
            pass

# ✅ Streaming helper (token-by-token from Ollama)
def stream_llama_response(prompt: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": True
    }
    response = requests.post(url, json=payload, stream=True)

    def event_stream():
        for line in response.iter_lines():
            if line:
                try:
                    json_data = json.loads(line.decode("utf-8"))
                    token = json_data.get("response", "")
                    yield token
                except:
                    continue

    return event_stream()

# ✅ /stream endpoint — for typing-style natural language answer
@app.post("/stream")
def stream_question(request: QuestionRequest):
    try:
        # Add table schema to help LLaMA
        schema = get_all_table_columns()

        prompt = f"""You are a helpful assistant. Answer the user's question clearly.

Database Schema:
{schema}

Question: {request.question}
Answer:"""

        return StreamingResponse(
            stream_llama_response(prompt),
            media_type="text/plain"
        )

    except Exception as e:
        return {"error": str(e)}