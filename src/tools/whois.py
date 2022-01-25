import discord
from src.tools.process import *
from src.tools.error import *
from src.tools.regex import whatis

async def whois (ctx,args):
    
    if len(args) != 1 :
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **whois** command with IPv4 or IPv6 like this : \n \n IPv4:\n`.whois 1.1.1.1`\n IPv6: \n`.whois 2606:4700:4700::1111`",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    print("Whois for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    
    view = discord.ui.View()    
    offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
    online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
    
    embed=discord.Embed(title="Whois", description = f"Whois **{ip}** in progress ...",color=0x00FF00)
    embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
    await ctx.channel.send(embed=embed)
    msg2= await ctx.channel.send(":hourglass:")
    
    
    version=await whatis(ip)
    print(version)
    if version=="v4" or version == "v6" or version == "AS":
        flag="-r"
    elif version == "url":
        return
    else:
        return
        

    try:
        res,err=await execute_prog(f"whois {flag} {ip}", 10)

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
        embed=discord.Embed(title="Error", description = f":warning: **Error {err.code}** occured during process for **{ip}** :warning:",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed, view=view)
        view.add_item(item=offline)
        return
    else:
        filter_res = ""
        
        for line in res.splitlines()[9:]: #remove the 10 lines of information whois function 
            if not line.startswith('remarks:'): #remove comments
                filter_res+=line+'\n'   
        print(filter_res)
        find = filter_res.find("ERROR:101") #detect error101 for button
        if find == -1:
            view.add_item(item=online)
            await msg2.edit(f"```py\n{filter_res}```",view=view)
            return
            
        else:
            embed=discord.Embed(title=f"Error", description = f"➜ No entries found in source RIPE for **{ip}**.",color=0xFF0000)
            embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
            view.add_item(item=offline)
            await msg2.delete()
            await ctx.channel.send(embed=embed,view=view)
            return
            
