import socket
import threading
from app.server.main import main , threaded

def get_available_port(host : str):
    # Set the target host and port range
    target_host = host
    port_range = range(1, 65535)

    # Iterate over the port range and check each port
    for port in port_range:
        try:
            # Try to create a new socket and connect to the target host
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_socket.bind((target_host, port))
            new_socket.listen(1)
        
        except OSError:
            continue
        
        else:
            res = port
            new_socket.close()

    return res

# print(get_available_port(str(socket.gethostbyname(socket.gethostname()))))

def test_threaded():
    ip_address = socket.gethostbyname(socket.gethostname())
    #ip_address = "localhost"
    port = get_available_port(str(ip_address))

    print(">>>>",port)

    # Create a socket server
    server_socket = socket.create_server((ip_address, int(port)), reuse_port=False)
    server_socket.listen()
    client, _ = server_socket.accept()
    threading.Thread(target=threaded, args=(client,), daemon=True).start()

    # Connect a client to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port))

    # Send a message to the server
    message = "PING"
    client_socket.sendall(message.encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode()

    # Verify that the server responded correctly
    assert response == "PONG"