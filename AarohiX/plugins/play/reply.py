import asyncio
import random
from AarohiX import app
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




@app.on_message(command(["بوت"]))

async def ktbat(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}
