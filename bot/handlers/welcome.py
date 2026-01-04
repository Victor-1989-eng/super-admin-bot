import asyncio
from aiogram import Router
from aiogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from bot.database import get_chat

router = Router()
pending = {}


@router.chat_member()
async def welcome(event: ChatMemberUpdated):
    if event.new_chat_member.status != "member":
        return

    chat = get_chat(event.chat.id)
    if not chat[2]:
        return

    user = event.from_user

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Я не бот", callback_data=f"human_{user.id}")]
    ])

    msg = await event.bot.send_message(
        event.chat.id,
        f"👋 {user.full_name}, нажмите кнопку, чтобы подтвердить вход",
        reply_markup=kb
    )

    pending[user.id] = msg.message_id

    await asyncio.sleep(60)

    if user.id in pending:
        await event.bot.restrict_chat_member(
            event.chat.id,
            user.id,
            permissions={}
        )
        pending.pop(user.id, None)
