commands = []

def inrl(info, fn):
  commands.append({**info, "function": fn})
