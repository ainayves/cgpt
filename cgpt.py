# -*- coding: utf-8 -*-

import click, os, subprocess
from termcolor import colored
from app.main import prompt
from app.create_env import file_prompt
from app.utils.constant import (
    SERVER_PATH,
    CLIENT_PATH,
    CGPT_NETWORK,
    YOU_SERVER,
    OPEN_TERMINAL,
    WELCOME,
    error_color,
    color,
    BOLD,
    PYTHONSTR,
)


@click.command()
def cgpt():
    click.echo(colored(WELCOME, color=color, attrs=[BOLD]))

    cgpt_path = os.path.abspath(os.path.dirname(__file__))
    use_in_lan = click.confirm(colored(CGPT_NETWORK, error_color))

    if use_in_lan:
        endpoint = click.confirm(colored(YOU_SERVER, error_color))

        if endpoint:
            click.echo(colored(OPEN_TERMINAL, error_color))
            subprocess.run([PYTHONSTR, cgpt_path + SERVER_PATH])

        else:
            subprocess.run([PYTHONSTR, cgpt_path + CLIENT_PATH])

    else:
        if not os.path.isfile(".env"):
            file_prompt()
        else:
            prompt()
