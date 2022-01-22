import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import yaml

from src.tools.ping import ping
from src.tools.traceroute import traceroute
from src.tools.traceroute6 import traceroute6
from src.tools.whois import whois
from src.tools.dig import dig
from src.tools.host import host
from src.tools.help import help

class OnMessage:
    @staticmethod
    async def run(ctx):
        if ctx.author.bot:
            return

        with open('config/config.yml', 'r') as file:
            config = yaml.safe_load(file)


        if ctx.content and ctx.content[0] != config['prefix']:
           return
        
        command = ctx.content.split(' ')[0][1:]
        args = ctx.content.split(' ')[1:]
        
        match command:
            case 'ping':
                await ping(ctx, args)
                return
            case 'traceroute':
                await traceroute(ctx, args)
                return
            case 'traceroute6':
                await traceroute6(ctx, args)
                return
            case 'whois':
                await whois(ctx, args)
            case 'dig':
                await dig(ctx, args)
                return
            case 'host':
                await host(ctx, args)
                return
            case 'help' :
                await help(ctx)
                return
            case _ :
                return
            