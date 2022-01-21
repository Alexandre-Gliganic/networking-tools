import discord
import subprocess

async def traceroute6 (ctx,args):
    
    if len(args)==0 or len(args) >1:
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **traceroute** command with domain or IPv6 like this : \n \n Domain: \n`.traceroute google.com` \n IPv6: \n`.traceroute 2606:4700:4700::1111`",color=0xFF0000)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    print("Traceroute6 for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    domaine=str(ip)

    view = discord.ui.View()    
    offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
    online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
    

    waiting1 = ("Traceroute6 for " + domaine)
    await ctx.channel.send(f"```py\n{waiting1} in progress ...```")
        
    try:
        
        p = subprocess.run(["traceroute6", domaine],capture_output=True, text=True, timeout=20)
        

    except subprocess.TimeoutExpired:
        print("Timeout")
        view.add_item(item=offline)
        await ctx.channel.send(f"```py\nTimeout for {domaine}```", view=view)
        return

   
    res = str(p.stdout)
    err = p.stderr

    if len(err) == 0:
        view.add_item(item=online)
        await ctx.channel.send(f"```py\n{res}```", view=view)
    else:
        view.add_item(item=offline)
        await ctx.channel.send(f"```py\n{err}```", view=view)
