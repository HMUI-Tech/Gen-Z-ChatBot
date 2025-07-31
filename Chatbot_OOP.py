import os
from openai import OpenAI
import tiktoken
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file into environment (specifically for OPENAI_API_KEY)


# Define the ChatBot class using Object-Oriented Programming
class ChatBot:
    def __init__(self, model="gpt-3.5-turbo", temperature=0.7, max_tokens=100, token_budget=1000, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")  # Load API key from environment
        self.client = OpenAI(api_key=self.api_key)  # Initialize OpenAI client
        self.model = model  # Set the model to use (default: GPT-4.1 Nano)
        self.temperature = temperature # Set response creativity (0 = deterministic, 1 = very creative)
        self.max_tokens = max_tokens # Max tokens per response
        self.token_budget = token_budget # Max total tokens allowed in conversation
        self.system_prompt = ("You're a witty, sarcastic Gen Z chatbot who is tired of answering questions, but are forced to answer nevertheless, who uses slang, Gen Z expressions, and emojis 🧃😎🔥. "
                        "You can fluently understand and respond in English, Italian, and German depending on the language of the user. "
                        "Always respond in the language the user uses. Keep your sass and emojis consistent in every language."
                        )  # Define personality
        self.messages = [{"role": "system", "content": self.system_prompt}] # Initialize message history with system prompt
        self.encoding = self._get_encoding() # Load encoding method for token counting

# Internal method to get tokenizer encoding for the given model
    def _get_encoding(self):
        try:
            return tiktoken.encoding_for_model(self.model)  # Fallback to default tokenizer if model-specific is unavailable
        except:
             # Fallback to default tokenizer if model-specific is unavailable
            print(f"⚠️ Warning: Token for model '{self.model}' not found. Using default encoding.")
            return tiktoken.get_encoding("cl100k_base")

 # Calculate total number of tokens in the current chat history
    def _total_tokens_used(self):
        return sum(len(self.encoding.encode(msg["content"])) for msg in self.messages)

    # Enforce token limit by trimming old messages if token budget is exceeded    
    def _enforce_token_budget(self):
        while self._total_tokens_used() > self.token_budget:
            if len(self.messages) <= 2:
                break
            self.messages.pop(1)

    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        self._enforce_token_budget()
        return reply

    def chat_loop(self):
        print("Type 'exit' or 'quit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() in {"exit", "quit"}:
                break
            reply = self.ask(user_input)
            print("Assistant:", reply)
            print("Current tokens:", self._total_tokens_used())

if __name__ == "__main__":
    bot = ChatBot()
    bot.chat_loop()