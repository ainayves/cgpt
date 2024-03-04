import os
import subprocess

import click
from termcolor import colored
from simple_term_menu import TerminalMenu
import dotenv


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
    MODEL,
    MODEL_USED,
    MODELS_LIST,
    CHOOSE_OTHERS,
    CHOOSE_MODEL,
    YOU_SELECTED,
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
@click.option("--model", "-m", is_flag=True, help=CHOOSE_MODEL)
def cgpt(version, apikey, lan, model):
    try:
        if version:
            click.echo(f"cgpt v{VERSION}")
        elif apikey:
            click.echo(colored(WELCOME, color=color, attrs=[BOLD]))
            file_prompt()

        elif model:
            click.echo(
                colored(MODEL_USED + os.getenv(MODEL), color=color, attrs=[BOLD])
            )
            click.echo(colored(CHOOSE_OTHERS, color=color, attrs=[BOLD]))
            options = MODELS_LIST
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()

            if menu_entry_index:
                dotenv.set_key(".env", MODEL, options[menu_entry_index])
                click.echo(
                    colored(
                        YOU_SELECTED + options[menu_entry_index] + " ✨", error_color
                    )
                )

            else:
                pass
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
