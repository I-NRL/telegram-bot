import requests
from lib import inrl, BASE_URL

async def chatgpt(message, match):
  if not message.apikey:
    return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
  elif not match:
    return await message.send('<i><b>Example:</b> gpt what is memory leakage</i>')
  res = requests.get(BASE_URL+f'api/ai/chatgpt?text={match}&apikey={message.apikey}')
  if not res.status_code == 200:
    return await message.send('Internal Server Error!')
  res = res.json()
  if not res['status']:
    return await message.send('Request Error, check you apikey!')
  return await message.send(res['result'].replace('```', ''))
 
inrl({
  "pattern": "gpt",
  "type": "eva"
}, chatgpt)