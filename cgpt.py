import click , os
from app.main import prompt
from app.file_service import file_prompt

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
def tellme():
    
    if not os.path.isfile(".env"): 

        file_prompt()
    else:

        prompt()
        


        

         

