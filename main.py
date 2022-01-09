import os
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.environ['Token']
bot = commands.Bot(command_prefix = '!')

bot.lava_nodes = [
  {
    'host': 'lava.link',
    'port': 80,
    'rest_uri': 'http://lava.link:80',
    'identifier': 'MAIN',
    'region': 'algeria',
    'password': 'anything really'
  }
]

@bot.event
async def on_ready():
  print('ready when you are o/')
  bot.load_extension('dismusic')
  bot.load_extension('dch')

keep_alive()
bot.run(TOKEN)