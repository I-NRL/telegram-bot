from lib import inrl


async def evaluation(message, match):
    try:
        evaled = await eval(match)
        if not isinstance(match, str):
            evaled = str(evaled)
            await message.send(evaled)
    except Exception as err:
        print(err)
        await message.send(str(err))
     

inrl({
  "on": "text",
  "fromMe": True,
  "prefix": ">"
}, evaluation)