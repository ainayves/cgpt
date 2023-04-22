import platform

VERSION = "1.2.2"
SUBTITLE = ">>> Make AI powered search inside your CLI"
os_name = platform.system()

WELCOME = f"""

  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$    
 /$$__  $$ /$$__  $$| $$__  $$|__  $$__/ v{VERSION}     
| $$  \__/| $$  \__/| $$  \ $$   | $$         
| $$      | $$ /$$$$| $$$$$$$/   | $$         
| $$      | $$|_  $$| $$____/    | $$         
| $$    $$| $$  \ $$| $$         | $$         
|  $$$$$$/|  $$$$$$/| $$         | $$         
 \______/  \______/ |__/         |__/ {SUBTITLE}

"""


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
color = "green"
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
PORT = "2048"
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
YOU_SERVER = f"Are you the server {HAPPY}?"
OPEN_TERMINAL = f"Please open another terminal..{RELEIVED}"
SERVER_LIVE = "Server live on "
GET_API_KEY = "Add your API key (invisible input) > "
API_KEY_ADDED = (
    "Your API key has been successfully added, please restart the cgpt command."
)
API_KEY_NOT_ADDED = "\nYou have not added an API key.\n"
SAY_SOMETHING = "Say something (q: quit, m: modify api_key) > "
ENTER_SERVER_IP = "Enter the server IP address: "
CONNECTION_LOST = f"Connection lost {SAD}"
CONNECTION_IMPOSSIBLE = f"Connection impossible {SAD}"
DASHED = "----------------------------------------------------------"
DAVINCI_MODEL = "gpt-3.5-turbo"
DAVINCI_PROMPT = "The following is a conversation with an AI. The AI is helpful, creative, clever, and very friendly.\n\nHuman:"
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
PYTHONSTR = "python"
PING = "PING"
PONG = "PONG"
