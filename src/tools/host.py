import discord
from src.process import *
from src.error import *
from src.embed import *
from src.view import *

async def host (ctx,args):
    
    if len(args) != 1 :
        print("Missing Required Argument")
        await ctx.channel.send(embed=CompleteEmbed("Error", "Missing Required Argument. \n \n You should use the **host** command with domain like this : \n \n Domain:\n`.host google.com`", 0xFF0000))
        return
    
    ip=args[0]
    print("Host for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    
    await ctx.channel.send(embed=CompleteEmbed("Host", f"Host **{ip}** in progress ...", 0x00FF00))
    msg2= await ctx.channel.send(":hourglass:")

    try:
        res,err=await execute_prog(f"host {ip}", 10)

    except TimeoutError:
        print("Timeout")
        await ctx.channel.send(embed=CompleteEmbed("Timeout", f"➜ Timeout for **{ip}**", 0xFF0000), view=simple_view("offline"))
        return
    except ErrorDuringProcess as err:
        print(f"Error code: {err.code}")
        await msg2.delete()
        await ctx.channel.send(embed=CompleteEmbed("Error {err.code}",f"➜ Host **{ip}** not found.",0xFF0000), view=simple_view("offline"))
        return
        
    else:
        await msg2.edit(f"```py\n{res}```",view=simple_view("online"))
        return