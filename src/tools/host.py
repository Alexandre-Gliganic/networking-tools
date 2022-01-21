import discord
import subprocess

async def host (ctx,args):
    
    if len(args)==0 or len(args) >1:
        print("Missing Required Argument")
        embed=discord.Embed(title="Error", description = "Missing Required Argument. \n \n You should use the **host** command with domain like this : \n \n Domain:\n`.host google.com`",color=0xFF0000)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.channel.send(embed=embed)
        return
    
    ip=args[0]
    print("Host for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    domaine=str(ip)

    view = discord.ui.View()    
    offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
    online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
    

    waiting1 = ("Host " + domaine)
    await ctx.channel.send(f"```py\n{waiting1} in progress ...```")
        
    try:
        p = subprocess.run(["host", domaine],capture_output=True, text=True, timeout=10)
        

    except subprocess.TimeoutExpired:
        print("Timeout")
        view.add_item(item=offline)
        await ctx.channel.send(f"```py\nTimeout for {domaine}```", view=view)
        return

   
    res = str(p.stdout)
    err = p.stderr

    find = res.find("not found")
    if find == -1:
        view.add_item(item=online)
        await ctx.channel.send(f"```py\n{res}```", view=view)
    else:
        view.add_item(item=offline)
        await ctx.channel.send(f"```py\n{res}```", view=view)
