from src.process import *
from src.error import *
from src.embed import *
from src.view import *

async def traceroute (ctx,args):
    
    if len(args) != 1 :
        print("Missing Required Argument")
        await ctx.channel.send(embed=CompleteEmbed("Error"
            ,f"Missing Required Argument. \n \n You should use the **traceroute** command with domain \
                or IPv4 or IPv6 like this : \n \n Domain: \n`.traceroute google.com` \n IPv4:\n`.traceroute 1.1.1.1`\n \
                    IPv6: \n`.traceroute 2606:4700:4700::1111`",0xFF0000))
        return
    
    ip=args[0]
    print("Traceroute for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    
    await ctx.channel.send(embed=CompleteEmbed("Traceroute", f"Traceroute **{ip}** in progress ...", 0x00FF00))
    msg2= await ctx.channel.send(":hourglass:")

    try:
        await execute_prog_realtime(f"traceroute {ip}", 20, msg2)

    except TimeoutError:
        print("Timeout")
        await ctx.channel.send(embed=CompleteEmbed("Timeout", f"➜ Timeout for **{ip}**", 0xFF0000), view=simple_view("offline"))
        return
    except ErrorDuringProcess as err:
        print(f"Error code: {err.code}")
        await msg2.delete()
        await ctx.channel.send(embed=CompleteEmbed("Error", f":warning: **Error {err.code}** occured during process for **{ip}** :warning:",0xFF0000), view=simple_view("offline"))
        return
    else:
        await msg2.edit(view=simple_view("online"))
