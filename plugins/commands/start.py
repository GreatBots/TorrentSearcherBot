from pyrogram import Client, filters
from pyrogram.types import Message

from config import START_MESSAGE

@Client.on_message(filters.command("start"))
async def start_message(Client, Message):
await message.reply_text(
    text=START_MESSAGE,
    reply_markup=InlineKeyboardMarkup(
      [
        InlineKeyboardMarkup("Updates", url="https://t.me/myownbots")
      ]
    )
)
