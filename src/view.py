import discord

def simple_view(input: str):
    view = discord.ui.View()
    if input == "online":    
        online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
        view.add_item(item=online)
        return view
    if input == "offline":    
        offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
        view.add_item(item=offline)
        return view
    
def v4_view(input: str, domain: str = None):
    view = discord.ui.View()
    if input == "online":    
        online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://{domain}")
        view.add_item(item=online)
        view.add_item(item=website)
        return view
    if input == "offline":    
        offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://{domain}")
        view.add_item(item=offline)
        view.add_item(item=website)
        return view
    
def v6_view(input: str, domain: str = None):
    view = discord.ui.View()
    if input == "online":    
        online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://[{domain}]")
        view.add_item(item=online)
        view.add_item(item=website)
        return view
    if input == "offline":    
        offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
        website = discord.ui.Button(style=discord.ButtonStyle.green, label=f"{domain}", url=f"https://[{domain}]")
        view.add_item(item=offline)
        view.add_item(item=website)
        return view
    
        