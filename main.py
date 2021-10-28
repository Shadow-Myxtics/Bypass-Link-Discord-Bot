import discord
import asyncio
import datetime
import os
import json
import requests
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from blurple import ui
bot = commands.Bot(command_prefix=commands.when_mentioned_or('Prefix'))
bot.remove_command('help')
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Status"))



@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f":x: An error occured: `{str(error)}`")       

@bot.command()
async def help(ctx):
embed = discord.Embed(title="Help", description="`prefix bypass`- Can Bypass Any Link!")
await ctx.send(embed=embed)

##### Bypass COMMAND #####
@bot.command()
async def bypass(ctx, arg):
  r=requests.get('https://adlink-bypass-api.bigbypassalt.repl.co/api?='+arg)
  a = ('%'+r.text)
  chunks = a.split(',')
  dest = chunks[1]
  stripped = dest.split('"')
  #await ctx.send(chunks[1])
  embed = discord.Embed()
  embed.set_thumbnail(url="https://thumbs.gfycat.com/PlainHonestAzurevase-size_restricted.gif")
  embed.add_field(name="Bypassed Link:", value=stripped[3], inline=False)
  await ctx.send(embed=embed)
#End

bot.run("Token")
