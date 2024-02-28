![PyPI](https://img.shields.io/pypi/v/cgpt)
![python](https://img.shields.io/badge/Python-3.7-blue.svg)
![commit activity](https://img.shields.io/github/commit-activity/m/ainayves/cgpt?color=blue)
[![Build Status](https://img.shields.io/badge/Build%20status-Passing-green)](https://github.com/ainayves/cgpt/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<center><h2>🤖 MAKE AI POWERED SEARCH INSIDE YOUR CLI 💻</h2></center>
</br>

# Features

- [AI conversation exactly the same as in openai website](#descriptions)
- [LAN support](#cgpt-inside-a-local-network)
- [Docker support](#run-with-docker)
- [Devbox support](#devbox-support)

</br>

![cgpt](https://i.imgflip.com/8hdiuv.jpg)

</br>

## Descriptions

- `cgpt` is a REPL that allows you to use AI directly in your favorite Terminal.
- `cgpt` is based on [CLICK](https://github.com/pallets/click) for creating beautiful command line interfaces in a composable way.

## Prerequisities

- python >=3.7
- openai API KEY :
  You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

  > This tool is still using `gpt-3.5-turbo` , 
  > `gpt-4` and `gpt-4-turbo` are on the way. 😉

# Setup and Run

### 🚀 Run in local

You can directly install the latest version from pypi.

```
pip install cgpt
```

```
$ cgpt
```

### CGPT inside a Local Area Network

You can use cgpt inside a LAN.

- You just need one Host (`connected to internet`) to be the server.
- Other Hosts (`not connected to internet`) can ALWAYS use Chat GPT as `client`.

> For more information , look [here](https://cgpt.readthedocs.io/en/latest/index.html#use-it-inside-a-local-network).


### Run with Docker 

Pull the image 
```
$ docker pull ainayves/cgpt:latest
```

Run the docker image by using your openai [api_key](https://platform.openai.com/account/api-keys) :

```
$ docker run -e OPENAI_API_KEY="yourapikey" -i -t ainayves/cgpt
```

# Devbox support

To make life easier for contributors , you can install and use [Devbox](https://www.jetpack.io/devbox/docs/installing_devbox/).

Then , run this command in the root directory of the project:

```
$ devbox run start
```

# 💚 Feedback

Please feel free to leave feedback in issues/PRs.
