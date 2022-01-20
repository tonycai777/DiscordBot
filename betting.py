from discord.ext import commands
import asyncio, random

class betting(commands.Cog):
    # Gambling

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="roll", description = 'Roll for more credits')
    async def roll(self, ctx: commands.Context, *amount):
        import balance

        if not amount:
            message = await ctx.send("Enter amount of credits to gamble")
            check = lambda m: m.author == ctx.author and m.channel == ctx.channel

            try:
                confirm = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await message.edit(content="Gamble cancelled, timed out.")
                return
            
            spend = confirm.content
        else:
            spend = amount[0]

        yourbal = balance.get_bal(ctx.message.author.id)
        if int(spend) > int(yourbal):
            await ctx.send("Not enough credits")
            return
        elif int(spend) <= 0:
            await ctx.send("You must use a positive amount of credits")
            return
        
        randnum = random.randrange(0, 100)
        if randnum >= 90:
            balance.update_bal(ctx.message.author.id, spend)
            await ctx.send(f"You win {spend} credits")
        else:
            losespend = int(spend) * -1
            balance.update_bal(ctx.message.author.id, losespend)
            await ctx.send(f"You lose {spend} credits")

def setup(bot: commands.Bot):
    bot.add_cog(betting(bot))