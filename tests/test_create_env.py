import getpass , os
from app.create_env import file_prompt
from app.utils.constant import STR_OPENAI_API_KEY
from pathlib import Path

def test_file_prompt(monkeypatch):
    # Set up test data
    expected_api_key = "my_api_key"
    env_file = Path(os.path.dirname(os.path.abspath(__file__)).replace("tests","") + "/.env")
    # Define a mock function to replace getpass.getpass()
    def mock_getpass(prompt):
        return expected_api_key

    # Use monkeypatch to replace getpass.getpass() with our mock function
    monkeypatch.setattr(getpass, "getpass", mock_getpass)

    # Call the function to prompt for the API key
    file_prompt()

    # Assert that the .env file was created and contains the expected API key
    assert env_file.is_file() == True
    with env_file.open("r") as f:
        env_data = f.read()
    assert f"{STR_OPENAI_API_KEY}={expected_api_key}" in env_data.replace('\n',"").replace("'","")

    # Call the function again with no input
    monkeypatch.setattr(getpass, "getpass", lambda prompt: "")
    file_prompt()
    
    # Assert that the .env file was not modified
    with env_file.open("r") as f:
        env_data = f.read()
    assert env_data.replace('\n',"").replace("'","") == f"{STR_OPENAI_API_KEY}={expected_api_key}"
