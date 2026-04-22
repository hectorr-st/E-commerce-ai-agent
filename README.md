# E-commerce AI Agent with LLaMA 3 + FastAPI

An intelligent AI-powered backend that translates natural language questions into SQL queries and retrieves actionable insights from e-commerce datasets. Built with a locally hosted LLaMA 3 model (via Ollama), FastAPI, and SQLite, this project demonstrates how LLMs can be integrated into real-world data systems for analytics and decision support.

---

## 🚀 Features

- **Natural Language → SQL**  
  Converts plain English queries into executable SQL using a local LLaMA 3 model.

- **FastAPI Backend**  
  Provides RESTful endpoints (`/ask`, `/stream`) for real-time interaction.

- **Streaming Responses**  
  Supports token streaming for a live typing / chat-like experience.

- **SQLite Database**  
  Lightweight, file-based database for storing e-commerce metrics.

- **Modular Architecture**  
  Clean separation between:
  - LLM-based SQL generation  
  - SQL execution layer  
  - API interface  

- **CLI-Friendly Testing**  
  Easily test with `curl` + `jq` for formatted terminal output.

---

## 📁 Project Structure

E-commerce-ai-agent/
├── .venv/ # Python virtual environment
├── .gitignore # Git ignore configuration
├── README.md # Project documentation
├── resume.md # Project summary (this file)
├── Product-Level *.xlsx # Raw e-commerce datasets
├── load_data_to_db.py # Loads Excel data into SQLite
├── ecommerce.db # Generated SQLite database
├── llama_sql_generator.py # LLM-based SQL query generator
├── llama_sql_executor.py # SQL execution module (optional)
├── api_server.py # FastAPI app with endpoints
├── test_database_queries.py # Manual SQL testing script


---

## ⚙️ Setup Instructions

### 1. Clone Repository
```
git clone https://github.com/hectorr-st/E-commerce-ai-agent.git
cd E-commerce-ai-agent
```

###2. Create Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate
```
###3. Install Dependencies
```
pip install -r requirements.txt
```
If requirements.txt is missing:
```
pip install fastapi uvicorn requests pandas openpyxl
```
###4. Start LLaMA 3 via Ollama
```
ollama run llama3
```
###5. Load Dataset into SQLite
```
python load_data_to_db.py
```
###6. Run FastAPI Server
```
uvicorn api_server:app --reload
```

---

### 🔹 Project Highlights
- Built an AI-powered system that converts natural language into SQL for e-commerce analytics  
- Enabled fully local LLM inference using LLaMA 3 via Ollama (no external API dependency)  
- Designed a scalable, modular backend using FastAPI  
- Implemented real-time streaming responses for interactive user experience  
- Applicable to dashboards, internal BI tools, and AI copilots  

---

### 🔹 Key Functionalities
- Total sales revenue calculation  
- Return on Ad Spend (RoAS) analysis  
- CPC (Cost Per Click) comparison across products  
- Monthly ad spend trend analysis  
- CTR (Click-Through Rate) aggregation  
- Top-performing products by sales  
- Click distribution per product  
- Identification of low-performing products (RoAS)  
- Total impressions tracking  
- Revenue-based product ranking  

---

### 🔹 Tech Stack
- **LLM:** LLaMA 3 (via Ollama)  
- **Backend:** FastAPI  
- **Database:** SQLite3  
- **Data Processing:** Pandas, OpenPyXL  
- **API Testing:** cURL, Swagger UI  
- **CLI Tools:** jq  

---

### 👤 Author
**Suzuki Taro**  
📧 dr.smart710@gmail.com
