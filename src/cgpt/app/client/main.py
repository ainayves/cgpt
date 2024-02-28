import ipaddress
import socket

import click
from termcolor import colored

from cgpt.app.base import Base_CGPT
from cgpt.app.utils.constant import (
    ADDRESS_NOT_VALID,
    CONNECTION_ERROR,
    CONNECTION_IMPOSSIBLE,
    DASHED,
    ENTER_SERVER_IP,
    IA,
    PORT,
    SAY_SOMETHING,
    UTF,
    error_color,
)

from cgpt.app.utils.verify_env import _check_env_file


def main() -> None:
    adresse_ip = click.prompt(colored(ENTER_SERVER_IP, error_color))

    try:
        ipaddress.IPv4Address(adresse_ip)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((adresse_ip, int(PORT)))
            Base_CGPT._void_func = _check_env_file

            cgpt = Base_CGPT(
                exit_key="q",
                modify_api_key="m",
                input_text=SAY_SOMETHING,
                decoration=DASHED,
                encode=UTF,
                icon_ans=IA,
                socket_resp=True,
                socket_instance=s,
            )

            cgpt.infinite_loop()

        except OSError as e:
            if e.errno == 113:
                click.echo(colored(CONNECTION_IMPOSSIBLE, error_color))
            else:
                click.echo(colored(f"{CONNECTION_ERROR} {e}", error_color))

        finally:
            s.close()

    except ipaddress.AddressValueError:
        click.echo(ADDRESS_NOT_VALID)


if __name__ == "__main__":
    main()
