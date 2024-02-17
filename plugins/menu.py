from lib import inrl, commands, BOT_INFO,PREFIX,BASE_URL
import os
import datetime
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
keyboard = [
    [
        InlineKeyboardButton("ping", callback_data=f'{PREFIX}ping'),
        InlineKeyboardButton("owner", callback_data=f'{PREFIX}owner'),
    ],
    [InlineKeyboardButton("Our Api Page", url=f'{BASE_URL}api/dashboard')],
]

async def send_menu(message, match):
    #print(BOT_INFO. S)
    date = datetime.datetime.now().strftime("%B %d, %Y")
    cmnd = []
    cmd = ''
    category = []
    menu = f"╭━〔 {BOT_INFO.split(';')[0]} 〕━◉\n┃╭━━━━━━━━━━◉\n┃┃ Plugins : {len(commands)}\n┃┃ User :- @{message.username}\n┃┃ Owner : {BOT_INFO.split(';')[1]}\n┃┃ Prefix:- {PREFIX}\n┃┃ Date:- {date}\n┃╰━━━━━━━━━━◉"

    for command in commands:
      if 'pattern' in command:
        cmnd.append({
            'cmd': command['pattern'],
            'type': command['type'].lower()
        })
        if command['type'].lower() not in category:
            category.append(command['type'].lower())
    for cmmd in category:
        menu += f"\n┠┌─⭓ {cmmd.upper()} "
        comad = [c for c in cmnd if c['type'] == cmmd]
        for num, com in enumerate(comad):
            menu += f"\n┃│◦ {com['cmd']}"
        menu += f"\n┃└────────⭓"
    menu += '\n╰━━━━━━━━━━━◉'
    await message.bot.bot.send_photo(message.chat_id, BOT_INFO.split(';')[2], caption=menu, disable_notification=None, reply_to_message_id=None, reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=None,pool_timeout=None, api_kwargs=None)


inrl({
  "pattern": "menu",
  "type": "info"
}, send_menu)