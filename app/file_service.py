# -*- coding: utf-8 -*-

import click , os , getpass ,dotenv

def file_prompt() -> None:
    
    api_key = getpass.getpass(" Ajoutez votre api key (invisible input) > ")
    
    if api_key :

        fichier = open(".env", "w")
        fichier.close()
        dotenv.set_key(".env", "OPENAI_API_KEY", api_key)

        click.echo("Votre API KEY a bien été ajouté , veuillez relancer la commande `cgpt tellme` ")

    elif api_key =="" or not api_key:

        click.echo("\n Vous n' avez pas ajouter un API KEY \n")