from discord.ext import commands

class miscCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="meth")
    async def meth(self, ctx: commands.Context):
        await ctx.send("https://twitter.com/amanopikamee/status/1266350001006899201?s=21")

def setup(bot: commands.Bot):
    bot.add_cog(miscCommand(bot))