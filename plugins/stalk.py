import requests
from lib import inrl, BASE_URL


async def igstalk(message, match):
  if not message.apikey:
    return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
  elif not match:
    return await message.send('<i><b>Example:</b> ig mhd_fasweeh</i>')
  res = requests.get(BASE_URL+f'api/stalk/ig?name={match}&apikey={message.apikey}')
  if not res.status_code == 200:
    return await message.send('Internal Server Error!')
  res = res.json()
  if not res['status']:
    return await message.send('Request Error, check your apikey!')
  res = res['result']['user_info']
  captionText = f"""username : {res['username']}\nname : {res['full_name']}\nposts : {res['posts']}\nfollowers : {res['followers']}\nfollowing : {res['following']}\nprivate account: {res['is_private']}\nverified account: {res['is_verified']}\n\n\nbio : {res['biography']}"""
  return await message.bot.bot.send_photo(message.chat_id, res['profile_pic_url'],
  caption=captionText)

async def ytchannel(message, match):
  if not message.apikey:
    return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
  elif not match:
    return await message.send('<i><b>Example:</b> ytc inrl</i>')
  res = requests.get(BASE_URL+f'api/stalk/ytchannel?name={match}&apikey={message.apikey}')
  if not res.status_code == 200:
    return await message.send('Internal Server Error!')
  res = res.json()
  if not res['status']:
    return await message.send('Request Error, check your apikey!')
  res = res['result'][0]
  name = res['name']
  thumbnail = res['thumbnail']
  verified = res['verified']
  url = res['url']
  subscribers = res['subscribers']
  total_video = res['total_video']
  family_safe = res['family_safe']
  keywords = res['keywords']
  description = res['description']
  return await message.bot.bot.send_photo(message.chat_id, thumbnail[0]['url'],caption=f"name: {name}\nverified: {verified}\nurl: {url}\nsubscribers: {subscribers}\nvideos: {total_video} video\ndescription: {description or 'null'}\nkeywords: {keywords or 'null'}\nfamily safe: {family_safe}")

inrl({
  "pattern": "ig",
  "type": "stalk"
}, igstalk)

inrl({
  "pattern": "ytc",
  "type": "stalk"
}, ytchannel)