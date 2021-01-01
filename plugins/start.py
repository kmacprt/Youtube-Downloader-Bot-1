from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔔 නාළිකාව", url="https://t.me/lkhitech")],
        [InlineKeyboardButton(
            "😊සම්බන්ධ කරගන්න ", url="https://t.me/kavinduaj")]
        [InlineKeyboardButton(
            "🖥 ප්‍රවේශ වන්න 😊", url="https://visi.tk/kavinduaj")]
    ])
    welcomed = f"ආයුබෝවාන්🙏<b>{message.from_user.first_name}</b>\n/help වැඩි දුර තොරතුරැ"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
