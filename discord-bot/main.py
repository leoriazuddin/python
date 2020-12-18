import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

# when bot is ready
@client.event
async def on_ready():
  print("MoneyBot logged in as {0.user}.".format(client))

# resolve command
@client.event
async def on_message(message):
  if message == "" or message.author == client.user:
    return

  msg = ""
  if message.content.startswith("$hello"):
    msg = commands()
  elif message.content.startswith("$quote"):
    msg = get_quote()

  await message.channel.send(msg)

# display help
def commands():
  command = "Hello! I am your Money Bot. Below is a list of commands I answer\n"
  command += "$hello - list of all commands.\n"
  command += "$quote - Random quote of the day.\n"

  return command

# get quote random
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']

  return quote

# run the server
keep_alive()

# run the client
client.run(os.getenv("TOKEN"))
