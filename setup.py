from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = 'cli-gpt',
    version = '0.0.1',
    author = 'Aina Yves',
    author_email = 'randrianaina.yves@gmail.com',
    license = 'MIT',
    description = 'Use openai chat-gpt on your cli',
    url = 'https://github.com/Aina15-DT/cli-gpt>',
    py_modules = ['cli_gpt', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cgpt=cli_gpt:cli
    '''
)