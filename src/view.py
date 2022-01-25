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
    

def website_view(input: str, domaine: str = None):
    view = discord.ui.View()
    if input == "online":    
        online = discord.ui.Button(style=discord.ButtonStyle.green, label="Online")
        view.add_item(item=online)
        return view
    if input == "offline":    
        offline = discord.ui.Button(style=discord.ButtonStyle.red, label="Offline")
        view.add_item(item=offline)
        return view