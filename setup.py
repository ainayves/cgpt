from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = 'cgpt',
    version = '0.0.4',
    author = 'Aina Yves',
    author_email = 'randrianaina.yves@gmail.com',
    license = 'MIT',
    description = 'Use openai chat-gpt on your cli',
    long_description='cgpt is a Python module that allows you to use Chat-GPT directly in your Terminal. \n\n 🔨 REQUIREMENTS \n python >=3.7 \n\n 🚀 RUN test version \n $ cgpt tellme',
    url = 'https://github.com/Aina15-DT/cli-gpt>',
    py_modules = ['cli_gpt', 'app'],
    packages = find_packages(),
    install_requires = ['aiohttp',
                        'aiosignal',
                        'async-timeout',
                        'attrs',
                        'bleach',
                        'certifi',
                        'cffi',
                        'charset-normalizer',
                        'click',
                        'cryptography',
                        'docutils',
                        'frozenlist',
                        'idna',
                        'importlib-metadata',
                        'importlib-resources',
                        'jaraco.classes',
                        'jeepney',
                        'keyring',
                        'markdown-it-py',
                        'mdurl',
                        'more-itertools',
                        'multidict',
                        'openai',
                        'pkginfo',
                        'pycparser',
                        'Pygments',
                        'python-dotenv',
                        'readme-renderer',
                        'requests',
                        'requests-toolbelt',
                        'rfc3986',
                        'rich',
                        'SecretStorage',
                        'six',
                        'tqdm',
                        'twine',
                        'typing_extensions',
                        'urllib3',
                        'webencodings',
                        'yarl',
                        'zipp',],
                        
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cgpt=cgpt:cli
    '''
)