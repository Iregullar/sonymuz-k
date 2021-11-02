from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""Ben {bn} !!
Grubunuzun sesli ve görüntülü sohbetinde müzik çalmak için tasarlan bir botum, Bana Mp3 Formatında Şarkıları Veriniz. Komutlarım Aşağıdaki Gibidir:
🔥 /play - yanıtlanan ses dosyasını veya YouTube videosunu linki url aracılığıyla oynatılır. 
🔥 /Listen - YouTube üzerinden müzik bulut. 
🔥 /find - İstenilen parçayı kısa sürede bulmak için
🔥 /pause - Sesli Sohbeti durdurmak için
🔥 /resume - sesli sohbeti devam ettirir. 
🔥 /skip - Geçerli Ses Atlanır. 
🔥 /stop - Sırayı temizler ve Sesli Sohbet Müziklerinin listesini kaldırır.
💡 /asistan - Userbot Grubunuza Katılır.
💡 /asistanby - Userbot Grubunuzdan Ayrılır. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎼 Asistan", url="https://t.me/SonyMusicAssistant"

                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url="https://t.me/SonyMusicSupport"
                    ),                    
                    InlineKeyboardButton(
                        "🇹🇷 Sahip", url="https://t.me/SonyMusicDeveloper" 
                    ), 
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""🔴 {PROJECT_NAME} is online""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ Beni Grubuna ekle ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Güncelleme kanalı', url=f"https://t.me/SonyMusicSupport"),
            [InlineKeyboardButton(text = '👨‍💻 Sahip 👨‍💻', url=f"https://{SOURCE_CODE}")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button 
        @Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)

async def ghelp(_, message: Message):

    await message.reply_text(

        f"""🙋‍♀️ Merhaba oradaki! Telegram gruplarının ve kanallarının sesli sohbetlerinde müzik çalabilirim.""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🟡 Yardım için buraya tıklayın 🟡", url=f"https://t.me/{BOT_USERNAME}?start"

                    )

                ]

            ]

        ),

    )
        
      












