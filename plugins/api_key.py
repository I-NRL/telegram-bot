from lib import inrl, my_db,BASE_URL

async def uapi(message, match):
  if not match:
      return await message.button({
          "url": f"{BASE_URL}api/signup",
          "text": "Provide me a new apikey",
          "name": "Get New Free ApiKey"
      })

  my_db["users"].update_one({'user': message.chat_id}, {'$set': {'apikey': match}})
  return await message.send(f'api key updated to <b>{match}</b>')

async def gapi(message, match)->str:
  db = my_db["users"].find_one({'user': message.chat_id})
  return await message.send(db['apikey'])

inrl({
  "pattern": "uapi",
  "type": "owner"
}, uapi)

inrl({
  "pattern": "gapi",
  "type": "owner"
}, gapi)