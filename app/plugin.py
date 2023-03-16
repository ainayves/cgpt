import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def davinci(what):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=what,
    temperature=0.3,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    
    res = response["choices"][0]["text"]
    

    return f"🤖 << CLI-GPT >> {res}"