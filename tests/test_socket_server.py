import socket
import threading
from app.server.main import main
from app.utils.constant import PING, PONG


def test_main_server():
    pass
    # port = 1234
    # ip_address = socket.gethostbyname(socket.gethostname())

    # # Start the server in a separate thread
    # server_thread = threading.Thread(target=main, args=(port, ip_address))
    # server_thread.start()

    # # Connect a client to the server
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect((ip_address, port))

    # # Send a message to the server
    # message = PING
    # client_socket.sendall(message.encode())

    # # Receive the response from the server
    # response = client_socket.recv(1024).decode()

    # # Verify that the server responded correctly
    # assert response == PONG
