import discord
from src.tools.process import *
from src.tools.error import *

async def traceroute6 (ctx,args):
    
    if len(args) != 1 :
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **traceroute** command with domain or IPv6 like this : \n \n Domain: \n`.traceroute google.com` \n IPv6: \n`.traceroute 2606:4700:4700::1111`",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    print("Traceroute6 for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")

    view = discord.ui.View()    
    offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
    online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
    
    embed=discord.Embed(title="Traceroute6", description = f"Traceroute6 **{ip}** in progress ...",color=0x00FF00)
    embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
    await ctx.channel.send(embed=embed)
    msg2= await ctx.channel.send("_ _")

    try:
        await execute_prog_realtime(f"traceroute6 {ip}", 20, msg2)

    except TimeoutError:
        print("Timeout")
        view.add_item(item=offline)
        embed=discord.Embed(title="Timeout", description = f"Timeout for **{ip}**",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed, view=view)
        return
    except ErrorDuringProcess as err:
        print(f"Error code: {err.code}")
        embed=discord.Embed(title="Error", description = f":warning: **Error {err.code} occured during process for {ip}** :warning:",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed, view=view)
        view.add_item(item=offline)
        return
    else:
        view.add_item(item=online)
    await msg2.edit(view=view)
