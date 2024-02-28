import socket
import threading
from _thread import *  # noqa: F403

import click
from termcolor import colored

from cgpt.app.plugin import davinci
from cgpt.app.utils.constant import (
    DECONNECTED_HOST,
    LIVE,
    PING,
    PONG,
    PORT,
    SERVER_LIVE,
    UTF,
    color,
    error_color,
    init_conversation,
)


print_lock = threading.Lock()


def threaded(c) -> None:
    init_conversation_client = init_conversation
    while True:
        try:
            client_data = c.recv(1024).decode()

            if client_data == PING:
                c.send(PONG.encode(encoding=UTF))

            api_response = davinci(client_data, init_conversation_client)
            if api_response is not None:
                c.send(api_response.encode(encoding=UTF))
            else:
                continue

        except BrokenPipeError:
            continue

        except ConnectionResetError:
            click.echo(colored(DECONNECTED_HOST, error_color))


def main(port: int, ip_address=None) -> None:
    if ip_address is None:
        auto_detcted_ip = socket.gethostbyname(socket.gethostname())
        server_socket = socket.create_server((auto_detcted_ip, port), reuse_port=False)
        server_socket.listen()
        click.echo(colored(f"{SERVER_LIVE} {auto_detcted_ip} ..{LIVE}", color))

    else:
        server_socket = socket.create_server((ip_address, int(port)), reuse_port=False)
        server_socket.listen()

    while True:
        client, _ = server_socket.accept()
        threading.Thread(target=threaded, args=(client,), daemon=True).start()


if __name__ == "__main__":
    main(PORT, None)
