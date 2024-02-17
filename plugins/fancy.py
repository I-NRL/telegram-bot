from lib import BASE_URL,my_db, inrl
import re
import requests

async def fancy(message, match):
    if match == "":
        res = requests.get(f"{BASE_URL}api/tools/fancy?text=fancy 10 inrl&apikey={message.apikey}&key=list")
        if not res.status_code == 200:
            return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
        elif  not res.json()['status']:
          return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
        msg = "Fancy Text List\n\n"
        for i in res.json()['result']:
          msg += f"{i['key']}. {i['fancy']}\n"
        return await message.send(msg)
    id = re.findall(r'\d+', match)
    if len(id) == 0 and match:
        res = requests.post(f"{BASE_URL}api/tools/fancy", json={"text": match, "apikey": message.apikey, "key": "list"})
        if not res.status_code == 200:
            return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
        elif  not res.json()['status']:
          return await message.button({"text":"Please enter a new apikey, as the given apikey limit has been exceeded. Visit our page for getting a new apikey.", "url": f"{BASE_URL}api/signup", "name":"Get New Free ApiKey"})
        msg = "Fancy Text List\n\n"
        for i in res.json()['result']:
          msg += f"{i['key']}. {i['fancy']}\n"
        return await message.send(msg)

    res = requests.post(f"{BASE_URL}api/tools/fancy", json={"text": match.replace(id[0], ""), "apikey": message.apikey, "key": id[0]})
    if not res.status_code == 200:
        return message.send(f"Please enter a new apikey, as the given apikey limit has been exceeded. Visit {BASE_URL}api/signup for getting a new apikey.")
    elif  not res.json()['status']:
      return await message.send(f"Please enter a new apikey, as the given apikey limit has been exceeded. Visit {BASE_URL}api/signup for getting a new apikey.")
    return await message.send(f"{res.json()['result']}")


inrl({
  'pattern': 'fancy',
  'type': 'utility'
}, fancy)