import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH","")
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    SESSION_NAME = "NXTBOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")


