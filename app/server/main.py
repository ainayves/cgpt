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

            api_response = davinci(client_data, init_conversation_client)
            if api_response is not None:
                c.send(api_response.encode(encoding=UTF))
            else:
                continue

        except BrokenPipeError:
            continue

        except ConnectionResetError:
            click.echo(colored(DECONNECTED_HOST, error_color))


def main():
    adresse_ip = socket.gethostbyname(socket.gethostname())
    server_socket = socket.create_server((adresse_ip, int(PORT)), reuse_port=False)
    server_socket.listen()
    click.echo(colored(f"{SERVER_LIVE} {adresse_ip} ..{LIVE}", color))
    while True:
        client, _ = server_socket.accept()
        threading.Thread(target=threaded, args=(client,), daemon=True).start()


if __name__ == "__main__":
    main()
