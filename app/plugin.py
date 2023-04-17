# -*- coding: utf-8 -*-

import os, click
from termcolor import colored
from typing import Union, List, Dict
import openai
from app.create_env import file_prompt
from dotenv import load_dotenv

load_dotenv()
from app.utils.constant import (
    AI_COLON,
    CHOICES,
    STR_OPENAI_API_KEY,
    DAVINCI_MODEL,
    INCORRECT_API_KEY,
    MESSAGE,
    CONTENT,
    OPENAI_REQUEST_TIMEOUT,
    NOT_CONNECTED,
    TOO_MUCH_REQUEST,
    USER,
    error_color,
)

openai.api_key = os.getenv(STR_OPENAI_API_KEY)


def davinci(what: str, previous_conv: List[Dict]) -> Union[str, None]:
    try:
        previous_conv.append({"role": USER, "content": what})
        response = openai.ChatCompletion.create(
            model=DAVINCI_MODEL, messages=previous_conv
        )

        res = response[CHOICES][0][MESSAGE][CONTENT].replace(AI_COLON, "")

    except openai.error.AuthenticationError:
        modify_apikey = input(INCORRECT_API_KEY)

        if modify_apikey == "m":
            file_prompt()
            res = None

        else:
            res = None

    except openai.error.Timeout:
        click.echo(colored(OPENAI_REQUEST_TIMEOUT, error_color))
        res = None

    except openai.error.APIConnectionError:
        click.echo(colored(NOT_CONNECTED, error_color))
        res = None

    except openai.error.RateLimitError:
        click.echo(colored(TOO_MUCH_REQUEST, error_color))
        res = None

    return res
