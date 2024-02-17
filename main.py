import logging
from telegram.ext import ApplicationBuilder, Defaults, CommandHandler, ContextTypes, PrefixHandler, MessageHandler, filters,CallbackQueryHandler,PollAnswerHandler
import os
import importlib
from lib import commands, Message as ReplyMessage, my_db
from telegram.constants import ParseMode
from config import SESSION_ID, MONGO_URL, PREFIX, BASE_URL, OWENER_ID
from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, Message, Update,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from typing import List, cast
import inspect

plugins = os.listdir('plugins')
for plugin in plugins:
  if plugin.endswith('.py'):
    try:
      plugin_name = os.path.splitext(plugin)[0]
      plugin_module = importlib.import_module(f'plugins.{plugin_name}')
    except Exception as e:
      print(e)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="mb.log",
)

logger = logging.getLogger(__name__)

async def greetings(update, context):
  group_meta = await context.bot.get_chat(update.message.chat.id)
  print(update.message.chat.id)
  print(group_meta)
  
async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  message = update.effective_message
  db_data = my_db["users"].find_one({"user": message.chat_id})
  if db_data is None:
    return await context.bot.send_message(
        chat_id=message.chat_id,
        text=
        "you are not started this bot, type /start to start this bot and try again"
    )
  elif 'apikey' in db_data:
    return await context.bot.send_message(
        chat_id=message.chat_id,
        text=
        "you are already logged in to our telegram bot, use the logout command if you want to remove your credentials"
    )
  elif not hasattr(
      message, 'text') or len(message.text.replace('/login', '').strip()) != 6:
    return await context.bot.send_message(
        chat_id=message.chat_id,
        text="Invalid ApiKey or You are not provided an ApiKey")
  else:
    try:
      apiKey = message.text.replace('/login', '').strip()
      my_db["users"].update_one({"user": message.chat_id},
                                {"$set": {
                                    "apikey": apiKey
                                }})
      return await context.bot.send_message(
          chat_id=message.chat_id,
          text="successfully Login'd to our telegram bot")
    except Exception as e:
      print(e)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  iscontact = hasattr(update.effective_message.contact,'phone_number')
  try:
    message = update.effective_message
    message_id = message.message_id
    chat_id = message.chat_id
    text = message.text
    date = message.date
    username = message.chat.username
    first_name = message.chat.first_name
    user_data = my_db["users"].find_one({"user": chat_id}) 
    if user_data is None or not 'contact' in user_data and iscontact == None:
      my_db["users"].insert_one({"user": chat_id, "name": username})
      contact_keyboard = KeyboardButton(text="send your contact to verifies you are a human", request_contact=True)
      custom_keyboard = [[contact_keyboard]]
      reply_markup = ReplyKeyboardMarkup(custom_keyboard)
      await context.bot.send_message(chat_id=chat_id,text="send a contact message to verifying you are not a bot",reply_markup=reply_markup)
    elif not 'contact' in user_data and iscontact:
      my_db["users"].update_one({"user": chat_id}, {"$set": {"contact": update.effective_message.contact.phone_number}})
      await context.bot.send_message(
          chat_id=OWENER_ID,
          text=
          f"<i><b>from:</b>  {username}\n<b>text:</b> {text}\n<b>date:</b> {date}\n<b>chat id:</b> {chat_id}\n<b>contact: {update.effective_message.contact.phone_number}</b></i>"
      )
    elif 'contact' in user_data:
      reply_markup = ReplyKeyboardRemove()
      await context.bot.send_message(chat_id=chat_id, text="you are already started this bot, use menu to show commands", reply_markup=reply_markup
)
    else:
      contact_keyboard = KeyboardButton(text="send your contact to verifies you are a human", request_contact=True)
      custom_keyboard = [[contact_keyboard]]
      reply_markup = ReplyKeyboardMarkup(custom_keyboard)
      await context.bot.send_message(chat_id=chat_id,text="must verify with forwarding contact!!",reply_markup=reply_markup)
  except Exception as e:
    print(e)


async def withClass(
    update,
    _
):
  message = ReplyMessage(update, _)
  for cmd in commands:
    if 'pattern' in cmd:
      is_command = message.body.replace(PREFIX,'').strip().lower().startswith(cmd['pattern'])
      if message.body.startswith(PREFIX) and is_command:
        message.body = message.body.replace(PREFIX,'').strip()
        setattr(message, 'cmd', cmd['pattern'])
        setattr(message, 'text',
              message.body.replace(message.cmd, '').replace(PREFIX, ''))
        try:
          
          if message.db_data is None and not message.apikey:
            return await message.send(
              "you are not started this bot, type /start to start this bot and try again"
          )
          elif not 'apikey' in message.db_data and not message.apikey:
            text = (
              "I'm the <b>Inrl Bot</b> and its just an usefull Telegram Bot"
              "To use me, you must login to our api page🙂."
              "after login use command /login and thet <b>apikey</b>")
            reply_markup = InlineKeyboardMarkup.from_button(
              InlineKeyboardButton("Get Free ApiKey🤖",
                                   url=f"{BASE_URL}api/signup"))
            await cast(Message,
                     update.message).reply_text(text,
                                                   reply_markup=reply_markup)
          else:
            await cmd['function'](message, message.text.strip())
        except Exception as e:
          print(e)
    elif 'on' in cmd and message.body.startswith(cmd['prefix']):
      setattr(message, 'text', message.body.replace(cmd['prefix'], '').strip())
      try:
        await cmd['function'](message, message.text)
      except Exception as e:
        print(e)


async def run_apps(app):
  app.add_handler(CommandHandler('start', start))
  app.add_handler(MessageHandler(filters.StatusUpdate.ALL, greetings))
  app.add_handler(CommandHandler('login', login))
  app.add_handler(MessageHandler(filters.CONTACT, start))
  app.add_handler(MessageHandler(filters.ALL, withClass))
  app.add_handler(CallbackQueryHandler(withClass))
  app.add_handler(PollAnswerHandler(withClass))
def main() -> None:
  application = (ApplicationBuilder().token(SESSION_ID).defaults(
      Defaults(parse_mode=ParseMode.HTML,
               do_quote=True)).post_init(run_apps).build())
  application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
  main()
