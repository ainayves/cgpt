![python](https://img.shields.io/badge/Python-3.7-blue.svg)
![commit activity](https://img.shields.io/github/commit-activity/m/ainayves/cgpt?color=blue)
[![Build Status](https://img.shields.io/badge/Build%20status-Passing-green)](https://github.com/ainayves/cgpt/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<center><h1>🌟 MAKE AI POWERED SEARCH INSIDE YOUR CLI 🌟</h1></center>
</br>

![cgpt1 1 28 (1)](https://user-images.githubusercontent.com/66997516/232239452-27e5c840-5699-44b8-bb28-da8d2dabc64f.gif)

</br>

`cgpt` is a Python module that allows you to use Chat-GPT directly in your favorite Terminal.

### ❓ REQUIREMENTS

- python >=3.7
- openai API KEY : 
You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

### 💻 SETUP

```
pip install -r requirements.txt
```

### 🔨 BUILD

- For this part , it is better to use Linux.

If you are on Linux , launch:

```
sudo chmod +x build.sh
```
Then , :

```
./build.sh
```

### ⏯️ GET VERSION 

```
cgpt-version
```

### 🚀 RUN

```
cgpt
```

### 🔗 CGPT INSIDE A LOCAL NETWORK

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

- A `client` can also use his own api_key in the next version.

### 💚 Feedback

Please feel free to leave feedback in issues/PRs.
