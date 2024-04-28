
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint
@app.on_message(
    command(["المطور", "سورس", "السورس", "سورس ميكسثون",  "ميكسثون"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7308dda897f0cda0eafa3.jpg",
        caption=f"""
  - 𓏺[𝙎𝙊𝙐𝙍𝘾𝙀 𝐌𝐢𝐱𝐭𝐡𝐨𝐧](https://t.me/mixthon) 
—————————————
-   [𝙗𝙤𝙩 𝙘𝙝𝙖𝙩 ](https://t.me/Mixthon) 

-  [𝙨𝙤𝙪𝙧𝙘𝙚 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧](https://t.me/AA37A) 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " أبو عُبَيْدَةْ ", url=f"https://t.me/AA37A"), 
                ],[
                    InlineKeyboardButton(
                        "𝐌𝐢𝐱𝐭𝐡𝐢𝐧 𝐂𝐌𝐃 𝐒𝐎𝐔𝐑𝐂𝐄", url=f"t.me/Mixthon"),
                ],

            ]

        ),

    )




    )
