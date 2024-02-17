import os
from lib import inrl, BASE_URL
import requests

def postJson(id, options):
    res = requests.post(f"{BASE_URL}api/gfx/{id}", data=options)
    return bytes(res.json()['result']['data'])


async def gfx1(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx1 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx1', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx2(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx2 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx2', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx3(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx3 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx3', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx4(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx4 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx4', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx5(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx5 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx5', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx6(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx6 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx6', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx7(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx7 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx7', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx8(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx8 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx8', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx9(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx9 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx9', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx10(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx10 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx10', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx11(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx11 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx11', options)
    return await message.bot.bot.send_photo(message.chat_id, res)

async def gfx12(message, match):
    if not match:
        await message.send('<i><b>Example:</b> gfx12 inrl|its me|dev</i>')
        return
    options = {'apikey': message.apikey}
    n = 1
    if '|' in match:
        options['text'] = match.split('|')[0]
        for a in match.split('|')[1:]:
            options[f'text{n}'] = a
            n += 1
    else:
        options['text'] = match
    res = postJson('gfx12', options)
    return await message.bot.bot.send_photo(message.chat_id, res)


inrl({
  "pattern": "gfx1",
  "type": "gfx"
}, gfx1)

inrl({
  "pattern": "gfx2",
  "type": "gfx"
}, gfx2)

inrl({
  "pattern": "gfx3",
  "type": "gfx"
}, gfx3)

inrl({
  "pattern": "gfx4",
  "type": "gfx"
}, gfx4)

inrl({
  "pattern": "gfx6",
  "type": "gfx"
}, gfx6)

inrl({
  "pattern": "gfx7",
  "type": "gfx"
}, gfx7)

inrl({
  "pattern": "gfx8",
  "type": "gfx"
}, gfx8)

inrl({
  "pattern": "gfx5",
  "type": "gfx"
}, gfx5)

inrl({
  "pattern": "gfx10",
  "type": "gfx"
}, gfx10)

inrl({
  "pattern": "gfx11",
  "type": "gfx"
}, gfx11)

inrl({
  "pattern": "gfx12",
  "type": "gfx"
}, gfx12)

inrl({
  "pattern": "gfx9",
  "type": "gfx"
}, gfx9)