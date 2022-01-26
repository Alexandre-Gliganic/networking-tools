from src.process import *
from src.error import *
from src.regex import whatis
from src.embed import *
from src.view import *
import os 

async def whois (ctx,args):
    
    if len(args) != 1 :
        print("Missing Required Argument")
        await ctx.channel.send(embed=CompleteEmbed("Error","Missing Required Argument. \n \n You should use the **whois** command with IPv4 \
            or IPv6 like this : \n \n IPv4:\n`.whois 1.1.1.1`\n IPv6: \n`.whois 2606:4700:4700::1111`",0xFF0000))
        return
    
    ip=args[0]
    print("Whois for", ip, "request by", ctx.author.name,f"(ID = {ctx.author.id}).")

    await ctx.channel.send(embed=CompleteEmbed("Whois",f"Whois **{ip}** in progress ...",0x00FF00))
    msg2= await ctx.channel.send(":hourglass:")
    
    
    version=await whatis(ip)
    if version=="v4" or version == "v6" or version == "AS":
        flag="-r"
    
    elif version == "url":
        flag=""
    else:
        await msg2.delete()
        await ctx.channel.send(embed=CompleteEmbed("Error","Missing Required Argument. \n \n You should use the **whois** command with IPv4 \
            or IPv6 like this : \n \n IPv4:\n`.whois 1.1.1.1`\n IPv6: \n`.whois 2606:4700:4700::1111`",0xFF0000))
        return

    try:
        res,err=await execute_prog(f"whois {flag} {ip}", 10)

    except TimeoutError:
        print("Timeout")
        await ctx.channel.send(embed=CompleteEmbed("Timeout",f"➜ Timeout for **{ip}**",0xFF0000), view=simple_view("offline"))
        return
    except ErrorDuringProcess as err:
        print(f"Error code: {err.code}")
        await msg2.delete()
        await ctx.channel.send(embed=CompleteEmbed("Error",f":warning: **Error {err.code}** occured during process \
            for **{ip}** :warning:", 0xFF0000), view=simple_view("offline"))
        return
    
    else:
        filter_res = ""
        if version != "url":
            for line in res.splitlines()[9:]: #remove the 10 lines of information whois function 
                if not line.startswith('remarks:'): #remove comments
                    filter_res+=line+'\n'  
        else:
            cpt_lines=0
            for line in res.splitlines():
                filter_res+=line+'\n'
                if line.startswith('source'):#remove the 10 lines of information whois function 
                    cpt_lines+=1
                if cpt_lines == 2:
                    break
            fileip=ip.replace("/","_")
            f= open(f"files/{fileip}.txt","w")
            f.write(filter_res)
            f.close()
            await msg2.delete()
            await ctx.channel.send(file=discord.File(f"files/{fileip}.txt",filename=f"whois {fileip}.txt"))
            os.remove(f"files/{fileip}.txt") 
            return
        
        find=res.find("ERROR:") #detect error101 for button
        print(find)
        if find == -1:
            await msg2.edit(f"```py\n{filter_res}```",view=simple_view("online"))
            return
            
        else:
            await msg2.delete()
            await ctx.channel.send(embed=CompleteEmbed("Error",f"➜ No entries found in source RIPE for **{ip}**.",0xFF0000), view=simple_view("offline"))
            return
            
