import os

from cgpt.app.create_env import file_prompt


def _check_env_file(self) -> None:
    if not os.path.isfile(".env"):
        file_prompt()
