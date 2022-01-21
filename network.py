from xml import dom
import discord
import yaml
from discord.ext import commands
from src.message import OnMessage

#Get the token
with open('config/tokens.yml', 'r') as file:
    tokens = yaml.safe_load(file)
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)
        

bot = commands.Bot(command_prefix=config['prefix'], description = "Look at the network")
#bot.remove_command('help')

@bot.event
async def on_ready():
    print("The bot is connected!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help to view commands"))
   

@bot.event
async def on_message(ctx):
    await OnMessage.run(ctx)
    return




"""
@bot.command()
async def test (ctx):
    print("test")
    print('Logged on as {0}!'.format(bot.user))
    #await ctx.send(f"Connected at {datetime.datetime.now()}")
    view = discord.ui.View()
    item = discord.ui.Button(style=discord.ButtonStyle.green, label="Click Me", url="https://google.com")
    item2 = discord.ui.Button(style=discord.ButtonStyle.green, label="Danger ⚠")
    item3 = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Test 🥵")
   
    async def button_callback(interaction):
        #await interaction.response.edit_message(content="Hello there", view=None)
        await interaction.response.send_message("Hi")
        
    item2.callback = button_callback
    view.add_item(item=item)
    view.add_item(item=item2)
    view.add_item(item=item3)
    await ctx.send(f"Connected at {datetime.datetime.now()}", view=view)
"""


bot.run(tokens['discord_token'])

