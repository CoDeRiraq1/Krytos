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

txt1 = [

            "**ها تاج راسي**",


             "**ها حياتي شغال انه **",
            

            "**ها أستاذي الكريم **",
            
            
           
            
            
 
            
            

        ]


        
        


@app.on_message(command(["بوت"]))
