from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SiderzBot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SesMusicAsistan")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "sohbetdestek")
PROJECT_NAME = getenv("PROJECT_NAME", "taliaMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/Mehmetbaba55")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))
LOG_GROUP = getenv("LOG_GROUP", None)


DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
