import streamlit as st
from dotenv import load_dotenv
from Chatbot_OOP import ChatBot
import os
import uuid

# Load environment variables
load_dotenv()
MY_API_KEY = os.getenv("OPENAI_API_KEY")

# Session management
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

if "history" not in st.session_state:
    st.session_state["history"] = []

if "count" not in st.session_state:
    st.session_state["count"] = 0

if "bot" not in st.session_state:
    st.session_state["bot"] = ChatBot(
        model="gpt-3.5-turbo", temperature=0.7, max_tokens=100, token_budget=1000
    )

st.title("💬 Gen Z ChatBot (Free or Bring Your Own Key)")
st.caption("Use your OpenAI key for unlimited access or continue free with 3 messages.")

# Store user input in session state so we can reset it
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""
    
user_api_key = st.text_input("Your OpenAI API Key (optional)", type="password")
user_input = st.text_input("Ask me anything...")

if st.button("Send") and user_input:
    use_custom_key = bool(user_api_key.strip())
    key = user_api_key if use_custom_key else MY_API_KEY
    user_input = st.session_state["user_input"]

    if not use_custom_key and st.session_state["count"] >= 3:
        st.session_state["history"].append(("You", user_input))
        st.session_state["history"].append(
            ("Bot", "❌ You've reached the 3-question limit. Add your API key to continue.")
        )
    else:
        st.session_state["bot"].client = ChatBot(api_key=key).client
        reply = st.session_state["bot"].ask(user_input)
        st.session_state["count"] += 1
        st.session_state["history"].append(("You", user_input))
        st.session_state["history"].append(("Bot", reply))
        
    # Clear the input field after sending
    st.session_state["user_input"] = ""

# Show chat history
for sender, message in st.session_state["history"]:
    with st.chat_message(sender):
        st.markdown(message)
