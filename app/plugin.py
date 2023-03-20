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
        prompt=what,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        
        res = response["choices"][0]["text"]

        return res
    
    except openai.error.AuthenticationError:

        modify_apikey = input("Votre API KEY est incorrect, tapez `m` pour modifer le key , ou `q` pour quitter > ")

        if modify_apikey == "m" :

            file_prompt()
            click.echo("API KEY modifié avec succès")
        
        else:

            click.echo("Votre API KEY nécessite d' être modifier")
            

        return None