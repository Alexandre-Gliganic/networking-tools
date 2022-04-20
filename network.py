import discord
import yaml
from discord.ext import commands
from src.message import OnMessage

#Get the token
with open('config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)


intents = discord.Intents(messages=True, guilds=True, reactions=False, members=False, dm_messages=False,
                              guild_reactions=False, message_content=True)        

bot = commands.Bot(command_prefix=config['prefix'], description = "Look at the network",intents = intents)

@bot.event
async def on_ready():
    print("The bot is connected!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help to view commands."))

@bot.event
async def on_message(ctx):
    await OnMessage.run(ctx)

bot.run(tokens['discord_token'])

