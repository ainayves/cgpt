# -*- coding: utf-8 -*-

from setuptools import setup
from app.utils.constant import VERSION

with open("pypi_desc.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="cgpt",
    version=VERSION,
    author="Aina Yves",
    author_email="randrianaina.yves@gmail.com",
    license="MIT",
    description="Use openai chat-gpt on your cli",
    long_description=long_desc,
    url="https://github.com/ainayves/cgpt>",
    long_description_content_type="text/markdown",
    py_modules=["cgpt", "app"],
    packages=["app", "app.client", "app.server", "app.utils", "app.commands"],
    install_requires=[
        "setuptools",
        "twine",
        "click>=7.1.2",
        "openai",
        "python-dotenv",
        "termcolor"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["cgpt=cgpt:cgpt", "cgpt-version=app.commands.main:version"]
    },
)
