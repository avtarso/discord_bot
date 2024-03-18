import os
import discord
from discord.ext import commands
from replace import abc_replace
# from ttt import TicTacToe



intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")


# @bot.command()
# async def tic(ctx: commands.Context):
#     """Starts a tic-tac-toe game with yourself."""
#     await ctx.send("Tic Tac Toe: X goes first", view=TicTacToe())


@bot.event
async def on_member_join(member: discord.Member):
    guild = member.guild
    if guild.system_channel:
        to_send = f"Welcome {member.mention} to {guild.name}!"
        await guild.system_channel.send(to_send)


@bot.event
async def on_message(message):
    replaced_message = abc_replace(message.content)
    # don't respond to ourselves
    if message.author == bot.user:
        return
    elif message.content.lower() == 'ping':
        await message.channel.send('pong')
    elif message.content != replaced_message and message.content != "!tic":
        await message.reply(replaced_message)
        await message.channel.send(f"'{message.content}' fixed to '{replaced_message}'")
    elif message.content.lower().find("привіт") > -1:
        await message.channel.send(f"Привіт, {message.author}")
    elif message.content.lower().find("привет") > -1:
        await message.channel.send(f"Привет, {message.author}")


TOKEN = os.getenv("DISCORD_BOT")

if __name__ == "__main__":
    bot.run(TOKEN)