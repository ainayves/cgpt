import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello World")