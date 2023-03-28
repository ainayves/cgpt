![](https://komarev.com/ghpvc/?username=ainayves&color=blueviolet)

## Use openai chat-gpt inside your cli
</br>

https://user-images.githubusercontent.com/66997516/228263166-01828e31-3bc1-46b9-ad37-9d44ca117d7f.mp4

</br>

`cgpt` is a Python module that allows you to use Chat-GPT directly in your Terminal.

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
- Create a build.sh file , copy - paste the content of build.sh.example.

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

### 🔗 CGPT INSIDE A LOCAL NETWORK

You can use cgpt inside a LAN. 

- You just need one Host (`connected to internet`) to be the server.
- Other Hosts (`not connected to internet`) can ALWAYS use Chat GPT as `client`. 

NOTES : 

- For now , a server must be launched inside a `Linux` computer . If the server is inside `Windows` : the address is sometimes wrong (to be fixed in the next version). 
- A `client` can also use his own api_key in the next version.

### 💚 Feedback

Please feel free to leave feedback in issues/PRs.
