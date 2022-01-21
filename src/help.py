import discord
import subprocess

async def help (ctx):
    
    embed=discord.Embed(title="Help", description = "You can find all the commands here. \n \n`.dig` \n`.host` \n`.ping` \n`.traceroute` \n`.traceroute6` \n`.whois`",color=0xFF8B00)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    await ctx.channel.send(embed=embed)
    return