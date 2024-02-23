import click
from cgpt.app.utils.constant import VERSION


@click.command()
def version():
    click.echo(VERSION)
