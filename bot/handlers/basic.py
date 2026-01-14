from aiogram import Router
from aiogram.types import Message
from aiogram.enums import ChatType

router = Router()  # 🔥 ВОТ ЭТОГО НЕ ХВАТАЛО

@router.message(lambda m: m.chat.type == ChatType.PRIVATE)
async def ignore_private(message: Message):
    await message.answer("🤖 Бот работает только в группах")


