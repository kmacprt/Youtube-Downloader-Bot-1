from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"🤕දැනට සහය දක්වන්නේ යූටියුබ් සිංගල් සඳහා පමණි (ධාවන ලැයිස්තුවක් නැත🤭) යූටියුබ් යූආර්එල් යවන්න"
    await message.reply_text(helptxt)
