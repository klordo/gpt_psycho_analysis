import os

from dotenv import load_dotenv


load_dotenv()


class Configs:
    # bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")