import openai
import os
import io
from cgpt.app.plugin import davinci
from cgpt.app.utils.constant import STR_OPENAI_API_KEY, init_conversation
from dotenv import load_dotenv

load_dotenv()


def test_correct_openai_api_key():
    openai.api_key = os.getenv(STR_OPENAI_API_KEY)
    ouptut = davinci("bjr", previous_conv=init_conversation)

    assert isinstance(ouptut, str)


def test_wrong_openai_key(monkeypatch):
    openai.api_key = "abcd"
    monkeypatch.setattr("sys.stdin", io.StringIO("q"))
    ouptut = davinci("bjr", previous_conv=init_conversation)
    assert ouptut is None
