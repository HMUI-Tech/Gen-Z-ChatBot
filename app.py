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
    
# bind the input field directly into session state:
st.text_input("Your OpenAI API Key (optional)", type="password", key="user_api_key")
st.text_input("Ask me anything…", key="user_input")

if st.button("Send") and st.session_state.user_input:
    use_custom = bool(st.session_state.user_api_key.strip())
    key = st.session_state.user_api_key if use_custom else MY_API_KEY

    # enforce 3-message free limit
    if not use_custom and st.session_state.count >= 3:
        st.session_state.history.append(("You", st.session_state.user_input))
        st.session_state.history.append(
            ("Bot", "❌ You've reached the 3-question limit. Add your API key to continue.")
        )
    else:
        st.session_state.bot.client = ChatBot(api_key=key).client
        reply = st.session_state.bot.ask(st.session_state.user_input)
        st.session_state.count += 1
        st.session_state.history.extend([
            ("You", st.session_state.user_input),
            ("Bot", reply),
        ])

    # clear the input field
    st.session_state.user_input = ""

# Show chat history
for sender, message in st.session_state["history"]:
    with st.chat_message(sender):
        st.markdown(message)
