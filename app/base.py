from typing import List, Dict
import click, socket
from app.create_env import file_prompt
from app.plugin import davinci
from app.utils.constant import (
    init_conversation,
    ASSISTANT,
    MAX_WIDTH,
    color,
    top_left,
    bottom_left,
    IA,
    stick,
    BLANK,
    assistant_color,
)
from termcolor import colored


class Base_CGPT:

    """
    Baseclass to create a conversational infinite-loop with CGPT module
    """

    def __init__(
        self,
        exit_key: str,
        modify_api_key: str,
        input_text: str,
        decoration: str,
        encode: str,
        socket_resp: bool,
        icon_ans: str,
        socket_instance: socket = None,
    ) -> None:
        self.exit_key = exit_key
        self.modify_api_key = modify_api_key
        self.input_text = input_text
        self.decoration = decoration
        self.icon_ans = icon_ans
        self.encode = encode
        self.socket_resp = socket_resp
        self.socket_instance = socket_instance

    def _anonym_func(self, *args):
        return args[0]

    def _void_func(self) -> None:
        pass

    def _I_O_func(
        self,
        socket_resp: bool,
        previous_conv: List[Dict],
        client_input: str = None,
        socket=None,
    ) -> str:
        if socket_resp:
            if client_input is not None:
                socket.send(client_input.encode(self.encode.lower()))

            elif client_input == self.exit_key:
                return

            elif client_input == self.modify_api_key:
                file_prompt()
                return

            data = socket.recv(1024)
            res = str(data.decode(self.encode.lower()))
        else:
            res = davinci(client_input, previous_conv)

        return res

    def infinite_loop(self) -> None:
        while True:
            self._void_func()
            click.echo(BLANK)
            client = input(colored(self.input_text, assistant_color))
            click.echo(BLANK)
            if client == self.exit_key:
                break

            elif client == self.modify_api_key:
                file_prompt()
                break

            resp = self._I_O_func(
                self.socket_resp,
                previous_conv=init_conversation,
                client_input=client,
                socket=self.socket_instance,
            )
            init_conversation.append({"role": ASSISTANT, "content": resp})
            if resp is None:
                break

            result = resp
            len_res = len(result)
            emoji_str = IA.encode("utf-8").decode("utf-8") if IA != "IA" else "IA"

            if len(result) > MAX_WIDTH - 4:
                len_res = MAX_WIDTH - 4
            else:
                len_res = len(result)

            wrapped_result = [result]

            box = (
                colored(top_left, color)
                + colored("─", color) * (len_res + 2)
                + " "
                + emoji_str
                + "\n"
            )
            box += colored(stick, color) + " " * (len_res + 2) + "\n"

            for line in wrapped_result:
                box += (
                    colored(stick, color)
                    + " "
                    + colored(line)
                    + " " * (MAX_WIDTH - len(line) - 3)
                    + "\n"
                )

            box += colored(stick, color) + " " * (len_res + 2) + "\n"
            box += colored(bottom_left, color) + colored("─", color) * (len_res + 2)

            click.echo(box)
