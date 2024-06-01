import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from AarohiX import app
from AarohiX.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
import config                                       



@app.on_message( 
command("اوامري")
)
@app.on_callback_query(filters.regex("obidaback"))
async def obidaback(_, query: CallbackQuery):
   await query.send_message_text(
       f"""<b>» مرحبـاً بك عـزيـزي </b> .\n\n<b>» استخـدم الازرار بالاسفـل 𝄞\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="obidall"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="obidach"),
                    InlineKeyboardButton(
                        "• اوامـر البوت •", callback_data="obidaad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="obidadv"),
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("obidadv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبـاً بك عـزيـزي المطـور </b>\n\n<b>» استخـدم الازرار بالاسفـل 𝄞\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• التحـديث •", callback_data="obidaup"),
                ],[
                    InlineKeyboardButton(
                        "• الـرفــع •", callback_data="obidasu"),
                    InlineKeyboardButton(
                        "• الـحظــر •", callback_data="obidabn"),
                ],[
                    InlineKeyboardButton(
                        "• الاشعــارات & المسـاعــد •", callback_data="obidaas"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidaback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("obidall"))
async def obidall(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر الـتشغـيـل :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم الاغنية / رابط الاغنية)
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

بحث + الاسـم  او يوت  + الاسم
<b>- لـ تحميـل الاغانـي والمقـاطـع الصوتيـه مـن اليوتيـوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidaback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("obidaad"))
async def obidaad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر  البوت :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

الاعدادات
<b>- لـ عـرض إعـدادات اوضـاع التشغيـل</b>

ايقاف / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / استئناف
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي / التالي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>

/الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>

`/bin  + الرقم`
<b>- لعرض معلومات الـ bin   </b>
/gen + bin number 
<b>- لتوليد مجموعة فيزات عن طريق الـ bin \nللحصول على Bin t.me/mixthon/47 </b>
كت
<b> لعبة كت تويت الشهيرة- </b>







الادمنيه
<b>- لـ عـرض قائمـة ادمنيـة البـوت</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عـدد الثـوانـي
<b>- لـ تقديـم الاغنيـه لـ الامـام</b>
/seekback + عـدد الثـوانـي
<b>- لـ إرجـاع الاغنيـه لـ الخـلف</b>
تاك
<b>-  لعمل تاك لجميع اعضلء المجموعة</b>
الرابط 
<b>- لـ ارسال رابط المجموعة </b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidaback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("obidach"))
async def obidach(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر التشغيــل فـي القنــاة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل المكالمه</b>
<b>- انشاء مجموعه وارفع البوت اشراف</b>
<b>- ارسـل في المجموعه (/channelplay او /ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الاوامــر بالاسفـل بالمجموعه لـ التشغيـل</b>
<b>- "استخدم الاوامر بـ / او بدون"</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
cplay + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

cvplay + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

cstop
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

cpause
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

cresume
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

cskip
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidaback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("obidaup") & SUDOERS)
async def obidaup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر التحـديثـات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

/السجلات
<b>- لـ جلب سجـلات البـوت 📋</b>

/تحديث
<b>- لـ تحديـث البــوت</b>

/اعاده تشغيل
<b>- لـ اعـادة تشغيـل البــوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidadv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("obidasu") & SUDOERS)
async def obidasu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرفــع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>ملاحظه :- استخدم "/" قبل الامر</b>

رفع مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي ميـوزك البـوت</b>

المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidadv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("obidabn") & SUDOERS)
async def obidabn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الحظــر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>ملاحظه :- استخدم "/" قبل الامر</b>

حظر/الغاء الحظر
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت</b>

المحظورين
<b>- لـ عـرض قائمـة المحظورين</b>

حظر عام/الغاء حظر عام
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت عـام</b>

المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>

حظر مجموعة/سماح
<b>- لـ حظـر/الغـاء حظـر مجموعـة من استخـدام ميـوزك البـوت</b>

المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidadv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("obidaas") & SUDOERS)
async def obidaas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- لـ تفعيـل/تعطيـل اشعـارات مجموعـة سجـل البــوت</b>

مغادره تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل المغـادره التلقائيـه لـ الحسـاب المسـاعـد مـن المجمـوعـات عنـد عـدم استـخـدام الميـوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="obidadv"),
               ],
          ]
        ),
)
