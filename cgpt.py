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
def tellme():

    resp = "begin"

    while len(resp) > 0:

        client = input("Dîtes quelques chose (q to quit) > ")

        if client == "q":
            break

        resp = index(client)

        
        click.echo("----------------------------------------------------------")
        click.echo(f"<< 🤖 >> {resp}")
        click.echo("\n")
        click.echo("----------------------------------------------------------")
        


        

         

