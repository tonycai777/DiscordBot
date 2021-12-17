from discord.ext import commands
import asyncio
import urllib.request
import re

class ytsearch(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="video", description = 'Search for 5 videos on YouTube', help = '\\video TF2')
    async def ping(self, ctx: commands.Context, *search):
        #Searches for yt video!

        if not search:
            message = await ctx.send("Enter a search term")
            check = lambda m: m.author == ctx.author and m.channel == ctx.channel

            try:
                confirm = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await message.edit(content="Search cancelled, timed out.")
                return

            if confirm.content != '':
                searchTerm = confirm.content
                searchTerm = searchTerm.replace(' ','+')
        else:
            searchTerm = ''
            for word in search:
                searchTerm += word
        
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchTerm)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        for ind in range(3):
            await ctx.send("https://www.youtube.com/watch?v=" + video_ids[ind])

def setup(bot: commands.Bot):
    bot.add_cog(ytsearch(bot))