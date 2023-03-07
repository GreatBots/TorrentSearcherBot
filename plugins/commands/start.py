import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

from config import START_MESSAGE

@Client.on_message(pyrogram.filters.command("start"))
def start(client, message):
    message.reply("Hi! I'm a Torrent Search Bot for search torrent.I can upload torrent to telegram", reply_messages_id=message.id)
