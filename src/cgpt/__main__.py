import os
import subprocess

import click
from termcolor import colored

from cgpt.app.create_env import file_prompt
from cgpt.app.main import prompt
from cgpt.app.utils.constant import (
    BOLD,
    BYE,
    CLIENT_PATH,
    OPEN_TERMINAL,
    PYTHONSTR,
    SERVER_PATH,
    WELCOME,
    YOU_SERVER,
    VERSION,
    APIKEY_OPTION,
    VERSION_OPTION,
    LAN_OPTION,
    color,
    error_color,
)


@click.command()
@click.option("--apikey", "-a", is_flag=True, help=APIKEY_OPTION)
@click.option("--version", "-v", is_flag=True, help=VERSION_OPTION)
@click.option(
    "--lan",
    "-l",
    is_flag=True,
    help=LAN_OPTION,
)
def cgpt(version, apikey, lan):
    try:
        if version:
            click.echo(f"cgpt v{VERSION}")
        elif apikey:
            click.echo(colored(WELCOME, color=color, attrs=[BOLD]))
            file_prompt()

        elif lan:
            click.echo(colored(WELCOME, color=color, attrs=[BOLD]))

            cgpt_path = os.path.abspath(os.path.dirname(__file__))
            endpoint = click.confirm(colored(YOU_SERVER, error_color))

            if endpoint:
                click.echo(colored(OPEN_TERMINAL, error_color))
                subprocess.run([PYTHONSTR, cgpt_path + SERVER_PATH])

            else:
                subprocess.run([PYTHONSTR, cgpt_path + CLIENT_PATH])

        else:
            click.echo(colored(WELCOME, color=color, attrs=[BOLD]))

            if not os.path.isfile(".env"):
                file_prompt()
            else:
                prompt()

    except click.exceptions.Abort:
        click.echo(BYE)
