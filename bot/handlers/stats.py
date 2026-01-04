from aiogram import Router
from aiogram.types import CallbackQuery
from bot.database import get_chat

router = Router()

@router.callback_query(lambda c: c.data == "stats")
async def stats(call: CallbackQuery):
    chat = get_chat(call.message.chat.id)

    text = (
        "📊 Статистика\n\n"
        f"👥 Участников: (см. Telegram)\n"
        f"➕ Входы 24ч: {chat[4]}\n"
        f"➖ Выходы 24ч: {chat[5]}\n"
        f"💬 Сообщений: {chat[3]}"
    )

    await call.message.edit_text(text)
