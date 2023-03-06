from pyrogram import Client, filters
from pyrogram.types import Message

from config import START_MESSAGE

@Client.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I can help you to search torrent in telegram.\n\nyou van easily search torrent usingthis bot)
