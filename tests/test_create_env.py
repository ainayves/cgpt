import getpass
import os
from pathlib import Path

from cgpt.app.create_env import file_prompt
from cgpt.app.utils.constant import STR_OPENAI_API_KEY


file_path = os.path.dirname(os.path.abspath(__file__))


def test_file_prompt(monkeypatch):
    # Set up test data
    expected_api_key = "sk-myapikey"
    env_file = Path(file_path + "/.env")

    def mock_getpass(prompt):
        return expected_api_key

    monkeypatch.setattr(getpass, "getpass", mock_getpass)
    monkeypatch.setenv(STR_OPENAI_API_KEY, expected_api_key)

    file_prompt(file_path)

    assert env_file.is_file() == True  # noqa: E712
    with env_file.open("r") as f:
        env_data = f.read()
    assert f"{STR_OPENAI_API_KEY}={expected_api_key}" in env_data.replace(
        "\n", ""
    ).replace("'", "")

    monkeypatch.setattr(getpass, "getpass", lambda prompt: "")
    file_prompt()

    with env_file.open("r") as f:
        env_data = f.read()

    assert (
        env_data.replace("\n", "").replace("'", "")
        == f"{STR_OPENAI_API_KEY}={expected_api_key}"
    )
