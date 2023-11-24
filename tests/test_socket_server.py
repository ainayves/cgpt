import socket
import threading
from app.server.main import threaded
from app.utils.constant import PING, PONG , UTF


def test_thread():

    # Create server
    port = 1234
    ip_address = socket.gethostbyname(socket.gethostname())
    server_socket = socket.create_server((ip_address, int(port)), reuse_port=False)
    server_socket.listen()
    client, _ = server_socket.accept()
    threading.Thread(target=threaded, args=(client,), daemon=True).start()

    # Connect the client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))
    message = PING
    s.send(message.encode(encoding=UTF))
    response = s.recv(1024).decode()


    assert response == PONG

