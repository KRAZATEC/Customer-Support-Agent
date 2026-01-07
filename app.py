import streamlit as st
from agent import build_agent

st.set_page_config(page_title="Customer Support Agent", page_icon="🤖")

# -------- Sidebar --------
st.sidebar.title("🔐 API Configuration")

groq_api_key = st.sidebar.text_input(
    "Groq API Key (starts with gsk_)",
    type="password"
)

st.sidebar.caption(
    "[Get a free key here](https://console.groq.com/keys)"
)

st.title("🤖 Intelligent Customer Support Agent")

# Stop app if no key
if not groq_api_key:
    st.info("Please enter your Groq API key in the sidebar to start.")
    st.stop()

# Build agent ONCE per session
if "agent" not in st.session_state:
    st.session_state.agent = build_agent(groq_api_key)

if "history" not in st.session_state:
    st.session_state.history = []

# -------- Chat UI --------
for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.markdown(msg)

user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        result = st.session_state.agent.invoke(
            {"user_input": user_input}
        )
        response = result["response"]

    st.session_state.history.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)
