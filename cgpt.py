import click
from app.main import index
import dotenv
import getpass

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
def tellme():
    
    api_key = getpass.getpass(" Ajouter votre api key > ")
    fichier = open(".env", "w")
    fichier.close()

    dotenv.set_key(".env", "OPENAI_API_KEY", api_key)
    
    
    if api_key :
        resp = "begin"

        while len(resp) > 0:

            client = input(" Dîtes quelque chose (q to quit) > ")

            if client == "q":
                break

            resp = index(client)

            
            click.echo("----------------------------------------------------------")
            click.echo(f"<< 🤖 >> {resp}")
            click.echo("\n")
            click.echo("----------------------------------------------------------")
    else:
        click.echo("vous n' avez pas ajouter un key")
        


        

         

