# bot.py
import os
import random
import discord
import keystokens
from coinbase.wallet.client import Client
from tradePackage import TradePackage
from discord.ext import commands
coinClient = Client(keystokens.coinbaseApiKey, keystokens.coinbaseApiSecret)
TOKEN = keystokens.discordToken
GUILDNUM = "706297495122214984"
client = discord.Client()
bot = commands.Bot(command_prefix='x')
bot.remove_command('help')
tradePack = None
lastMessage = None

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
async def trade(ctx, arg1, arg2, arg3):
    global tradePack
    global lastMessage
    if arg3 == 'b':
        await ctx.send("Beginning a trade: \n")
        tradePack = TradePackage(arg2,arg1,ctx.author)
        theMessage = await ctx.send(embed=tradePack.get_embed())
        lastMessage = theMessage
        await theMessage.add_reaction("💳")
    elif arg3 == 'a':
        print("holder")
    else:
        await ctx.send("Please enter a `b` for BID or `a` for ASK")
        await ctx.send("k!d")

@bot.event
async def on_reaction_add(reaction, user):
    global tradePack
    global lastMessage
    if user == bot.user:
        return
    if reaction.emoji == '💳':
        tradePack.set_bidderName(user)
        await lastMessage.edit(embed=tradePack.get_embed(1))
        await lastMessage.channel.send(embed=tradePack.get_embed(2))

@bot.command(name="help")
async def help(ctx):
    await ctx.send("Commands available:\n" + "`xtrade <CardCode> <Price> <b/a>`")

bot.run(TOKEN)
