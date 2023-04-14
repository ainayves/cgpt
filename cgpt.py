# -*- coding: utf-8 -*-

import click, os, subprocess
from termcolor import colored
from app.main import prompt
from app.file_service import file_prompt
from app.utils.constant import (
    SERVER_PATH,
    CLIENT_PATH,
    CGPT_NETWORK,
    YOU_SERVER,
    OPEN_TERMINAL
)

@click.command()
def cgpt():
    cgpt_path = os.path.abspath(os.path.dirname(__file__))
    use_in_lan = click.confirm(colored(CGPT_NETWORK, "yellow"))

    if use_in_lan:
        endpoint = click.confirm(colored(YOU_SERVER, "yellow"))

        if endpoint:
            click.echo(colored(OPEN_TERMINAL, "yellow"))
            subprocess.run(["python", cgpt_path + SERVER_PATH])

        else:
            subprocess.run(["python", cgpt_path + CLIENT_PATH])

    else:
        if not os.path.isfile(".env"):
            file_prompt()
        else:
            prompt()
