import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    chat_id INTEGER PRIMARY KEY,
    antispam INTEGER DEFAULT 1,
    welcome INTEGER DEFAULT 1,
    messages_24h INTEGER DEFAULT 0,
    joins_24h INTEGER DEFAULT 0,
    leaves_24h INTEGER DEFAULT 0
)
""")

conn.commit()


def get_chat(chat_id: int):
    cursor.execute("SELECT * FROM chats WHERE chat_id=?", (chat_id,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("INSERT INTO chats(chat_id) VALUES(?)", (chat_id,))
        conn.commit()
        return get_chat(chat_id)
    return row


def toggle(chat_id: int, field: str):
    cursor.execute(f"UPDATE chats SET {field}=1-{field} WHERE chat_id=?", (chat_id,))
    conn.commit()
