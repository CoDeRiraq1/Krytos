from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app 

@app.on_message(filters.command("Whats"))
async def generate_whatsapp_link(client, message: Message):
    if len(message.command) < 2:
        await message.reply("ارسل رقم الهاتف مع الأمر. الأستخدام: /Whats +1234567890")
        return

    phone_number = message.command[1]

    whatsapp_link = f"https://wa.me/{phone_number}"

    await message.reply(f"اضغط على الرابط لمراسة  {phone_number}:\n{whatsapp_link}")
