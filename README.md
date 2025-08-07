# 🛒 E-commerce AI Agent with Local LLM (LLaMA 3)

This project is an intelligent AI agent that understands natural language questions related to e-commerce metrics and returns accurate answers by generating and executing SQL queries on a local database. It uses a locally hosted LLaMA 3 model via Ollama, integrates with FastAPI, and supports streamed responses for a live typing effect.

---

## 🚀 Features

- 🔗 Natural language to SQL query conversion using LLaMA 3
- 🧠 Local LLM hosting via [Ollama](https://ollama.com)
- 📊 Executes SQL on structured SQLite e-commerce datasets
- 💬 FastAPI backend with RESTful endpoints
- 📥 `POST /ask` for direct Q&A
- ✨ `POST /stream` for real-time typing effect
- 📁 Modular codebase: easy to understand and extend
- 🎯 Tested on real-world marketing and product datasets

---

## 📂 Project Structure

E-commerce_ai_agent/
│
├── api_server.py               # FastAPI endpoints (/ask and /stream)
├── llama_sql_generator.py      # LLM prompt + SQL generation logic
├── llama_sql_executor.py       # SQL execution & safety check logic
├── load_data_to_db.py          # Loads Excel files into SQLite DB
├── test_database_queries.py    # Simple test queries
├── *.xlsx                      # Raw datasets (mapped to SQL tables)
├── ecommerce.db                # SQLite database (auto-created)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

---

## 📦 Dependencies

Install the following before running the app:

```bash
pip install -r requirements.txt

Make sure you have Ollama installed and running with:

ollama run llama3


⸻

▶️ How to Run
	1.	Activate virtual environment (if not already):

source .venv/bin/activate

	2.	Start the FastAPI server:

uvicorn api_server:app --reload

	3.	Test queries using cURL:

curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is my total sales?"}' | jq

	4.	Try streaming (typing effect):

curl -N -X POST http://localhost:8000/stream \
  -H "accept: text/plain" \
  -H "Content-Type: application/json" \
  -d '{"question": "How do you calculate ROAS?"}'


⸻

🧠 Example Questions
	•	What is my total sales?
	•	Calculate the RoAS (Return on Ad Spend).
	•	Which product had the highest CPC?
	•	Show total ad spend per month.
	•	What is the average CTR by month?
	•	List top 5 products by ad sales.
	•	How many clicks did each product receive?
	•	Which product had the lowest RoAS?
	•	What is the total number of impressions?

⸻

🛠 Tech Stack

Component	Tech Used
LLM	LLaMA 3 via Ollama
Backend	FastAPI
Database	SQLite3
API Testing	cURL, Swagger
JSON Handling	jq (for formatted terminal output)
Dataset Format	Excel (XLSX → SQLite)

⸻

📌 Notes
	•	All SQL queries are auto-validated to prevent unsafe operations.
	•	All data is processed locally; no external LLM APIs are used.
	•	For visualization support, Matplotlib can be optionally added (not enabled in current build).

⸻

📚 Credits
	•	LLaMA 3 hosted via Ollama
	•	FastAPI team for clean REST API support
	•	SQLite3 for a minimal yet powerful DB engine

⸻

🧑‍💻 Author

Gokularaman C
⸻