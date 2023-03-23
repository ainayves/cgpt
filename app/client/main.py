# -*- coding: utf-8 -*-

import socket, click , os
from app.file_service import file_prompt

 
def Main():
    
    adresse_ip = click.prompt("Entrez l' adresse IP du serveur ")
    port = 2048
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:

        s.connect((adresse_ip,port))
        while True:
            
            if not os.path.isfile(".env"): 

                file_prompt()

            client = input(" Dîtes quelque chose (q : quitter , m : modifier api_key ) > ")

            if client == "q":    
                break
            
            elif client == "m":
                
                file_prompt()
                break

            s.send(client.encode('utf-8'))
            data = s.recv(1024)

            click.echo("----------------------------------------------------------")
            click.echo(f"<< 🤖 >> {str(data.decode('utf-8'))}")
            click.echo("\n")
            click.echo("----------------------------------------------------------")
   
    except BrokenPipeError:
        click.echo("Connexion perdue 😥")
    
    except socket.gaierror:
        click.echo("Connexion impossible 😥")

    finally:
        # close the connection
        s.close()
 
if __name__ == '__main__':
    Main()