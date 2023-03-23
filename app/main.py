# -*- coding: utf-8 -*-

import click 
from app.plugin import davinci
from app.file_service import file_prompt
from app.utils.constant import (
    SAY_SOMETHING,
    DASHED,
    IA,
    BEGIN
)

def index(text_input : str) -> str:
    return davinci(text_input)


def prompt() -> None:
    resp = BEGIN
    
    while len(resp) > 0:

        client = input(SAY_SOMETHING)

        if client == "q":
            break
        
        elif client == "m":
            
            file_prompt()
            break

        resp = index(client)

        if resp == None:
            break
        
        click.echo(DASHED, color=True)
        click.echo(f"<< {IA} >> {resp}")
        click.echo("\n")
        click.echo(DASHED, color=True)
