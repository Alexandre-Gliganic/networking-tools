import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import os
import subprocess
import re
import yaml


regex_ipv6="(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
regex_ipv4="^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$"
regex_url="^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"


async def ping (ctx,args):
    
    if len(args)==0 or len(args) >1:
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **ping** command with domain or IPv4 or IPv6 like this : \n \n Domain: \n`.ping google.com` \n IPv4:\n`.ping 1.1.1.1`\n IPv6: \n`.ping 2606:4700:4700::1111`",color=0xFF0000)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    domaine=str(ip)
    
    #Regex match 
    patternv6=re.compile(regex_ipv6)
    res_patternv6=patternv6.match(domaine)
    patternv4=re.compile(regex_ipv4)
    res_patternv4=patternv4.match(domaine)
    patternurl=re.compile(regex_url)
    res_patternurl=patternurl.match(domaine)


    #print("V6 : ",res_patternv6) 
    #print("V4 : ",res_patternv4)
    #print("Url : ",res_patternurl)

    view = discord.ui.View()

    #IPV6 detect
    if res_patternv6!=None:
        ip_detect=6
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domaine}", url=f"https://[{domaine}]")
    #IPV4 detect
    elif res_patternv4!=None:
        ip_detect=4
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domaine}", url=f"https://[{domaine}]")
    #Website detect
    elif res_patternurl!=None:
        ip_detect=42
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domaine}", url=f"https://{domaine}")
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
    waiting1 = ("Ping for " + domaine +" with "+f"IPv{version}" )
    await ctx.channel.send(f"```py\n{waiting1} in progress ...```")
   
        
    try:
        if (version == 6):
            p = subprocess.run(["ping","-6", "-c", "5", domaine],capture_output=True, text=True, timeout=10)
        else:
            p = subprocess.run(["ping","-4", "-c", "5", domaine],capture_output=True, text=True, timeout=10)

    except subprocess.TimeoutExpired:
        print("Timeout")
        view.add_item(item=offline)
        if ip_detect != 0:
            view.add_item(item=website)
        await ctx.channel.send(f"```py\nTimeout for {domaine}```", view=view)
        return

    res = str(p.stdout)
    err = p.stderr
    

    if len(err) == 0:
        view.add_item(item=online)
        if ip_detect != 0:
            view.add_item(item=website)
        await ctx.channel.send(f"```py\n{res}```", view=view)
    else:
        view.add_item(item=offline)
        await ctx.channel.send(f"```py\n{err}```", view=view)
