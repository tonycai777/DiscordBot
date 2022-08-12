from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="\\")

@bot.event
async def on_ready():
    print('Launching...')
    CurrentGuildCount = 0
    for _ in bot.guilds:
        CurrentGuildCount += 1
    print('Current Server Count: ' + str(CurrentGuildCount))
    await bot.change_presence(activity=discord.Game(name='Working...'))

bot.remove_command('help')
bot.load_extension("pingpong")
bot.load_extension("blackjack")
bot.load_extension("ytsearch")
bot.load_extension("weather")
bot.load_extension("ErrorHandler")
bot.load_extension("miscCommand")
bot.load_extension("tictac")
bot.load_extension("customhelp")
bot.load_extension("credits")
bot.load_extension("betting")
bot.load_extension("pevents")

bot.run("ODk4MzgzMDEyMzQ0MDA0NjE5.GDVlAF.3YW4sFLf8LWqbw11aFNacADrVW-mW2KJOz865g")