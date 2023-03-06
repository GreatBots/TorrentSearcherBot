from pyrogram import Client, filters
from pyrogram.types import Message

from config import START_MESSAGE

@Client.on_message(pyrogram.Filters.command("start"))
def start(client, message):
    message.reply(START_MESSAGE)
