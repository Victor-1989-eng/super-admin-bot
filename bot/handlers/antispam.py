from aiogram import Router
from aiogram.types import Message
from aiogram.enums import ChatType
from time import time

from bot.database import get_chat

router = Router()
user_last_message = {}


@router.message()
async def antispam_handler(message: Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    chat = get_chat(message.chat.id)
    antispam_enabled = chat[1]

    if not antispam_enabled:
        return

    # ссылки
    if message.text and ("http://" in message.text or "https://" in message.text):
        await message.delete()
        return

    # антифлуд
    uid = message.from_user.id
    now = time()

    if uid in user_last_message and now - user_last_message[uid] < 1.2:
        await message.delete()
        return

    user_last_message[uid] = now
