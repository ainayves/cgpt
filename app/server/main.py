# -*- coding: utf-8 -*-

import socket, click
from _thread import *
import threading
from termcolor import colored

print_lock = threading.Lock()
from app.plugin import davinci
from app.utils.constant import (
    PORT,
    SERVER_LIVE,
    UTF,
    LIVE,
    PING,
    PONG,
    DECONNECTED_HOST,
    init_conversation,
    error_color,
    color,
)


def threaded(c):
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


def main(port, ip_address=None):
    if ip_address is None:
        auto_detcted_ip = socket.gethostbyname(socket.gethostname())
        server_socket = socket.create_server(
            (auto_detcted_ip, int(port)), reuse_port=False
        )
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
