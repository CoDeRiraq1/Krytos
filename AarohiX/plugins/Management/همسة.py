@app.on_message(
    command(["همسة", همسه", اهمس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**اضغط على الزر لكتابة همسة ⭐**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "اهمس ❤️‍🔥", url=f" https://t.me/mixthon/8")
                ],   [
                    InlineKeyboardButton(
                        "تمويل قنوات", url=f"https://t.me/V_64_V"),                        
                 ],
            ]
        ),
                             )
