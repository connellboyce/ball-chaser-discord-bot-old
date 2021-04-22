import os
import discord
import requests
import json

# Initialize the client
client = discord.Client()

# On ready notification
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# On message(s) handling
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Give list of commands
  if message.content.startswith('!help'):
    await message.channel.send("!rank <username> <1, 2, or 3> : check your rank\n!goal : get 'get what a save-d'")

  # Say "What a save!"
  if message.content.startswith('!goal'):
    await message.channel.send("What a save!")

  # Provide user's rank
  if message.content.startswith('!rank'):
    contentList = str(message.content).split(" ")
    rank = getRank(contentList[1], contentList[2])
    await message.channel.send(rank)

  # Gets and categorizes ranks
  if message.content.startswith('!summary'):
    contentList = str(message.content).split(" ")
    summary = getSummary(contentList[1])
    await message.channel.send(summary)


"""
Gets JSON response for the specified user

@param username: the specified username to find
@return the account summary of that user
"""
def getJson(username):
  key = os.environ['TRN_ACCESS_KEY_ID'] # Your key goes here, this is mine
  platform = 'epic' 
  link = f"https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}"
  headers = {
    'TRN-Api-Key' : key,
  }
  response = requests.get(link, headers=headers)
  jsonResponse = json.loads(response.text)
  return jsonResponse


"""
Gets rank based on the username and game mode provided

@param username: the specified username to find
@param mode: the game mode to search for
@return the rank of the user in that game mode
"""
def getRank(username, mode):
  jsonResponse = getSummary(username)

  translation = {'1': 'Ranked Duel 1v1', '2': 'Ranked Doubles 2v2', '3': 'Ranked Standard 3v3', 'hoops': 'Hoops', 'rumble': 'Rumble', 'dropshot': 'Dropshot', 'snowday': 'Snowday', 'tournament': 'Tournament Matches', 'unranked': 'Un-Ranked'}
  return jsonResponse[translation[mode.lower()]]


"""
Gets all ranks for a given user

@param username the specified username to find
@return the ranks summary of that user
"""
def getSummary(username):
  jsonResponse = getJson(username)
  stuff = {}
  for x in range(10):
    try: stuff[jsonResponse['data']['segments'][x]['metadata']['name']] = jsonResponse['data']['segments'][x]['stats']['tier']['metadata']['name']
    except: None
  return stuff


# Starts the bot
token = os.environ['BALL_CHASER_TOKEN']
client.run(token)