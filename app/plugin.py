import os, click
from typing import Union
import openai
from app.file_service import file_prompt
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def davinci(what : str) -> Union[str, None]:

    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman:{what}",
        temperature=0.9,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        
        res = response["choices"][0]["text"].replace("AI Assistant:","")

    
    except openai.error.AuthenticationError:

        modify_apikey = input("Votre API KEY est incorrect, tapez `m` pour modifer le key , ou `q` pour quitter > ")

        if modify_apikey == "m" :

            file_prompt()
            res = None
            
        else:

            res = None
            

    return res