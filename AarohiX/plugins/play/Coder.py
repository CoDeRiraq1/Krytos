#copyrighted mixton Source Channel @mixthon
import asyncio

import random

from AarohiX import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)

from strings.filters import command

from pyrogram import filters, Client





txt = [

"‏عيب؟ ",
"‏قليل أدب 🙂",
"‏ ‏ ممنوع! ",
"‏ ‏أستحي شوي ! ",
"‏ لا تعيدهااا! ",
"‏ليش ما تتأدب؟ ",
"‏ اشششششش",
"راح تنطرد!",
"!!!!",
"اذا ما تتأدب اطردك",
"ناوي تاخذ كتم!",


        ]


        


@app.on_message(command(["كسمك" ,"كسختك"]))

async def ktbat(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
