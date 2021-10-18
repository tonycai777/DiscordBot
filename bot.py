from discord.ext import commands

bot = commands.Bot(command_prefix="\\")

bot.load_extension("pingpong")
bot.load_extension("blackjack")
bot.load_extension("ytsearch")

bot.run("ODk4MzgzMDEyMzQ0MDA0NjE5.YWjaYQ.3_e2ehvAZNGJLRnR2BaxnUc10JM")