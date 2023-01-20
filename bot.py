# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:34:47 2022

@author: lwuil
"""

import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand


import nest_asyncio
import asyncio
nest_asyncio.apply()
import youtube_dl
import random

bot = commands.Bot (command_prefix="&")
slash = SlashCommand(bot, sync_commands = True)
musics = {}
ytdl = youtube_dl.YoutubeDL()



status = ["Bangtan, hello we are BTS", "8 makes one Team", "17 makes 3 sub-units, 13 members and 1 group", "To The World", "Shinee is back", "We are One",
          "Tentastic, hello we are Pentagon", "To be sensation", "Best We The Boyz", "In X, Hello We're CIX", "Find your TREASURE! Hello, we're Treasure!",
          "Hapiness! Hello we are Red velvet!","One! Dream! Hello we are Tomorrow by together!"]

@bot.event
async def on_ready():
    print("Ready !")
    changeStatus.start()
    


@slash.slash(name="clear", guild_ids=[916020670352199731,895736754626248724],description="Supprime un nombre de messages donné par l'user (seulement pour le staff)")
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre).flatten()
    for message in messages :
        await message.delete()
        
    await ctx.send(f"{nombre} messages ont été supprimé")
        
@slash.slash(name="kick",guild_ids=[916020670352199731,895736754626248724], description="Kick un membre (seulement pour le staff)")
async def kick (ctx, user : discord.User):
        await ctx.guild.kick (user)
        await ctx.send(f"{user} a été kick.")

    
@slash.slash(name="ban",guild_ids=[916020670352199731,895736754626248724], description="Ban un membre (seulement pour le staff)")
async def ban (ctx, user : discord.User):
    await ctx.guild.ban(user)
    await ctx.send(f"{user} a été ban.")

@slash.slash(name="user",guild_ids=[916020670352199731,895736754626248724], description="Renvoie le pseudo général Discord d'un membre")
async def hello (ctx, user : discord.User):
    await ctx.send(f"Le pseudo général de ce membre est : {user}")

@slash.slash(name="serverinfo",guild_ids=[895736754626248724], description="Renvoie les infos sur le serveur en général" )
async def serverInfo (ctx):
    server = ctx.guild 
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfMembers = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfMembers}* membres. \n Le serveur contient {numberOfTextChannels} salons textuels ainsi que {numberOfVoiceChannels} salons vocaux."
    await ctx.send(message)
    
@tasks.loop(minutes=180)
async def my_background_task():
    channel = bot.get_channel(925488200733044776) # Get the channel, the id has to be an int
    rolechannel=bot.get_channel(971382408219881482)
    colorchannel=bot.get_channel(956848904924692520)
    presentationchannel=bot.get_channel(1041689575636082719)
    message = f"Si ce n'est pas encore fait, n'oublie pas de prendre tes rôles dans {rolechannel} !\nTu peux également choisir la couleur de ton pseudo dans {colorchannel} et faire ta présentation dans {presentationchannel} !"
    await channel.send(message)
    
@tasks.loop(seconds = 120)
async def changeStatus():
    await bot.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.listening,name=random.choice(status)))
    

@my_background_task.before_loop
async def my_background_task_before_loop():
    await bot.wait_until_ready()
    

    
my_background_task.start()




    
        
    
bot.run("MTAzMzcxODYxNjYyMjkxMTU1OQ.GxWKb3.dLnpX8Ru4ZlzQ_9Sn4M0yZNfGApX18C1Y0sC7Y")

    

