import click
from ..utils.constant import VERSION


@click.command()
def version():
    click.echo(VERSION)
