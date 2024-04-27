import asyncio
import os
from pyrogram.types import CallbackQuery
from AarohiX import  (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command("الاوامر")
)
async def mixthon(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7308dda897f0cda0eafa3.jpg",
        caption=f"""**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس mixthon \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**mixthon music**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯", url=f"https://t.me/mixthon"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def mixthon_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**
اهلا بك في الأوامر اوامر التشغيل والتحميل 
~ اليك | اوامر المستخدمين

~ تشغيل - لتشغيل ملف صوتي في القنوات
~ يوت - تنزيل ملف صوتي من اليوتيوب 
~ الصاعدين - اضهار الموجودين في المكالمة
~ فيديو - تنزيل فيديو من اليوتيوب الجديد
~ ايقاف - ايقاف الملف الصوتي المشغل الجديد
~ سكب - تخطي الملف الصوتي المشغل الجديد
~ تكرار - عمل تكرار الى الملف الصوتي المشغل
~ عشوائي - تشغيل الطابور عشوائياً المكالمة
بنترست للتحميل مجموعة صور من بنترست وأرسالها
المزيد من المميزات قريباً
- يرجى دخول قناة السورس لمتابعة التحديثات ✓ . 


**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def mixthon_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**
اوامر القنوات  

~ تشغيل - لتشغيل ملف صوتي في القنوات
~ ايقاف - ايقاف الملف الصوتي المشغل الجديد
~ سكب - تخطي الملف الصوتي المشغل الجديد
~ تكرار - عمل تكرار الى الملف الصوتي المشغل
~ عشوائي - تشغيل الطابور عشوائياً المكالمة

- يرجى دخول قناة السورس لمتابعة التحديثات ✓ .

**⩹𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def mixthon_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**𓏺َِmixthon**
★¦ اهلا بك عزيزي في قسم اوامر المجموعة
/تثبيت لتثبيت رسالة في المجموعة
/الغاء تثبيت لمسح الرسالة المثبتة
/وضع صورة بالرد لوضع صورة للمجموعة
`حذف الصورة` لحذف صورة المجموعة
/وضع وصف لوضع وصف للمجموعة



**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def mixthon_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/7308dda897f0cda0eafa3.jpg",
        caption=f"""**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس mixthon \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𝐌𝐈𝐗𝐓𝐇𝐎𝐍 𝐂𝐌𝐃 ⌯", url=f"https://t.me/mixthon"),
                ],

            ]

        ),

    )
