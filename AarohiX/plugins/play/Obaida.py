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
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
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



@app.on_message(command(["غنيلي", "غني", "غ", "ميكسثون غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
