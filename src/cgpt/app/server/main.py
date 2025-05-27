import socket
import threading

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


def handle_client(client_socket: socket.socket) -> None:
    conversation_context = init_conversation

    while True:
        try:
            data = client_socket.recv(1024).decode(UTF)

            if not data:
                break

            if data == PING:
                client_socket.send(PONG.encode(UTF))
                continue

            response = davinci(data, conversation_context)
            if response is not None:
                client_socket.send(response.encode(UTF))

        except (BrokenPipeError, ConnectionResetError):
            click.echo(colored(DECONNECTED_HOST, error_color))
            break

    client_socket.close()


def start_server(port: int, ip_address: str = None) -> None:
    host = ip_address or socket.gethostbyname(socket.gethostname())
    server_socket = socket.create_server((host, port), reuse_port=False)
    server_socket.listen()

    click.echo(colored(f"{SERVER_LIVE} {host} ..{LIVE}", color))

    while True:
        client_socket, _ = server_socket.accept()
        threading.Thread(
            target=handle_client, args=(client_socket,), daemon=True
        ).start()


if __name__ == "__main__":
    start_server(PORT)
