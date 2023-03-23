import click
from app.file_service import file_prompt

class Base_CGPT():
    """
    This is the Baseclass to create a conversation infinite loop with CGPT
    """
    def __init__(
            self, exit_key : str, 
            modify_api_key : str, 
            input_text : str , 
            decoration : str, 
            icon_ans :str) -> None:

        self.exit_key = exit_key
        self.modify_api_key = modify_api_key
        self.input_text = input_text
        self.decoration = decoration
        self.icon_ans = icon_ans

    def _anonym_func(self, _client : str):

        return _client

    def infinite_loop(self):

        while True :

            client = input(self.input_text)

            if client == self.exit_key:
                break
            
            elif client == self.modify_api_key:
                
                file_prompt()
                break

            resp = self._anonym_func(client)

            if resp == None:
                break
            
            click.echo(self.decoration, color=True)
            click.echo(f"<< {self.icon_ans} >> {resp}")
            click.echo("\n")
            click.echo(self.decoration, color=True)

