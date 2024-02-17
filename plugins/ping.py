import time
from lib import inrl

async def ping(message, match):
    start = time.time() * 1000
    sped = await message.send("Ping!")
    end = time.time() * 1000
    await sped.edit_text(f"<b>⚡PONG!</b> {str(end - start).split('.')[0]} ms")

inrl({
  'pattern': 'ping',
  'type': 'utility'
}, ping)
    