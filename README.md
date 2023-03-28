![](https://visitor-badge.glitch.me/badge?page_id=Aina15-DT.cli-gpt)

## Use openai chat-gpt on your cli
cgpt is a Python module that allows you to use Chat-GPT directly in your Terminal.

### ❓ REQUIREMENTS

- python >=3.7
- openai API KEY : 
You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

### 💻 SETUP

```
pip install -r requirements.txt
```

### 🔨 BUILD

Create a build.sh file , copy - paste the content of build.sh.example 

If you are on Linux , launch:

```
sudo chmod +x build.sh
```
Then , :

```
./build.sh
```


### 🚀 RUN

```
cgpt tellme
```

### 🌞 NEW FEATURE : CGPT INSIDE A LOCAL NETWORK

Now , you can use cgpt inside a LAN. 

- You just need one Host (`connected to internet`) to be the server, and other Hosts (`not connected to internet`) can ALWAYS use Chat GPT.  

- NOTE : For now , a server must be launched inside a Linux computer . If the server is inside Windows , the serving address is sometimes wrong (TODO for the next release)

### 💚 Feedback

Please feel free to leave feedback in issues/PRs.
