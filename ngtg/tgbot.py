from django.conf import settings
from telebot.async_telebot import AsyncTeleBot
import asyncio

"""Import func sync_to_async"""
from asgiref.sync import sync_to_async

from ngtg.models import Profile

#  обьявление переменной бота
bot = AsyncTeleBot(settings.TELEGRAM_BOT_TOKEN)

@sync_to_async
def add_user_to_database(user_id, user_name, full_name):
    """Func to add user in DataBase"""
    p, created = Profile.objects.update_or_create(
        user_id=user_id,
        defaults={
            'user_name': user_name,
            'full_name': full_name

        }
    )
    return created

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    """Обработчик команды старт записывает в базу данные о новом профиле"""
    user_id = message.from_user.id
    user_name = message.from_user.username
    full_name = message.from_user.full_name

    if await add_user_to_database(user_id, user_name, full_name):
        await bot.send_message(message.chat.id, f'Привіт {message.from_user.first_name}, тебе додано до бази')
    else:
        await bot.send_message(message.chat.id, f'Привіт {message.from_user.first_name}, ти є у базі')
        
      






