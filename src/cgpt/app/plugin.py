import os
from typing import Dict
from typing import List
from typing import Union

import click
import openai
from dotenv import load_dotenv
from termcolor import colored

from cgpt.app.create_env import file_prompt
from cgpt.app.utils.constant import AI_COLON
from cgpt.app.utils.constant import CHOICES
from cgpt.app.utils.constant import CONTENT
from cgpt.app.utils.constant import DAVINCI_MODEL
from cgpt.app.utils.constant import INCORRECT_API_KEY
from cgpt.app.utils.constant import MESSAGE
from cgpt.app.utils.constant import NOT_CONNECTED
from cgpt.app.utils.constant import OPENAI_REQUEST_TIMEOUT
from cgpt.app.utils.constant import STR_OPENAI_API_KEY
from cgpt.app.utils.constant import TOO_MUCH_REQUEST
from cgpt.app.utils.constant import USER
from cgpt.app.utils.constant import error_color


load_dotenv()
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
