import discord
from discord.ext import commands


token = "TOKEN_HERE"
prefix = "PREFIX_HERE"

client = commands.Bot(command_prefix= prefix)
client.remove_command("help")


@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client))
    activity = discord.Game(name="yar help", type=3)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
