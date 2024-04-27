import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
from config import OWNER_ID



txt = [

            "كول حبيبي بخدمتك ",


             "ها سيد",
            

            "اسمي  محاسن",
            
            
            "والله ماكو بوت غيرك",
            
            
            "حب دز `الاوامر` ويطلعلك كلشي",
            
            
             "هلا گلبي گول",
            
            
 
            
            

        ]

txt1 = [

            "**ها تاج راسي**",


             "**ها حياتي شغال انه **",
            

            "**ها أستاذي الكريم **",
            
            
           
            
            
 
            
            

        ]


        
        


@app.on_message(command(["بوت"]))


async def cutt(client: Client, message: Message):
     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(


         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}"
