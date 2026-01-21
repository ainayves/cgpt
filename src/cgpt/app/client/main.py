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


def validate_ip(ip: str) -> bool:
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False


def connect_to_server(ip: str, port: int) -> socket.socket | None:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
        return client_socket
    except OSError as e:
        if e.errno == 113:
            click.echo(colored(CONNECTION_IMPOSSIBLE, error_color))
        else:
            click.echo(colored(f"{CONNECTION_ERROR} {e}", error_color))
        return None


def launch_client_session(sock: socket.socket) -> None:
    Base_CGPT._void_func = _check_env_file  # si nécessaire
    cgpt = Base_CGPT(
        exit_key="q",
        modify_api_key="m",
        input_text=SAY_SOMETHING,
        decoration=DASHED,
        encode=UTF,
        icon_ans=IA,
        socket_resp=True,
        socket_instance=sock,
    )
    cgpt.infinite_loop()


def main() -> None:
    ip_input = click.prompt(colored(ENTER_SERVER_IP, error_color))

    if not validate_ip(ip_input):
        click.echo(colored(ADDRESS_NOT_VALID, error_color))
        return

    client_socket = connect_to_server(ip_input, PORT)
    if client_socket:
        try:
            launch_client_session(client_socket)
        finally:
            client_socket.close()


if __name__ == "__main__":
    main()
