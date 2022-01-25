from src.process import *
from src.error import *
from src.embed import *
from src.view import *

async def dig (ctx,args):
    
    if len(args) != 1:
        print("Missing Required Argument")
        await ctx.channel.send(embed=CompleteEmbed("Error", "Missing Required Argument. \n \n You should use the \
            **dig** command with IPv4 or IPv6 like this : \n \n IPv4:\n`.dig 1.1.1.1`\n IPv6: \n`.dig 2606:4700:4700::1111`", 0xFF0000))
        return
    
    ip=args[0]
    print("Dig for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")

    await ctx.channel.send(embed=CompleteEmbed("Dig", f"Dig **{ip}** in progress ...", 0x00FF00))
    msg2= await ctx.channel.send(":hourglass:")
        
    try:
        res,err=await execute_prog(f"dig +short -x {ip}", 10)

    except TimeoutError:
        print("Timeout")
        await ctx.channel.send(embed=CompleteEmbed("Timeout", f"➜ Timeout for **{ip}**", 0xFF0000), view=simple_view("offline"))
        return
    except ErrorDuringProcess as err:
        print(f"Error code: {err.code}")
        await msg2.delete()
        await ctx.channel.send(embed=CompleteEmbed(f"Error {err.code}",f"➜ Dig **{ip}** not found.",0xFF0000), view=simple_view("offline"))
        return
        
    else:
        if len(res) != 0:
            await msg2.edit(f"```py\n{res}```", view=simple_view("online"))
            return
        else:
            await msg2.delete()
            await ctx.channel.send(embed=CompleteEmbed("Error",f"➜ Dig **{ip}** not found.",0xFF0000), view=simple_view("offline"))
            return