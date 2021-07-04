# Discord Imports
import discord
from discord.ext import commands
from discord.ext.commands import Context

# CMC Imports
from lib.cmc import cmc_client
from lib.helpers import embedMessagesHelper

import os

TEST_MODE = os.environ.get('TEST_MODE', False)
DISCORD_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

client = commands.Bot(command_prefix = commands.when_mentioned_or('.'))

@client.event
async def on_ready():
    print("Discord Bot is ready")
    activity = discord.Activity(type=discord.ActivityType.playing, name="Waiting for your commands.")
    await client.change_presence(activity=activity)

@client.command()
async def about(ctx: Context):
    title = "Crypto Bot"
    description = "Serving with many features for your crypto interests!"
    embeddedMessage = discord.Embed(title = title, description = description)

    await ctx.send(embed = embeddedMessage)

@client.command()
async def commands(ctx: Context):
    commandFile = open("/app/src/command_text/commands.txt", "r")
    commandsFromFile = commandFile.read()

    title = "Overview of all commands"
    description = commandsFromFile

    embeddedMessage = discord.Embed(title = title, description = description)
    await ctx.send(embed = embeddedMessage)

@client.command()
async def setup(ctx: Context, function, value):
    await ctx.send(embed = embeddedMessage)

@client.command(aliases=['cp'])
async def cmcPrice(ctx: Context, symbolName):

    tokenInformation = cmc_client.informationForCryptoBySymbolName(symbolName)
    title = "Market Information for Token " + tokenInformation['name']

    if TEST_MODE:
        print(tokenInformation)

    quote = tokenInformation['quote']['USD']

    embeddedMessage = discord.Embed(title = title)
    embeddedMessage = embedMessagesHelper.addFieldsFromDataByMap(quote, embeddedMessage)
    embeddedMessage.set_footer(text = 'Last update on CoinMarketCap for this coin on: ' + quote['last_updated'])

    await ctx.send(embed = embeddedMessage)

client.run(DISCORD_TOKEN)