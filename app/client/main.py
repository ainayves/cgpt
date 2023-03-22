import socket, click , os
from app.file_service import file_prompt
 
def Main():
    adresse_ip = socket.gethostbyname(socket.gethostname())
    port = 2048
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    click.echo(f"--> Connexion à {adresse_ip}:{port}")
    try:
        s.connect((adresse_ip,port))
        click.echo(f"---> Connecté à {adresse_ip}:{port}")
        while True:
            
            if not os.path.isfile(".env"): 

                file_prompt()

            client = input(" Dîtes quelque chose (q : quitter , m : modifier api_key ) > ")

            if client == "q":
                
                break
            
            elif client == "m":
                
                file_prompt()
                break

            s.send(client.encode('ascii'))
            data = s.recv(1024)
            resp = str(data.decode('ascii'))

            click.echo("----------------------------------------------------------")
            click.echo(f"<< 🤖 >> {resp}")
            click.echo("\n")
            click.echo("----------------------------------------------------------")
   
    except BrokenPipeError:
        print("Connexion perdu")

    finally:
        # close the connection
        s.close()
 
if __name__ == '__main__':
    Main()