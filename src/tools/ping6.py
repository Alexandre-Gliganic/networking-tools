from src.process import *
from src.error import *
from src.regex import whatis
from src.embed import *
from src.view import *


async def ping6(ctx,args):
    
    if len(args) != 1:
        print("Missing Required Argument")
        await ctx.channel.send(embed=CompleteEmbed("Error","Missing Required Argument. \n \n You should use the **ping6** command with domain \
            or IPv6 like this : \n \n Domain: \n`.ping6 google.com` \n IPv6: \n`.ping6 2606:4700:4700::1111`",0xFF0000))
        return
    
    ip=args[0]

    ip_detect = await whatis(ip)
    match ip_detect:
        case "v4":
            version = 4
            await ctx.channel.send(embed=CompleteEmbed("Error","Missing Required Argument. \n \n You should use the **ping6** command with domain \
            or IPv6 like this : \n \n Domain: \n`.ping6 google.com` \n IPv6: \n`.ping6 2606:4700:4700::1111`",0xFF0000))
            return
        case "v6":
            version = 6
        case "url":
            version = 42
        case _ :
            version = 0
            await ctx.channel.send(embed=CompleteEmbed("Error","Missing Required Argument. \n \n You should use the **ping6** command with domain \
            or IPv6 like this : \n \n Domain: \n`.ping6 google.com` \n IPv6: \n`.ping6 2606:4700:4700::1111`",0xFF0000))
            return
            
                  
    print("Ping6 for", ip, f"with IPv6", "request by", ctx.author.name,f"(ID = {ctx.author.id}).")
    await ctx.channel.send(embed=CompleteEmbed("Ping6", f"Ping6 for **{ip}** with **IPv6** in progress ...", 0x00FF00))
    msg2= await ctx.channel.send(":hourglass:")

    try:
        await execute_prog_realtime(f"ping -6 -c 5 {ip}", 8, msg2)
       
    except TimeoutError:
        print("Timeout")
        await msg2.delete()
        await ctx.channel.send(embed=CompleteEmbed("Timeout", f"➜ Timeout for **{ip}**", 0xFF0000), view=v4_view('offline',ip) if version == 42 else v6_view('offline',ip))
        return
    
    except ErrorDuringProcess as err:
        if err.code!=1:
            await msg2.delete()
        print(f"Error code: {err.code}")
        await ctx.channel.send(embed=CompleteEmbed(f"Error {err.code}", f"➜ {err.err if len(err.err) != 0 else 'Error occured'}", 0xFF0000), \
            view=v4_view('offline',ip) if version == 42 else v6_view('offline',ip))
        return
    else:
        await msg2.edit(view=v4_view('online',ip) if version == 42 else v6_view('online',ip))