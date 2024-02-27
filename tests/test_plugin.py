import io
import os
import getpass
import pytest
import openai
from dotenv import load_dotenv

from cgpt.app.plugin import davinci
from cgpt.app.utils.constant import STR_OPENAI_API_KEY
from cgpt.app.utils.constant import init_conversation


load_dotenv()


def test_correct_openai_api_key():
    openai.api_key = os.getenv(STR_OPENAI_API_KEY)

    if os.getenv(STR_OPENAI_API_KEY) != "sk-myapikey":
        ouptut = davinci("bjr", previous_conv=init_conversation)
        assert isinstance(ouptut, str)
    else:
        def mock_getpass(prompt):
            return "randomstring"

        pytest.MonkeyPatch.setattr(getpass, "getpass", mock_getpass)

        ouptut = davinci("bjr", previous_conv=init_conversation)
        assert ouptut is None


def test_wrong_openai_key(monkeypatch):
    openai.api_key = "abcd"
    monkeypatch.setattr("sys.stdin", io.StringIO("q"))
    ouptut = davinci("bjr", previous_conv=init_conversation)
    assert ouptut is None
