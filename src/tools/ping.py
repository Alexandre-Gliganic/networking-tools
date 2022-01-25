import discord
import re
from src.process import *
from src.error import *


regex_ipv6="(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
regex_ipv4="^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$"
regex_url="^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"


async def ping(ctx,args):
    
    if len(args)==0 or len(args) >1:
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **ping** command with domain or IPv4 or IPv6 like this : \n \n Domain: \n`.ping google.com` \n IPv4:\n`.ping 1.1.1.1`\n IPv6: \n`.ping 2606:4700:4700::1111`",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    domain=str(ip)
    
    #Regex match 
    patternv6=re.compile(regex_ipv6)
    res_patternv6=patternv6.match(domain)
    patternv4=re.compile(regex_ipv4)
    res_patternv4=patternv4.match(domain)
    patternurl=re.compile(regex_url)
    res_patternurl=patternurl.match(domain)


    #print("V6 : ",res_patternv6) 
    #print("V4 : ",res_patternv4)
    #print("Url : ",res_patternurl)

    view = discord.ui.View()

    #IPV6 detect
    if res_patternv6!=None:
        ip_detect=6
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://[{domain}]")
    #IPV4 detect
    elif res_patternv4!=None:
        ip_detect=4
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://[{domain}]")
    #Website detect
    elif res_patternurl!=None:
        ip_detect=42
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://{domain}")
    #else
    else:
        ip_detect = 0
    
    offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
    online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
    
    if ip_detect==42 or ip_detect==0 or ip_detect==4:
        version=4
    else:
        version=6
    
        
    print("Ping for", ip, f"with IPv{version}", "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    embed=discord.Embed(title="Ping", description = f"Ping for **{domain}** with **IPv{version}** in progress ...",color=0x00FF00)
    embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
    await ctx.channel.send(embed=embed)
    msg2= await ctx.channel.send(":hourglass:")

    try:
        await execute_prog_realtime(f"ping -{4 if version == 4 else 6} -c 5 {domain}", 8, msg2)
       
    except TimeoutError:
        print("Timeout")
        view.add_item(item=offline)
        if ip_detect != 0:
            view.add_item(item=website)
        await msg2.delete()
        embed=discord.Embed(title="Timeout", description = f"➜ Timeout for **{domain}**",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed, view=view)
        return
    
    except ErrorDuringProcess as err:
        if err.code!=1:
            await msg2.delete()
        print(f"Error code: {err.code}")
        view.add_item(item=offline)
        embed=discord.Embed(title=f"Error {err.code}", description = f"➜ {err.err if len(err.err) != 0 else 'Error occured'}",color=0xFF0000)
        embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
        await ctx.channel.send(embed=embed, view=view)
        return
    else:
        view.add_item(item=online)
        if ip_detect != 0:
            view.add_item(item=website)
    await msg2.edit(view=view)