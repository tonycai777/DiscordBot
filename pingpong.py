from discord.ext import commands

class PingPong(commands.Cog):
    # Ping~Pong

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", description = 'Gets the latency to the bot')
    async def ping(self, ctx: commands.Context):
        # Get the bot's current websocket latency.
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

def setup(bot: commands.Bot):
    bot.add_cog(PingPong(bot))