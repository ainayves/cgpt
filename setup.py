from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = 'cgpt',
    version = '0.0.16',
    author = 'Aina Yves',
    author_email = 'randrianaina.yves@gmail.com',
    license = 'MIT',
    description = 'Use openai chat-gpt on your cli',
    long_description='cgpt is a Python module that allows you to use Chat-GPT directly in your Terminal. \n\n 🔨 REQUIREMENTS \n python >=3.7 \n\n 🚀 RUN test version \n $ cgpt tellme',
    url = 'https://github.com/Aina15-DT/cli-gpt>',
    py_modules = ['cgpt','app'],
    packages = find_packages(),
    install_requires = ['setuptools',
                        'twine',
                        'click>=7.1.2',
                        'openai',
                        'python-dotenv'],
                        
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