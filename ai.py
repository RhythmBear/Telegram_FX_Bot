import openai
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

user_input = ""
while user_input != "quit()":
    user_input = input("Type your message here : ")
    message = {"role": "user", "content": user_input}
    messages.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")