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

  if message.content.startswith('!help'):
    await message.channel.send("!rank <username> <1, 2, or 3> : check your rank\n!goal : get 'get what a save-d'")

  if message.content.startswith('!goal'):
    await message.channel.send("What a save!")

  if message.content.startswith('!rank'):
    contentList = str(message.content).split(" ")
    rank = getRank(contentList[1], contentList[2])

    await message.channel.send(rank)

def getRank(username, mode):
  mode = int(mode)
  key = os.environ['TRN_ACCESS_KEY_ID'] # Your key goes here, this is mine
  platform = 'epic' 
  username = username;
  link = f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}"
  headers = {
    'TRN-Api-Key' : key,
  }
  response = requests.get(link, headers=headers)
  jsonResponse = json.loads(response.text)
  if (jsonResponse["data"]["segments"][1]["metadata"]["name"] == "Un-Ranked"):
    mode = mode+1
  rank = jsonResponse["data"]["segments"][mode]["stats"]["tier"]["metadata"]["name"]
  return rank;

token = os.environ['BALL_CHASER_TOKEN']
client.run(token)