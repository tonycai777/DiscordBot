from discord.ext import commands
from datetime import datetime
import discord

class customhelp(commands.Cog):
    # Custom help command

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx: commands.Context, *args):
        if not args:
            embed = discord.Embed(title="Commands ", colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.add_field(name="Fun", value='ping\nttt\nbj')
            embed.add_field(name="Information", value= "weather\nvideo")
            embed.add_field(name='Betting', value='bal\ndaily\nroll')
            await ctx.send(embed=embed)
        else:
            command = args[0]
            found = False
            for x in self.bot.cogs:
                cog_command = (self.bot.get_cog(x)).get_commands()
                for y in cog_command:
                    if command == y.name:
                        help=discord.Embed(title=y.name, colour=0x87CEEB, timestamp=datetime.utcnow())
                        for c in self.bot.get_cog(y.cog_name).get_commands():
                            if command == c.name:
                                help.add_field(name='Description',value=c.description, inline=False)
                                help.add_field(name='Inputs',value=f"\\{c.name} {c.signature}", inline=False)
                                if c.help:
                                    help.add_field(name='Examples / Further Help',value=c.help, inline=False)
                        found = True
            
            if found == False:
                help = discord.Embed(title=f'No command with name {command} found',color=discord.Color.red())
            
            await ctx.send(embed=help)

def setup(bot: commands.Bot):
    bot.add_cog(customhelp(bot))