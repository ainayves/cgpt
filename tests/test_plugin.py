from app.plugin import davinci


def test_openai_func():

    res = davinci("bjr", previous_conv=[{"role": "system", "content": "You are a helpful assistant."}])

    assert isinstance(res, str)