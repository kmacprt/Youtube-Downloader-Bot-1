from datetime import datetime, timedelta
from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
from bot import user_time
from config import youtube_next_fetch
from helper.ytdlfunc import extractYt, create_buttons

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"


@Client.on_message(Filters.regex(ytregex))
async def ytdl(_, message):
    userLastDownloadTime = user_time.get(message.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await message.reply_text(f"`Wait {wait_time} Minutes before next Request`")
            return
    except:
        pass

    url = message.text.strip()
    await message.reply_chat_action("typing")
    try:
        title, thumbnail_url, formats = extractYt(url)

        now = datetime.now()
        user_time[message.chat.id] = now + \
                                     timedelta(minutes=youtube_next_fetch)

    except Exception:
        await message.reply_text("`යූ ටියුබ් දත්ත ලබා ගැනීමට අපොහොසත් විය ... 😔 \nටියුබ් අවහිර කළ සේවාදායකය ip \n#error`")
        return
    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    sentm = await message.reply_text("යූටියුබ් යූආර්එල් සැකසීම ◾️◾️◾️◾️👀")
    try:
        # Todo add webp image support in thumbnail by default not supported by pyrogram
        # https://www.youtube.com/watch?v=lTTajzrSkCw
        await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        await sentm.delete()
    except Exception as e:
        try:
            thumbnail_url = "https://telegra.ph/file/44706b57abb809b53c68d.png"
            await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")

