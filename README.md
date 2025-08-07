# E-commerce AI Agent with LLaMA 3 + FastAPI

This project is an intelligent AI agent that understands natural language questions related to e-commerce metrics and returns accurate answers by generating and executing SQL queries on a local database. It uses a locally hosted LLaMA 3 model via Ollama, integrates with FastAPI, and supports streamed responses for a live typing effect.

---

## 🚀 Features

	•	Natural Language to SQL: Converts plain English questions into valid SQL queries using a local LLaMA 3 model via Ollama.
	•	FastAPI Backend: Serves endpoints to receive questions and return results in real time.
	•	SQLite3 Database: Lightweight and efficient storage for e-commerce metrics.
	•	Live Typing Effect: Streaming responses simulate human typing for natural interaction.
	•	cURL + JQ Demo Support: Easily test endpoints from terminal with clean JSON formatting.
	•	Modular Design: Clean separation of concerns between LLM generation, SQL execution, and API serving.

---
### 🔹 Project Structure

```
E-commerce_ai_agent/
├── .venv/                     # Python virtual environment
├── .gitignore               # Git ignore config
├── README.md               # Project documentation
├── Product-Level *.xlsx     # Source Excel datasets
├── load_data_to_db.py      # Script to load Excel files into SQLite
├── ecommerce.db            # Generated SQLite database
├── llama_sql_generator.py  # Converts questions into SQL using LLaMA 3
├── llama_sql_executor.py   # (Optional) For modular SQL execution
├── api_server.py           # FastAPI backend with /ask and /stream endpoints
├── test_database_queries.py # (Optional) Manual SQL query tester
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/gokularaman-c/E-commerce-ai-agent.git
cd E-commerce-ai-agent
```

2. Create and Activate Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```

✅ If requirements.txt is not present, manually install:

```
pip install fastapi uvicorn requests sqlite3
```

4. Start Ollama (if not running)

```
ollama run llama3
```

5. Load Data into SQLite

```
python load_data_to_db.py
```

6. Start FastAPI Server

```
uvicorn api_server:app --reload
```
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
	•	Show top 3 products with highest total sales.

---

🛠 Tech Stack

| Component     | Technology               |
|---------------|--------------------------|
| LLM           | LLaMA 3 via Ollama       |
| Backend       | FastAPI                  |
| Database      | SQLite3                  |
| API Testing   | cURL, Swagger UI         |
| JSON Parsing  | jq (for terminal output) |
| Dataset Format| Excel (.xlsx → SQLite)   |

---

👨‍💻 Author

**Gokularaman C**  
---