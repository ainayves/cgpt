# -*- coding: utf-8 -*-

import click , os , getpass ,dotenv
from app.utils.constant import (
    GET_API_KEY,
    API_KEY_ADDED,
    API_KEY_NOT_ADDED,
    STR_OPENAI_API_KEY

)

def file_prompt() -> None:
    
    api_key = getpass.getpass(GET_API_KEY)
    
    if api_key :

        fichier = open(".env", "w")
        fichier.close()
        dotenv.set_key(".env", STR_OPENAI_API_KEY, api_key)

        click.echo(API_KEY_ADDED)

    elif api_key =="" or not api_key:

        click.echo(API_KEY_NOT_ADDED)