# -*- coding: utf-8 -*-

import click , os , subprocess
from app.main import prompt
from app.file_service import file_prompt
from app.utils.constant import (
    SERVER_PATH, 
    CLIENT_PATH,
    CGPT_NETWORK,
    YOU_SERVER,
    OPEN_TERMINAL,
    VERSION
    )


@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
def version():
    click.echo(VERSION)

@cli.command()
def tellme():
    
    cgpt_path = os.path.abspath(os.path.dirname(__file__))   
    use_in_lan = click.confirm(CGPT_NETWORK)
    
    if use_in_lan:

        endpoint = click.confirm(YOU_SERVER)

        if endpoint:
            click.echo(OPEN_TERMINAL)
            subprocess.run(['python', cgpt_path+SERVER_PATH])
        
        else:
            subprocess.run(['python', cgpt_path+CLIENT_PATH])

    else : 

        if not os.path.isfile(".env"): 

            file_prompt()
        else:

            prompt()
        


        

         

