![](https://komarev.com/ghpvc/?username=ainayves&color=blueviolet)

## Use openai chat-gpt on your CLI
`cgpt` is a Python module that allows you to use Chat-GPT directly in your favorite Terminal.

### REQUIREMENTS

- python >=3.7
- openai API KEY : 

You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

### SETUP

```
pip install cgpt
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

### 🐋 RUN INSIDE DOCKER

```
docker-compose run --rm app
```

### GITHUB

- [cgpt](https://github.com/ainayves/cgpt/)
