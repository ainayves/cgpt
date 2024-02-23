import click

from cgpt.app.utils.constant import VERSION


@click.command()
def version() -> None:
    click.echo(VERSION)
