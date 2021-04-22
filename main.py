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
    contentList = str(message.content).split(" ")
    if (contentList[2] == "1"):
      rank = get1Rank(contentList[1])
    if (contentList[2] == "2"):
      rank = get2Rank(contentList[1])
    if (contentList[2] == "3"):
      rank = get3Rank(contentList[1])
    else:
      rank = "invalid arguments"

    await message.channel.send(rank)

def get3Rank(username):
  print("uname="+username)
  key = os.environ['TRN_ACCESS_KEY_ID'] # Your key goes here, this is mine
  platform = 'epic' 
  username = username;
  link = f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}"
  headers = {
    'TRN-Api-Key' : key,
  }
  response = requests.get(link, headers=headers)
  jsonResponse = json.loads(response.text)
  rank = jsonResponse["data"]["segments"][3]["stats"]["tier"]["metadata"]["name"]
  return rank;

def get2Rank(username):
  print("uname="+username)
  key = os.environ['TRN_ACCESS_KEY_ID'] # Your key goes here, this is mine
  platform = 'epic' 
  username = username;
  link = f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}"
  headers = {
    'TRN-Api-Key' : key,
  }
  response = requests.get(link, headers=headers)
  jsonResponse = json.loads(response.text)
  rank = jsonResponse["data"]["segments"][2]["stats"]["tier"]["metadata"]["name"]
  return rank;

def get1Rank(username):
  print("uname="+username)
  key = os.environ['TRN_ACCESS_KEY_ID'] # Your key goes here, this is mine
  platform = 'epic' 
  username = username;
  link = f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}"
  headers = {
    'TRN-Api-Key' : key,
  }
  response = requests.get(link, headers=headers)
  jsonResponse = json.loads(response.text)
  rank = jsonResponse["data"]["segments"][1]["stats"]["tier"]["metadata"]["name"]
  return rank;

token = os.environ['BALL_CHASER_TOKEN']
client.run(token)