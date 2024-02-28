![PyPI](https://img.shields.io/pypi/v/cgpt)
![python](https://img.shields.io/badge/Python-3.7-blue.svg)
![commit activity](https://img.shields.io/github/commit-activity/m/ainayves/cgpt?color=blue)
[![Build Status](https://img.shields.io/badge/Build%20status-Passing-green)](https://github.com/ainayves/cgpt/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<center><h1>🤖 MAKE AI POWERED SEARCH INSIDE YOUR CLI 💻</h1></center>
</br>

### ⭐ FEATURES

- [AI conversation exactly the same as in openai website](#description)
- [LAN support](#link-cgpt-inside-a-local-network)
- [Docker support](#whale2-run-with-docker)
- [Devbox support](#eject-run-with-devbox)

</br>

![cgpt1 1 28 (1)](https://user-images.githubusercontent.com/66997516/232239452-27e5c840-5699-44b8-bb28-da8d2dabc64f.gif)

</br>

### DESCRIPTIONS

- `cgpt` is a Python package that allows you to use AI directly in your favorite Terminal.
- `cgpt` is based on [CLICK](https://github.com/pallets/click) for creating beautiful command line interfaces in a composable way.

### :question: REQUIREMENTS

- python >=3.7
- openai API KEY :
  You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

### INSTALL FROM PYPI

You can install the latest version from pypi.

```
pip install cgpt
```

### 🚀 RUN

```
cgpt
```

### :link: CGPT INSIDE A LOCAL NETWORK

You can use cgpt inside a LAN.

- You just need one Host (`connected to internet`) to be the server.
- Other Hosts (`not connected to internet`) can ALWAYS use Chat GPT as `client`.

NOTES :

- For now , a server must be launched inside a `Linux` computer . If the server is inside `Windows` : the address is sometimes wrong (to be fixed in the next version).

- Also , make sure that your `/etc/hosts` is configured correctly like :

```
127.0.0.1	localhost
127.0.1.1	your-hostanme
```

- A `client` can also use his own api_key on future releases.

- This tool is still using `gpt-3.5-turbo` , `gpt-4` and `gpt-4-turbo` are on the way 😉.


### :whale2: RUN WITH DOCKER 

Pull the image 
```
# docker pull ainayves/cgpt:v1.2.6
```

Run the docker image by using your openai api key :

```
# docker run -e OPENAI_API_KEY="yourapikey" -i -t ainayves/cgpt
```

### :eject: RUN WITH DEVBOX

You need to install [Nix](https://nix.dev/install-nix.html) and [Devbox](https://www.jetpack.io/devbox) on the first place.

Then , run this command in the root directory :

```
devbox run start
```

### 💚 Feedback

Please feel free to leave feedback in issues/PRs.
