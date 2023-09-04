from django.conf import settings
from telebot.async_telebot import AsyncTeleBot
import asyncio

"""Import func sync_to_async"""
from asgiref.sync import sync_to_async

from ngtg.models import Profile

#  обьявление переменной бота
bot = AsyncTeleBot(settings.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')







