# 🤖 Customer Support AI Agent (LangGraph + LangChain + Groq)

An AI-powered Customer Support Agent that classifies, routes, and responds to customer queries using LangGraph for workflow orchestration, LangChain for LLM handling, and Groq as a free LLM provider (no OpenAI billing required).

⭐ **Features**

---

🔍 **Query Classification**
- Technical
- Billing
- General

😀 **Sentiment Analysis**
- Positive / Neutral / Negative

🔁 **Intelligent Routing**
- Technical handler
- Billing handler
- General handler
- Negative sentiment → Escalation to human

⚡ Runs smoothly in Google Colab

💸 **Zero cost using Groq API**

---

## 🛠️ Tech Stack
| Component      | Library        |
|---------------|---------------|
| Orchestration | LangGraph      |
| LLM Framework | LangChain      |
| LLM Provider  | Groq           |
| Runtime       | Google Colab / Jupyter Notebook |

---

## 🚀 Quick Start (Google Colab)

1️⃣ **Install Dependencies**
```python
!pip install langchain langgraph python-dotenv langchain-groq
```

2️⃣ **Get a Free Groq API Key**

Create your free key here:

https://console.groq.com/keys

3️⃣ **Set API Key in Colab**
```python
import os
os.environ["GROQ_API_KEY"] = "gsk_xxxxxxxxxxxxxxxxx"
```

4️⃣ **Use Groq Model**

Make sure you use an active Groq model like:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
```

Replace any ChatOpenAI usage with ChatGroq.

---

### ▶️ Run Example
```python
query = "My internet connection keeps dropping. Can you help?"
result = run_customer_support(query)

print("Category:", result["category"])
print("Sentiment:", result["sentiment"])
print("Response:", result["response"])
```

---

## 🧠 How It Works

1️⃣ Categorizes the query  
2️⃣ Analyzes sentiment  
3️⃣ Routes based on logic:
- If sentiment = Negative → escalate
- If category = Technical → technical handler
- If category = Billing → billing handler
- Else → general handler

---

## ⚠️ Common Issues & Fixes

**❌ Model Decommissioned**
- Use:
  - llama-3.1-8b-instant

**❌ Billing / Quota Error**
- You are accidentally using OpenAI — switch to Groq.

---

🙌 **Credits**

Base tutorial inspiration by Nir Diamant  
Updated and optimized for Groq + Colab

---

📜 **License**

Open-source — feel free to modify and improve.

---

💬 **Support**

If something breaks, open an issue or reach out.
