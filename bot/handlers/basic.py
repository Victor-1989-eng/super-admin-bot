from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def ignore_private(message: Message):
    if message.chat.type == "private":
        await message.answer("🤖 Бот работает только в группах")
