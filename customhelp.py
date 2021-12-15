from discord.ext import commands
from datetime import datetime
import discord

class customhelp(commands.Cog):
    # Custom help command

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx: commands.Context, *args):
        embed = discord.Embed(title="Commands ", colour=0x87CEEB, timestamp=datetime.utcnow())
        embed.add_field(name="Fun", value='ping\nttt\nbj')
        embed.add_field(name="Information", value= "weather\nvideo")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(customhelp(bot))