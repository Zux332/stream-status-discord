import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)



# name = for your status and url = for your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "status", url = "https://twitch.tv/overtaker55"))



alive.alive()
client.run(os.getenv("OTE4NTcwNzQyNjMzODg5ODUz.G9Uhob.2gFo3IIFyPCjqMdnwgn9eujeZh9neQdBM3EeCE"), bot=False)
