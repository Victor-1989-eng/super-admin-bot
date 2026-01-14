from aiogram.enums import ChatType

@router.message(lambda m: m.chat.type == ChatType.PRIVATE)
async def ignore_private(message: Message):
    await message.answer("🤖 Бот работает только в группах")

