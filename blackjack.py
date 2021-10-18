from discord.ext import commands
import asyncio
from random import *

class blackjack(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = 'bj')
    async def bj(self, ctx: commands.Context):
        # Super basic black jack game
        message = await ctx.send("Type hit to start")
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel

        try:
            confirm = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await message.edit(content="Game cancelled, timed out.")
            return

        if confirm.content == 'hit':
            playerCard = randint(1, 13)
            await ctx.send(playerCard)

def setup(bot: commands.Bot):
    bot.add_cog(blackjack(bot))