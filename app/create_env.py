# -*- coding: utf-8 -*-

import click, os, getpass, dotenv
from termcolor import colored
from app.utils.constant import (
    GET_API_KEY,
    API_KEY_ADDED,
    API_KEY_NOT_ADDED,
    STR_OPENAI_API_KEY,
    color,
)


def file_prompt(output_path=None) -> None:
    api_key = getpass.getpass(GET_API_KEY)

    if output_path is None:
        output_path = ""

    if api_key:
        fichier = open(output_path + ".env", "w")
        fichier.close()
        dotenv.set_key(output_path + ".env", STR_OPENAI_API_KEY, api_key)

        click.echo(colored(API_KEY_ADDED, color))

    elif api_key == "" or not api_key:
        click.echo(colored(API_KEY_NOT_ADDED, color))
