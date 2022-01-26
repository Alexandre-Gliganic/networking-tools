from src.embed import *

async def help (ctx):
    await ctx.channel.send(embed=CompleteEmbed("Help","You can find all commands here\
        \n \n`.dig` \n`.host` \n`.ping` \n`.ping6` \n`.traceroute` \n`.traceroute6` \n`.whois`",0xFF8B00))
    return