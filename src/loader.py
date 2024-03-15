from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from core import configs


bot = Bot(token=configs.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()