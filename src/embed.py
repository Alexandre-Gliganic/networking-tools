import discord

def BasicEmbed(title=None, description=None, color=None):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
    return embed

def CompleteEmbed(title=None, description=None, color=None):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_thumbnail(url="https://api.alexandregliganic.fr/folder/serveur.png")
    embed.set_footer(text="By Alexandre Gliganic",
                     icon_url="https://api.alexandregliganic.fr/folder/pp-alex2.jpg")
    return embed