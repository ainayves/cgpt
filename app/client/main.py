# -*- coding: utf-8 -*-

import socket, click , os
from app.file_service import file_prompt
from app.utils.constant import (
    UTF,
    IA,
    SAY_SOMETHING,
    ENTER_SERVER_IP,
    CONNECTION_LOST,
    CONNECTION_IMPOSSIBLE,
    DASHED
)   

 
def Main():
    
    adresse_ip = click.prompt(ENTER_SERVER_IP)
    port = 2048
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:

        s.connect((adresse_ip,port))
        while True:
            
            if not os.path.isfile(".env"): 

                file_prompt()

            client = input(SAY_SOMETHING)

            if client == "q":    
                break
            
            elif client == "m":
                
                file_prompt()
                break

            s.send(client.encode(UTF.lower()))
            data = s.recv(1024)

            click.echo(DASHED, color=True)
            click.echo(f"<< {IA} >> {str(data.decode(UTF.lower()))}")
            click.echo("\n")
            click.echo(DASHED, color=True)
   
    except BrokenPipeError:
        click.echo(CONNECTION_LOST)
    
    except socket.gaierror:
        click.echo(CONNECTION_IMPOSSIBLE)

    finally:
        # close the connection
        s.close()
 
if __name__ == '__main__':
    Main()