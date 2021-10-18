from discord.ext import commands

class weather(commands.Cog):
    # Weather checker!

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx: commands.Context):
        await ctx.send("Its cold :smile:")

def setup(bot: commands.Bot):
    bot.add_cog(weather(bot))