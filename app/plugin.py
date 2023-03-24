# -*- coding: utf-8 -*-

import os, click
from typing import Union
import openai
from app.file_service import file_prompt
from dotenv import load_dotenv
load_dotenv()
from app.utils.constant import (
    HUMAN,
    AI_COLON,
    CHOICES,
    TEXT,
    STR_OPENAI_API_KEY,
    DAVINCI_MODEL,
    DAVINCI_PROMPT,
    INCORRECT_API_KEY,
    TEMPERATURE,
    MAX_TOKENS,
    TOP_P,
    FREQUENCY_P,
    PRESENCE_P,
    OPENAI_REQUEST_TIMEOUT,
    NOT_CONNECTED,
    AI_COLON_SPACE,
    TOO_MUCH_REQUEST
)

openai.api_key = os.getenv(STR_OPENAI_API_KEY)

def davinci(what : str) -> Union[str, None]:

    try:
        response = openai.Completion.create(
        model=DAVINCI_MODEL,
        prompt=f"{DAVINCI_PROMPT}{what}",
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_P,
        presence_penalty=PRESENCE_P,
        stop=[HUMAN, AI_COLON_SPACE]
        )
        
        res = response[CHOICES][0][TEXT].replace(AI_COLON,"")

    except openai.error.AuthenticationError:

        modify_apikey = input(INCORRECT_API_KEY)

        if modify_apikey == "m" :

            file_prompt()
            res = None
            
        else:

            res = None
            
    except openai.error.Timeout:

        click.echo(OPENAI_REQUEST_TIMEOUT)
        res = None

    
    except openai.error.APIConnectionError:

        click.echo(NOT_CONNECTED)
        res = None

    except openai.error.RateLimitError:

        click.echo(TOO_MUCH_REQUEST)
        res = None

    return res