# 🤖 Intelligent Customer Support Agent

A Streamlit-based customer support chatbot powered by **Groq LLM** and **LangGraph** for intelligent workflow orchestration.

## Features

- **Real-time Chat Interface**: Interactive conversation with sentiment analysis
- **LLM-Powered Responses**: Uses Groq's fast inference engine (Llama 3.1 8B model)
- **Sentiment Analysis**: Automatic sentiment detection for context-aware responses
- **Session Management**: Conversation history maintained throughout the session
- **Professional Support**: Tailored responses based on user sentiment

## Tech Stack

- **Streamlit**: Interactive web UI
- **LangChain**: LLM framework and utilities
- **LangGraph**: Workflow orchestration for multi-step agent logic
- **Groq**: Fast LLM inference API

## Prerequisites

- Python 3.11+
- Groq API key (free tier available at [console.groq.com](https://console.groq.com/keys))

## Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd CustomerSupportAgent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Get a free Groq API key from [console.groq.com/keys](https://console.groq.com/keys)
   - Keep it ready for the app (enters via Streamlit sidebar)

## Running the Application

```bash
streamlit run app.py
```

The app will launch at `http://localhost:8501`

### First Run
1. Paste your Groq API key in the sidebar input field
2. Start chatting with the support agent

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── agent.py            # LangGraph agent logic & sentiment analysis
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## How It Works

### Agent Workflow

The agent follows a two-stage pipeline:

1. **Sentiment Analysis Node**: Analyzes the user's message to detect sentiment (positive, neutral, or negative)
2. **Response Generation Node**: Uses the detected sentiment context to generate empathetic and appropriate support responses

```
User Input → Sentiment Analysis → Response Generation → Chat Output
```

## Dependencies

- `streamlit` - Web UI framework
- `langchain-groq` - Groq integration for LangChain
- `langgraph` - Graph-based workflow orchestration
- `langchain-core` - Core LangChain utilities

## Configuration

### Models Used
- **LLM**: `llama-3.1-8b-instant` (via Groq)
  - Fast inference
  - Cost-effective
  - High-quality responses

### Customization
- Edit `agent.py` to modify sentiment analysis logic
- Update the system prompt in `generate_response()` for different support styles
- Adjust `app.py` for UI customization

## Troubleshooting

### "ModuleNotFoundError: No module named..."
```bash
pip install -r requirements.txt
```

### "Invalid API key"
- Ensure your key starts with `gsk_`
- Get a new key from [console.groq.com/keys](https://console.groq.com/keys)

### "Model not found"
- The model `llama-3.1-8b-instant` is default and widely available on Groq
- Check Groq documentation for current available models

## License

MIT License - Feel free to use and modify for your projects.

## Support

For issues or questions:
1. Check Groq API status: https://console.groq.com/docs
2. Review LangChain docs: https://python.langchain.com
3. Streamlit help: https://docs.streamlit.io

---

**Built with ❤️ using Streamlit, LangChain, and Groq**
