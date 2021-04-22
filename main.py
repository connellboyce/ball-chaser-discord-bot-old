import os
import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!goal'):
    await message.channel.send("What a save!")

  if message.content.startswith('!rank'):
    rank = getRank()
    await message.channel.send(rank)

def getRank():
  key = os.environ['TRN_ACCESS_KEY_ID'] # Your key goes here, this is mine
  platform = 'epic' 
  platformUserIdentifier = 'i_am_connell' # Random user example from gg tracker website
  link = f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{platformUserIdentifier}"
  headers = {
    'TRN-Api-Key' : key,
  }
  response = requests.get(link, headers=headers)
  jsonResponse = json.loads(response.text)
  rank = jsonResponse["data"]["segments"][3]["stats"]["tier"]["metadata"]["name"]
  return rank;

token = os.environ['BALL_CHASER_TOKEN']
client.run(token)