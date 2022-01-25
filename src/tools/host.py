import discord
from src.tools.process import *
from src.tools.error import *

async def host (ctx,args):
    
    if len(args) != 1 :
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **host** command with domain like this : \n \n Domain:\n`.host google.com`",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    print("Host for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    
    view = discord.ui.View()    
    offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
    online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
    
    embed=discord.Embed(title="Host", description = f"Host **{ip}** in progress ...",color=0x00FF00)
    embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
    await ctx.channel.send(embed=embed)
    msg2= await ctx.channel.send(":hourglass:")

    try:
        res,err=await execute_prog(f"host {ip}", 10)

    except TimeoutError:
        print("Timeout")
        view.add_item(item=offline)
        embed=discord.Embed(title="Timeout", description = f"➜ Timeout for **{ip}**",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed, view=view)
        return
    except ErrorDuringProcess as err:
        print(f"Error code: {err.code}")
        await msg2.delete()
        embed=discord.Embed(title=f"Error {err.code}", description = f"➜ Host **{ip}** not found.",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        view.add_item(item=offline)
        await ctx.channel.send(embed=embed, view=view)
        return
        
    else:
        view.add_item(item=online)
        await msg2.edit(f"```py\n{res}```",view=view)
        return