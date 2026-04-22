# 🧠 AI-Powered E-commerce Query Engine

A backend system that enables users to interact with e-commerce data using natural language instead of writing SQL. This project bridges the gap between non-technical queries and structured databases by leveraging a locally deployed large language model.

---

## ✨ Overview

This application acts as an intelligent query layer on top of an e-commerce dataset. Users can ask business questions in plain English, and the system interprets the intent, generates optimized SQL queries, executes them, and returns structured results in real time.

The entire pipeline runs locally, ensuring data privacy and eliminating dependency on external APIs.

---

## ⚡ What Makes This Interesting

- Replaces traditional dashboards with a conversational interface  
- Demonstrates practical use of LLMs in backend systems  
- Eliminates the need for manual SQL writing  
- Designed for fast iteration and extensibility  

---

## 🧩 System Workflow

1. User submits a natural language query  
2. LLM interprets intent and generates SQL  
3. Query is validated and executed on SQLite  
4. Results are formatted and returned via API  
5. (Optional) Response is streamed token-by-token  

---

## 🔧 Core Components

| Layer            | Description |
|------------------|-------------|
| Language Model   | Local LLaMA 3 model via Ollama for SQL generation |
| API Layer        | FastAPI service handling requests and responses |
| Data Layer       | SQLite database populated from Excel datasets |
| Processing Layer | Python scripts for transformation and execution |

---

## 📂 Repository Layout

```
E-commerce-ai-agent/
├── api_server.py            # API entry point
├── llama_sql_generator.py  # Converts text → SQL
├── llama_sql_executor.py   # Handles SQL execution
├── load_data_to_db.py      # Data ingestion script
├── ecommerce.db            # Local database
├── Product-Level *.xlsx    # Source data files
├── test_database_queries.py# Debug/testing utilities
├── README.md               # Documentation
├── resume.md               # Project summary
```

## 🧪 Example Use Cases

- Business performance analysis without traditional BI tools  
- Rapid ad-hoc querying of sales and marketing data  
- Internal analytics assistant for non-technical teams  
- Prototype for AI-powered data copilots  

---

## 🛠 Implementation Notes

- SQL generation handled by a local LLM  
- No cloud dependencies or external API costs  
- Modular Python design for easy extension and maintenance  
- Streaming responses improve interactivity and user experience  

---

## 🚀 Getting Started

```
git clone https://github.com/hectorr-st/E-commerce-ai-agent.git
cd E-commerce-ai-agent

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

ollama run llama3

python load_data_to_db.py

uvicorn api_server:app --reload
```
