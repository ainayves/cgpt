![PyPI](https://img.shields.io/pypi/v/cgpt)
![python](https://img.shields.io/badge/Python-3.7-blue.svg)
![commit activity](https://img.shields.io/github/commit-activity/m/ainayves/cgpt?color=blue)
[![Build Status](https://img.shields.io/badge/Build%20status-Passing-green)](https://github.com/ainayves/cgpt/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<center><h2>🤖 MAKE AI POWERED SEARCH INSIDE YOUR CLI 💻</h2></center>
</br>

# ⭐ FEATURES

- [AI conversation exactly the same as in openai website](#descriptions)
- [LAN support](#cgpt-inside-a-local-network)
- [Devbox support](#whale2-run-with-docker)
- [Docker support](#whale2-run-with-docker)

</br>

![cgpt](https://i.imgflip.com/8hdiuv.jpg)

</br>

### DESCRIPTIONS

- `cgpt` is a REPL that allows you to use AI directly in your favorite Terminal.
- `cgpt` is based on [CLICK](https://github.com/pallets/click) for creating beautiful command line interfaces in a composable way.

### :question: PREREQUISITES

- python >=3.7
- openai API KEY :
  You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

  > This tool is still using `gpt-3.5-turbo` , 
  > `gpt-4` and `gpt-4-turbo` are on the way. 😉

### INSTALL FROM PYPI

You can install the latest version from pypi.

```
pip install cgpt
```

# 🚀 RUN

```
cgpt
```

### :link: CGPT INSIDE A LOCAL NETWORK

You can use cgpt inside a LAN.

- You just need one Host (`connected to internet`) to be the server.
- Other Hosts (`not connected to internet`) can ALWAYS use Chat GPT as `client`.

> For more information , look [here](https://cgpt.readthedocs.io/en/latest/index.html#use-it-inside-a-local-network).

### ⏏️ RUN WITH DEVBOX

For contributors , you need to install [Devbox](https://www.jetpack.io/devbox/docs/installing_devbox/) if you do not have it yet.

Then , run this command in the root directory of the project:

```
devbox run start
```

### :whale2: RUN WITH DOCKER 

Pull the image 
```
# docker pull ainayves/cgpt:latest
```

Run the docker image by using your openai [api_key](https://platform.openai.com/account/api-keys) :

```
# docker run -e OPENAI_API_KEY="yourapikey" -i -t ainayves/cgpt
```

# 💚 Feedback

Please feel free to leave feedback in issues/PRs.
