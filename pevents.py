from discord.ext import commands
from datetime import datetime
import discord

class PEvents(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="pevent", description = 'Displays upcoming Pokemon Masters events')
    async def pevent(self, ctx: commands.Context):
        # Get current time as yyyy-mm-dd hh:mm:ss UTC
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

        # Open rumors.txt and read it into a list
        with open('rumors.txt', 'r', encoding='utf-8') as f:
            rumors = f.readlines()

        # Remove newline characters in rumors
        for i in range(len(rumors)):
            rumors[i] = rumors[i].strip()

        embed = discord.Embed(title="Upcoming Pokemon Masters Events:", color=0xFF0000, timestamp=datetime.utcnow())
        embed.set_author(name = '')

        # If index % 5 == 2, check if the event is in the future. If not, add it to the embed.
        count = 0
        for i in range(len(rumors)):
            if i % 5 == 2:
                if now < rumors[i]:
                    # Do not add if contains scout or Scout
                    if 'scout' not in rumors[i-2] and 'Scout' not in rumors[i-2]:
                        # Get time difference between now and the event
                        time_diff = datetime.strptime(rumors[i], '%Y-%m-%d %H:%M:%S UTC') - datetime.strptime(now, '%Y-%m-%d %H:%M:%S UTC')
                        embed.add_field(name=rumors[i-2], value='Starting: ' + rumors[i] + '\nIn: ' + str(time_diff))
                        count += 1

        # If no events are found, add a message to the embed
        if count == 0:
            embed.add_field(name="No upcoming events found", value="Check https://github.com/pm-events/pm-events.github.io/ if there are any new leaks")

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(PEvents(bot))