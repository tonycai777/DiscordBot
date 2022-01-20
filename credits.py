from discord.ext import commands
import asyncio

class credits(commands.Cog):
    # Everything needed with credits

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="bal", description = 'Checks credits of user')
    async def bal(self, ctx: commands.Context):
        import balance
        yourbal = balance.get_bal(ctx.message.author.id)
        await ctx.send("{} credits".format(yourbal))

    @commands.command(name="updbal", description = 'Changes credits of user [Admin only]')
    async def updbal(self, ctx:commands.Context, *credits):
        import balance
        if ctx.message.author.id == 305584920116592640:
            if not credits:
                message = await ctx.send("Enter credits to add/remove")
                check = lambda m: m.author == ctx.author and m.channel == ctx.channel

                try:
                    confirm = await self.bot.wait_for("message", check=check, timeout=30)
                except asyncio.TimeoutError:
                    await message.edit(content="Command cancelled, timed out.")
                    return

                credits_to_add = confirm.content
            else:
                credits_to_add = credits[0]

            if credits_to_add != '':
                balance.update_bal(ctx.message.author.id, credits_to_add)
            yourbal = balance.get_bal(ctx.message.author.id)
            await ctx.send("You now have {} credits".format(yourbal))
        
        else:
            await ctx.send("Stanvord only :smiley:")

    @commands.command(name="daily", description = 'Gets your daily credits')
    async def daily(self, ctx:commands.Context):
        import balance
        balance.update_bal(ctx.message.author.id, 1000)
        yourbal = balance.get_bal(ctx.message.author.id)
        await ctx.send("You now have {} credits".format(yourbal))

def setup(bot: commands.Bot):
    bot.add_cog(credits(bot))