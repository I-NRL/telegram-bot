from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, Update
from typing import List, cast
from . import BASE_URL, my_db
import sys


class Message:
  def __init__(self, update, _):
      self.update = update
      self.bot = _
      if hasattr(update.poll_answer,'poll_id'):
        #print(update)
        answer = update.poll_answer
        answered_poll = _.bot_data[answer.poll_id]
        selected_options = answer.option_ids
        print(answered_poll,selected_options)
      elif hasattr(update.callback_query,'data'):
        self.update = update.callback_query
        self.body = update.callback_query.data
        self.message = update.callback_query.message.caption
        self.chat_id = update.callback_query.from_user.id
        self.first_name = update.callback_query.from_user.first_name
        self.username = update.callback_query.from_user.username
        self.message_id = update.callback_query.message.message_id
        self.db_data = my_db["users"].find_one({"user": self.chat_id})
        if str(update.callback_query.message.chat.id).__contains__(str(1002097273316)):
          self.apikey = 'inrl-bot-mdaqz3ks6md7'
        else:
          self.apikey = self.db_data.setdefault('apikey', None)
        self.bottons = update.callback_query.message.reply_markup
      else:
        self.body = update.effective_message.text
        self.message = update.effective_message
        self.message_id = self.message.message_id
        self.chat_id = self.message.chat_id
        self.text = self.message.text
        self.date = self.message.date
        self.username = update.message.from_user.username
        self.first_name = update.message.from_user.first_name
        self.db_data = my_db["users"].find_one({"user": self.chat_id})
        if str(update.message.chat.id).__contains__(str(1002097273316)):
          self.apikey = 'inrl-bot-mdaqz3ks6md7'
        else:
          self.apikey = self.db_data.setdefault('apikey', None)
  async def send(self,text,options = {}, type= 'text'):
      if type == 'text':
        message = await self.update.message.reply_text(text)
        return message


  async def button(self, dict):
      reply_markup = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(dict['name']
        , url=dict['url'])
      )
      return await self.update.message.reply_text(dict['text'], reply_markup=reply_markup)