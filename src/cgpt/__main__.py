# """Command-line interface."""
# import click


# @click.command()
# @click.version_option()
# def main() -> None:
#     """Cgpt."""


# if __name__ == "__main__":
#     main(prog_name="cgpt")  # pragma: no cover

# -*- coding: utf-8 -*-

import os
import subprocess

import click
from termcolor import colored

from cgpt.app.create_env import file_prompt
from cgpt.app.main import prompt
from cgpt.app.utils.constant import BOLD
from cgpt.app.utils.constant import CGPT_NETWORK
from cgpt.app.utils.constant import CLIENT_PATH
from cgpt.app.utils.constant import OPEN_TERMINAL
from cgpt.app.utils.constant import PYTHONSTR
from cgpt.app.utils.constant import SERVER_PATH
from cgpt.app.utils.constant import WELCOME
from cgpt.app.utils.constant import YOU_SERVER
from cgpt.app.utils.constant import color
from cgpt.app.utils.constant import error_color


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
