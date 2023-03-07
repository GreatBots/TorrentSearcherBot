import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

from config import START_MESSAGE

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, update):
    await update.reply(
        f"**Hi {update.chat.first_name}!**\n\n"
        "I am a simple torrent searcher bot. You can search torrent easily by using this bot.For more help @DevsChats")
