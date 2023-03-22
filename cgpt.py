import click , os , subprocess
from app.main import prompt
from app.file_service import file_prompt
from utils.constant import SERVER_PATH


@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
def tellme():
    
    use_in_lan = click.confirm("Est ce que voulez vous utiliser cgpt en réseaux ? ")
    script_path = SERVER_PATH
    if use_in_lan:
        subprocess.run(['python', script_path])

    else : 

        if not os.path.isfile(".env"): 

            file_prompt()
        else:

            prompt()
        


        

         

