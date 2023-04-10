from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
from pyowm import OWM

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
owm = OWM(api_key=getenv('OWM'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
