# Import commands from discord
import discord
from discord.ext import commands

# Import bot token
from apikey import *

intents = discord.Intents.default()
intents.members = True

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '!',intents=intents)

# Tell us that the bot is ready for commands
@client.event
async def on_ready():
   print("The bot is now ready for use")
   print("----------------------------")

# What the user will type to call an action 
# ctx takes the input from discord
@client.command()
async def hello(ctx):
   await ctx.send("Hello! I am bot programmed by Owen as a project for his resume! I hope you enjoy!")

# Show the user what commands are available
@client.command()
async def commands(ctx):
   await ctx.send("Here are a list of the commands you can run!\nhello\ncommands\n!join\n!leave\n")

# Welcomes a user with a message when they join the server
@client.event
async def on_member_join(member):
   channel = client.get_channel(1177031719422021702)
   await channel.send("Welcome to Odogs Server! Use !commands to see what you can do!")

# Sends the server a goodbye message when soemone leaves the server
@client.event
async def on_member_remove(member):
   channel = client.get_channel(1177031719422021702)
   await channel.send("Sad to see you go :(")

# If user is in a channel, get channel ID and join the channel
@client.command(pass_context = True)
async def join(ctx):
   if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      await channel.connect()
   else:
      await ctx.send("You are not in a voice channel")

# If bot is in a voice channel, then run the following commands
@client.command(pass_context = True)
async def disconnect(ctx):
   if (ctx.voice_client):
      await ctx.guild.voice_client.disconnect()
      await ctx.send("Disconnected")
   else:
      await ctx.send("Not in a voice channel")



client.run(BOTTOKEN)
