import click , os , subprocess
from app.main import prompt
from app.file_service import file_prompt
from utils.constant import SERVER_PATH , CLIENT_PATH


@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
def tellme():
    
    cgpt_path = os.path.abspath(os.path.dirname(__file__))   
    use_in_lan = click.confirm("Est ce que voulez vous utiliser cgpt en réseaux ? ")
    
    if use_in_lan:

        endpoint = click.confirm("Êtes vous le serveur 😃 ?  ")

        if endpoint:
            click.echo("Veuillez ouvrir un autre terminal..😌")
            subprocess.run(['python', cgpt_path+SERVER_PATH])
        
        else:
            subprocess.run(['python', cgpt_path+CLIENT_PATH])

    else : 

        if not os.path.isfile(".env"): 

            file_prompt()
        else:

            prompt()
        


        

         

