import click
from app.main import index

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
@click.option('-t','--text' , type=str, help='Use this option to ask your question', default='How are you ?')
def tellme(text):     
    click.echo("------------------------THINKING--------------------------")
    click.echo("----------------------------------------------------------")
    click.echo(index(text))
    click.echo("----------------------------------------------------------")
    click.echo("----------------------------------------------------------")

