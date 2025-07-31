# 💬 Gen Z ChatBot (Streamlit + OpenAI)

This is a Gen Z-flavored chatbot powered by OpenAI's GPT models. It allows users to interact either for **free with a 3-message limit** or **unlimited if they bring their own API key**.

## 🔥 Features

- ✅ Free mode (3-message limit using a default OpenAI key)
- 🔐 Bring Your Own Key (Unlimited use with your own API key)
- 🎨 Built with `streamlit` UI
- 🔁 Session tracking using UUIDs
- 🧠 Personality & sass baked in
- 🌍 Deployable on streamlit or run locally

---

## 🚀 Try It Now

👉 [https://gen-z-chatbot.streamlit.app/](https://gen-z-chatbot.streamlit.app/)

👯‍♀️ Fork & Collaborate
Feel free to fork this project and customize it for your own experiments or projects!

If you're interested in contributing, improving the sass engine, or integrating new models — I'm open to collaborations and feedback.

📩 Contact me directly via GitHub Issues or drop me a message if you'd like to team up!

🔐 Environment Variables
This app uses environment variables to keep your API keys safe.

Make sure to define them either via a .env file in the root directory:

env
Copy
Edit
OPENAI_API_KEY=your-secret-key-here
Or via TOML format in Streamlit's Advanced Settings → Secrets:

toml
Copy
Edit
OPENAI_API_KEY = "your-secret-key-here"
📦 Requirements
txt
Copy
Edit
gradio
openai
python-dotenv
tiktoken
💡 Future Ideas
🧩 Plugin support

🌐 Multilingual version

💬 Memory persistence beyond session

🧑‍🎤 More personalities to choose from

✨ License
MIT License — Use it freely, respectfully, and give credit where it's due.

Made with ❤️ by [Your Name or GitHub Handle]

yaml
Copy
Edit

---

Let me know if you'd like this updated for `Streamlit` instead of `Gradio` as the UI or want it auto

### 💻 Local (localhost)
```bash
git clone https://github.com/yourusername/Gen-Z_ChatBot.git
cd Gen-Z_ChatBot
pip install -r requirements.txt
python app.py



