import click
from app.utils.constant import VERSION


@click.command()
def version():
    click.echo(VERSION)
