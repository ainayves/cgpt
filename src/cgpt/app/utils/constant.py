import platform

VERSION = "1.2.11"
SUBTITLE = ">>> Make AI powered search inside your CLI"
os_name = platform.system()
APIKEY_OPTION = "Modify API key."
VERSION_OPTION = "Show version of cgpt."
LAN_OPTION = "Use LAN mode, share your connection to AI with people in the network."

WELCOME = (
    "    "
    + "\n"
    + f""" 
   █████████    █████████  ███████████  ███████████ v{VERSION} by Aina Yves
  ███░░░░░███  ███░░░░░███░░███░░░░░███░█░░░███░░░█
 ███     ░░░  ███     ░░░  ░███    ░███░   ░███  ░ 
░███         ░███          ░██████████     ░███    
░███         ░███    █████ ░███░░░░░░      ░███    
░░███     ███░░███  ░░███  ░███            ░███    
 ░░█████████  ░░█████████  █████           █████   
  ░░░░░░░░░    ░░░░░░░░░  ░░░░░           ░░░░░    

    {SUBTITLE}
    
    q: quit, m: modify api_key
"""
)

if os_name == "Linux" or os_name == "Darwin":
    IA = "🤖"
    HAPPY = "😃"
    RELEIVED = "😌"
    SAD = "😥"
    NO_ENTRY = "🚫"
    LIVE = "✨"
else:
    IA = "IA"
    HAPPY = ""
    RELEIVED = ""
    SAD = ""
    NO_ENTRY = ""
    LIVE = ""

init_conversation = [{"role": "system", "content": "You are a helpful assistant."}]
BYE = f"\n Bye ! {SAD}"
color = "cyan"
error_color = "yellow"
assistant_color = "yellow"
top_left = "╭"
top_right = "╮"
bottom_left = "╰"
bottom_right = "╯"
stick = "│"
BLANK = "\n"
TEMPERATURE = 0.9
MAX_TOKENS = 200
TOP_P = 1.0
FREQUENCY_P = 0.0
PRESENCE_P = 0.6
PORT = 2048
UTF = "UTF-8"
BEGIN = "begin"
HUMAN = " Human:"
USER = "user"
ASSISTANT = "assistant"
AI_COLON = "AI:"
AI_COLON_SPACE = " AI:"
CHOICES = "choices"
TEXT = "text"
MAX_WIDTH = 100
MESSAGE = "message"
CONTENT = "content"
STR_OPENAI_API_KEY = "OPENAI_API_KEY"
SERVER_PATH = "/app/server/main.py"
CLIENT_PATH = "/app/client/main.py"
CGPT_NETWORK = "Do you want to use cgpt on networks? "
YOU_SERVER = f"You are using the LAN mode...\nAre you the server {HAPPY} ?"
OPEN_TERMINAL = f"Please open another terminal..{RELEIVED}"
SERVER_LIVE = "Server live on "
GET_API_KEY = "Add your API key (invisible input) > "
API_KEY_ADDED = (
    "Your API key has been successfully added, please restart the cgpt command."
)
API_KEY_NOT_ADDED = "\nYou did not add an API key.\n"
SAY_SOMETHING = "    Say something > "
ENTER_SERVER_IP = "Enter the server IP address: "
CONNECTION_LOST = f"Connection lost {SAD}"
CONNECTION_IMPOSSIBLE = f"Connection impossible {SAD}"
DASHED = "----------------------------------------------------------"
CHOOSE_MODEL = "Show current model or , choose another one"
MODEL_ERROR = f"Too bad you can't access the selected Model {SAD} , Type cgpt -m to use another one {RELEIVED}"
MODEL_USED = "You are currently using : "
CHOOSE_OTHERS = "You can choose another one if you want : "
YOU_SELECTED = "You selected : "
MODELS_LIST = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]
MODEL = "OPENAI_MODEL"
DAVINCI_MODEL = "gpt-3.5-turbo"
DAVINCI_PROMPT = "The following is a conversation with an AI. The AI is helpful, creative, clever, and very friendly.\n\nHuman:"  # noqa: E501
INCORRECT_API_KEY = (
    "Your API key is incorrect. Type m to modify the key or q to quit > "
)
OPENAI_REQUEST_TIMEOUT = "AI is asleep"
NOT_CONNECTED = "You are not connected to the internet.."
TOO_MUCH_REQUEST = "Too many requests"
CONNECTION_ERROR = "Connection error: "
ADDRESS_NOT_VALID = f"The IP address is not valid {NO_ENTRY}"
DECONNECTED_HOST = "A host has disconnected."
BOLD = "bold"
PYTHONSTR = "python3"
PING = "PING"
PONG = "PONG"
