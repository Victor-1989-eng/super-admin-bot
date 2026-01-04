from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def moderation_kb(user_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔇 10 мин", callback_data=f"mute_10_{user_id}")],
        [InlineKeyboardButton("🔇 1 час", callback_data=f"mute_60_{user_id}")],
        [InlineKeyboardButton("🔇 24 часа", callback_data=f"mute_1440_{user_id}")],
        [InlineKeyboardButton("🔨 Ban", callback_data=f"ban_{user_id}")]
    ])
