import asyncio

import random

from AarohiX import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)

from strings.filters import command

from pyrogram import filters, Client





txt = [

"‏عيون البوت",
"‏ها سيد",
"‏ ‏ ها حبي ",
"‏ ‏شتريد مني؟ ",
"‏ هلا حبيبي ",
"‏صاعد اتصال وية الحب ",
"‏ امر خدمة سيد",
"‏دز `الاوامر` وشوف شسوي بمكان مجاي تصيح بوت دوختني",
"‏ :عوفني بربك ضايج كلش .",
"‏ : مو بوت 🙂 .",
"‏ ‏: مفارغلك هسة?",
"صدك لعبة العراق والأردن راح يعيدوها",
"‏ اكلك انته برشلوني ",
"‏ علضحكة نحسدنة وهي بس صوت",
"‏ وجت وجت.",
"‏ ‏قسيت اني وچنت مجبور
ابينلك الحب هين
ردودك علمتني الـ ألم بس ينعاش
ما مسموحلة يبين ..",
"‏ليهسه مَعزتك باقيه بروحي 
لا راحت ولا قلت 
مَعزتك تشبه جروحي.",
"‏ هل كانت كل الطرق تؤدي إليكِ، أم أنني كنتُ أجعلها كذلك.",
"‏ ‏هففف اطلع من راسي.",
"‏ ها حبيبي انت",
"‏ ها حياتي انت",
"‏ ها ",
"‏ أنعم .",


        ]


        


@app.on_message(command(["كتبات","حكمه"]))

async def ktbat(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
