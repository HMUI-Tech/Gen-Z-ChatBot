# 💬 Gen Z ChatBot (Streamlit + OpenAI && Gradio + OpenAI)

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

👉 [7 days access with Gradio] (https://1840936aca7e792779.gradio.live)

---

## 👯‍♀️ Fork & Collaborate
Feel free to fork this project and customize it for your own experiments or projects!

If you're interested in contributing, improving the sass engine, or integrating new models, i'm open to collaborations and feedback.

📩 Contact me directly via GitHub Issues or drop me a message if you'd like to team up!

---

## 🔐 Environment Variables

This app uses environment variables to keep your API keys safe.

Make sure to define them either via a .env file in the root directory: OPENAI_API_KEY= "your-secret-key-here"

Or via Streamlit's Advanced Settings → Secrets: OPENAI_API_KEY = "your-secret-key-here"

---

## 📦 Requirements

- gradio
- openai
- python-dotenv
- tiktoken

---

## 💡 Future Ideas

🧩 Plugin support

🌐 Multilingual version (Currently, just a sassy english speaking Gen Z)

💬 Memory persistence beyond session

🧑‍🎤 More personalities to choose from

🧑‍🎤 Deployable on Huggingface

---

## ✨ License
MIT License — Use it freely, respectfully, and give credit where it's due.

Made with ❤️ by [Hilary Martins-Udeze] just for fun

---

### 💻 Local (localhost)
```bash
git clone https://github.com/yourusername/Gen-Z_ChatBot.git
cd Gen-Z_ChatBot
pip install -r requirements.txt
python app.py (for Gradio Vaersion)
python Web_Chatbot.py (for streamlit version)



