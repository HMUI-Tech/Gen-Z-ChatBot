import streamlit as st
import uuid
from dotenv import load_dotenv
from Chatbot_OOP import ChatBot
import os

load_dotenv()
MY_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize once
if "history" not in st.session_state:
    st.session_state.history = []
if "count" not in st.session_state:
    st.session_state.count = 0
if "bot" not in st.session_state:
    st.session_state.bot = ChatBot(
        model="gpt-3.5-turbo", temperature=0.7, max_tokens=100, token_budget=1000
    )

st.title("💬 Gen Z ChatBot")
st.caption("3 free messages or unlimited with your own key")

# Define your “Send” logic as a callback
def send_message():
    prompt = st.session_state.user_input  # grab the latest text_input
    use_custom = bool(st.session_state.user_api_key.strip())
    key = st.session_state.user_api_key if use_custom else MY_API_KEY

    if not use_custom and st.session_state.count >= 3:
        st.session_state.history.append(("You", prompt))
        st.session_state.history.append(
            ("Bot", "❌ You've reached the 3-question limit. Add your API key to continue.")
        )
    else:
        # swap in the user’s key if provided
        st.session_state.bot.client = ChatBot(api_key=key).client
        reply = st.session_state.bot.ask(prompt)
        st.session_state.count += 1
        st.session_state.history.extend([
            ("You", prompt),
            ("Bot", reply),
        ])

    # **This is now safe** because it’s inside the callback
    st.session_state.user_input = ""  

# Place your inputs
st.text_input("Your OpenAI API Key (optional)", type="password", key="user_api_key")
st.text_input("Ask me anything…", key="user_input")

# Wire up the callback
st.button("Send", on_click=send_message)

# Finally render the chat
for sender, msg in st.session_state.history:
    with st.chat_message(sender):
        st.markdown(msg)
