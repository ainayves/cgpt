import os
from app.create_env import file_prompt


def _check_env_file(self):
    if not os.path.isfile(".env"):
        file_prompt()
