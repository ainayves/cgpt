from cgpt.app.utils.constant import WELCOME


def add_welcome(f):
    """
    Add the version of the tool to the help heading.

    :param f: function to decorate
    :return: decorated function
    """

    f.__doc__ = "Version: "

    return f
