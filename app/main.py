# -*- coding: utf-8 -*-

from app.plugin import davinci
from app.utils.constant import (
    SAY_SOMETHING,
    DASHED,
    IA
)

from app.base import Base_CGPT

def index(self, text_input : str) -> str:
    return davinci(text_input)


def prompt() -> None:
    
    # while True:

    #     client = input(SAY_SOMETHING)

    #     if client == "q":
    #         break
        
    #     elif client == "m":
            
    #         file_prompt()
    #         break

    #     resp = index(client)

    #     if resp == None:
    #         break
        
    #     click.echo(DASHED, color=True)
    #     click.echo(f"<< {IA} >> {resp}")
    #     click.echo("\n")
    #     click.echo(DASHED, color=True)

    Base_CGPT._anonym_func = index

    cgpt = Base_CGPT(
        exit_key="q",
        modify_api_key="m",
        input_text=SAY_SOMETHING,
        decoration=DASHED,
        icon_ans=IA

    )

    cgpt.infinite_loop()

    
