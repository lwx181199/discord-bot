# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:34:47 2022

@author: lwuil
"""

import discord
import nest_asyncio
nest_asyncio.apply()
from discord.ext import commands

client = discord.Client()


bot=commands.Bot(command_prefix="&")
"""@client.event
async def on_message(message):
    if message.content == "Re" :
        await message.channel.send("Nard")
    if message.content == "Ping" :
        await message.channel.send("Pong")
    if message.content == "Quoi" :
        await message.channel.send("Feur")"""

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()

bot.run("OTc1NjkzODUzMDk0OTkzOTMw.G_vdgS._RXBUi2DNclMeK6FkH9UT-miFeSzrpENzjdRfI")
#client.run("OTc1NjkzODUzMDk0OTkzOTMw.G_vdgS._RXBUi2DNclMeK6FkH9UT-miFeSzrpENzjdRfI")
