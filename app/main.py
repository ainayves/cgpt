import click 
from app.plugin import davinci
from app.file_service import file_prompt

def index(text_input : str) -> str:
    return davinci(text_input)


def prompt() -> None:
    resp = "begin"

    while len(resp) > 0:

        client = input(" Dîtes quelque chose (q : quitter , m : modifier api_key ) > ")

        if client == "q":
            break
        
        elif client == "m":
            
            file_prompt()
            break

        resp = index(client)

        if resp == None:
            break
        
        click.echo("----------------------------------------------------------")
        click.echo(f"<< 🤖 >> {resp}")
        click.echo("\n")
        click.echo("----------------------------------------------------------")
