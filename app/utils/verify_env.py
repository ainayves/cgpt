import os
from app.file_service import file_prompt


def _check_env_file(self):
    if not os.path.isfile(".env"):
        file_prompt()
