from lib import inrl

async def tag(message, match):
  questions = ["Good", "Really good", "Fantastic", "Great"]
  mssage = await message.bot.bot.send_poll(
        message.update.effective_chat.id,
        "How are you?",
        questions,
        is_anonymous=False,
        allows_multiple_answers=False,
    )
    # Save some info about the poll the bot_data for later use in receive_poll_answer
  payload = {
        mssage.poll.id: {
            "questions": questions,
            "message_id": mssage.message_id,
            "chat_id": message. update.effective_chat.id,
            "answers": 0,
        }
    }
  message.bot.bot_data.update(payload)
  #group_meta = await message.bot.bot.get_chat(message.chat_id)
 # print(group_meta)

inrl({
  "pattern": "tag",
  "type": "owner"
}, tag)