import os
from openai import OpenAI
import tiktoken
from dotenv import load_dotenv

# Load API key
load_dotenv()

# To get the OpenAI API key from environment variables (good for security)
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
Model = "gpt-4.1-nano-2025-04-14"
Temp = 0.7 # Temperature controls how creative or random the response is (0 = predictable, 1 = very creative)
Max_Tokens = 100 # Limit the number of tokens the assistant is allowed to generate per response
Token_budget = 1000 # Set a maximum number of tokens to keep in memory (for budget control)

# Seting the assistant's personality to that of the GenV's
System_Prompt = "You are a fed up and sassy Gen Z assistant questions."
Messages = [{"role": "system", "content":System_Prompt}]

# This function returns the token encoder for a given model (used to count token usage)
def get_encoding(Model):
    try:
        return tiktoken.encoding_for_model(Model)
    except:
        print(f"Warning: Token for the model '{Model}' not found")
        return tiktoken.get_encoding("cl100k_base")
ENCODING = get_encoding(Model)

def enforce_token_budget(messages, budget=Token_budget):
    try:
        while total_tokens_used(messages) > budget:
            if len(messages) <= 2:
                break 
            messages.pop(1)
    except Exception as e:
        print(f"[token budget error]: {e}")

def total_tokens_used(messages):
    return sum(len(ENCODING.encode(msg["content"])) for msg in messages)

def chat(user_input):
    Messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model=Model,
        messages = Messages,
        temperature=Temp, #using 1 would give you a very hallucinated answer
        max_tokens=Max_Tokens #use this not to spend too much money
    )
    reply = response.choices[0].message.content
    Messages.append({"role": "assistant", "content": reply})
    enforce_token_budget(Messages)
    return reply

while True:
    user_input = input("You: ")
    if user_input.strip().lower in {"exit", "quit"}:
        break
    answer = chat(user_input)
    print("You: ", user_input)
    print("Assistant:", answer)
    print("current tokens:", total_tokens_used(Messages))

