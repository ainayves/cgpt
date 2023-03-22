import socket
from _thread import *
import threading
print_lock = threading.Lock()

def threaded(c):
    
    while True:
        pass

def main():
   
    server_socket = socket.create_server(("localhost", 2048), reuse_port=False)
    server_socket.listen()
    while True:
        client, _ = server_socket.accept()
        threading.Thread(target=threaded,args=(client,), daemon=True).start()

if __name__ == "__main__":
    main()