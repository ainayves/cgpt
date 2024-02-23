import click

from . import *


@click.command()
def version():
    click.echo(VERSION)
