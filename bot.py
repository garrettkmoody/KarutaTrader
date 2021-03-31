# bot.py
import os
import random
import discord
from discord.ext import commands
TOKEN = "ODI2NzE1MDUxMDE1Nzk4Nzk0.YGQgYw.h5cxPUt_djPTsHt2Lnev0TIwuUw"
GUILDNUM = "706297495122214984"
client = discord.Client()
bot = commands.Bot(command_prefix='x')
bot.remove_command('help')
lastMessage = None
lastEmbed = None
replace = None


async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILDNUM:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.command(name="trade")
async def trade(ctx, arg1, arg2, arg3, arg4):
    global lastMessage
    global lastEmbed
    global replace
    if arg4 == 'b':
        embedVar = discord.Embed(title="Trade Outline", color=0xFF9900)
        embedVar.add_field(name=ctx.author, value="***PRICE*** : `${}`".format(arg3), inline=False)
        replace = embedVar.add_field(name="No User Selected", value="***CARD*** : `{}`".format(arg1), inline=False)
        await ctx.send("Beginning a trade: \n")
        theMessage = await ctx.send(embed=embedVar)
        lastEmbed = embedVar
        lastMessage = theMessage
        await theMessage.add_reaction("💳")
    elif arg4 == 'a':
        print("holder")
    else:
        await ctx.send("Please enter a `b` for BID or `a` for ASK")

@bot.event
async def on_reaction_add(reaction, user):
  global lastEmbed
  if user == bot.user:
      return
  if reaction.emoji == '💳':
    lastEmbed.fields[1] = None
    lastEmbed.add_field(name=user, value="***CARD*** : `{}`".format("buut"), inline=False)
    await lastMessage.channel.send(embed=lastEmbed)

@bot.command(name="help")
async def help(ctx):
    await ctx.send("Commands available:\n" + "`xtrade <CardCode> <Other user> <Price> <b/a>`")

bot.run(TOKEN)
