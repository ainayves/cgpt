# -*- coding: utf-8 -*-

import socket, click
from _thread import *
import threading
print_lock = threading.Lock()
from app.plugin import davinci
from app.utils.constant import PORT , SERVER_LIVE , UTF ,init_conversation

def threaded(c):
    
    init_conversation_client = init_conversation
    while True:
        
        client_data = c.recv(1024).decode()
        try:
            
            if client_data is not None : 
                c.send(davinci(client_data, init_conversation_client).encode(encoding=UTF))
            else : 
                continue
        
        except BrokenPipeError:
            continue

def main():
    adresse_ip = socket.gethostbyname(socket.gethostname())
    server_socket = socket.create_server((adresse_ip, 2048), reuse_port=False)
    server_socket.listen()
    click.echo(f"{SERVER_LIVE} {adresse_ip}:{PORT} ..")
    while True:
        client, _ = server_socket.accept()
        threading.Thread(target=threaded,args=(client,), daemon=True).start()

if __name__ == "__main__":
    main()