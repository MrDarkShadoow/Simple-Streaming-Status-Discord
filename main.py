import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event



async def on_connect():
  await client.change_presence(status= discord.Status.do_not_disturb,activity = discord.Streaming(name = "Lofi", url = "https://www.youtube.com/watch?v=5qap5aO4i9A"))
  print("Ready")



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
