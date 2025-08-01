import gradio as gr
import os
from dotenv import load_dotenv
from Chatbot_OOP import ChatBot  # reusing the same class here

load_dotenv()
MY_API_KEY = os.getenv("OPENAI_API_KEY")  # Your private key from .env

# Session variables to keep track of message count and api_key
user_sessions = {}

def chat_interface(user_input, user_api_key, session_id, history):
    # Use user API key if provided, otherwise fall back to your key
    use_custom_key = bool(user_api_key and user_api_key.strip())
    key = user_api_key if use_custom_key else MY_API_KEY

    # Initialize chatbot for this session if not already
    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "bot": ChatBot(model="gpt-3.5-turbo", temperature=0.7, max_tokens=100, token_budget=1000),
            "count": 0,
            "key": key,
            "history": []
        }
        #user_sessions[session_id]["bot"].client = ChatBot().client = ChatBot(api_key=key).client

    session = user_sessions[session_id]

    # Enforce 3 message limit if using my own key
    if not use_custom_key and session["count"] >= 3:
        session["history"].append({
            "role": "user", "content": user_input
        })
        session["history"].append({
            "role": "assistant", "content": "❌ You've reached the 3-question limit. Please bring your own API key to continue."
        })
        
    else:
        # Run the chat
        session["bot"].client = ChatBot(api_key=key).client
        reply = session["bot"].ask(user_input)

        session["count"] += 1
        session["history"].append({"role": "user", "content": user_input})
        session["history"].append({"role": "assistant", "content": reply})

    return session["history"], session["history"], ""


# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 💬 Gen Z ChatBot (Free version or Bring Your Own Key)")
    gr.Markdown("Use your OpenAI key for unlimited access, or continue for free with a 3-question limit.")
    
    with gr.Row():
        user_input = gr.Textbox(label="Your Message")
        user_api_key = gr.Textbox(label="Your OpenAI API Key (optional)", type="password", placeholder="sk-...")

    session_id = gr.Textbox(value="", visible=False)  # Internal session tracker
    chat_history = gr.Chatbot(label="Conversation", type = "messages")

    def generate_session_id():
        import uuid
        return str(uuid.uuid4())

    demo.load(fn=generate_session_id, outputs=session_id)
    user_input.submit(fn=chat_interface, inputs=[user_input, user_api_key, session_id, chat_history], outputs=[chat_history, chat_history, user_input])

demo.launch(share=True)

