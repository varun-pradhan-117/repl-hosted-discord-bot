import os
import discord
from dotenv import load_dotenv
from keepAlive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
@client.event 
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event 
async def on_message(message):
  #Check if message is sent to "Responses" channel
  if message.channel.id != {Responses Channel ID}:
    return 
  #Ignore messages sent by bot
  if message.author==client.user:
    return 
  #Collect message data
  text=message.content
  user=message.author
  #Delete message from "Responses" channel
  await message.delete()
  #Check if author has the participant role
  if discord.utils.get(user.roles,name="The Words and the Bees")==None:
    return
  #Set destination Channel as the private mod channel
  destChannel=client.get_channel({destination channel ID})
  #Report message in private channel
  await destChannel.send(f"**{user.display_name}** says '{text}'")

#keep_alive is used to prevent repl.it from timing out after 1 hour
keep_alive()
client.run(TOKEN)

