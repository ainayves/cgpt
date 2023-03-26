import platform

os_name = platform.system()

if os_name == "Linux" or os_name == "Darwin":
    IA = "🤖"
    HAPPY = "😃"
    RELEIVED = "😌"
    SAD = "😥"
else:
    IA = ""
    HAPPY = ""
    RELEIVED = ""
    SAD = ""

init_conversation = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

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
MESSAGE = "message"
CONTENT = "content"
STR_OPENAI_API_KEY = "OPENAI_API_KEY"
SERVER_PATH = "/app/server/main.py"
CLIENT_PATH = "/app/client/main.py"
CGPT_NETWORK = "--> Voulez-vous utiliser cgpt en réseaux ?"
YOU_SERVER = f"---> Êtes vous le serveur {HAPPY} ?"
OPEN_TERMINAL = f"----> Veuillez ouvrir un autre terminal..{RELEIVED}"
SERVER_LIVE = "Serveur live sur "
GET_API_KEY = "Ajoutez votre api key (invisible input) >"
API_KEY_ADDED = "Votre API KEY a bien été ajouté , veuillez relancer la commande `cgpt tellme` "
API_KEY_NOT_ADDED = "\n Vous n' avez pas ajouter un API KEY \n"
SAY_SOMETHING = " Dîtes quelque chose (q : quitter , m : modifier api_key ) > "
ENTER_SERVER_IP = "Entrez l' adresse IP du serveur "
CONNECTION_LOST = f"Connexion perdue {SAD}" 
CONNECTION_IMPOSSIBLE = f"Connexion impossible {SAD}"
DASHED = "----------------------------------------------------------"
DAVINCI_MODEL = "gpt-3.5-turbo"
DAVINCI_PROMPT = "The following is a conversation with an AI. The AI is helpful, creative, clever, and very friendly.\n\nHuman:"
INCORRECT_API_KEY = "Votre API KEY est incorrect, tapez `m` pour modifer le key , ou `q` pour quitter > "
OPENAI_REQUEST_TIMEOUT = "IA endormie"
NOT_CONNECTED = "Vous êtes déconnecté d' internet .."
TOO_MUCH_REQUEST = "Trop de requête"
