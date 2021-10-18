from discord.ext import commands
from datetime import datetime
import requests, asyncio, discord

api_key = 'ee140fb6371b91d5d4a64af8d97e6e50'

class weather(commands.Cog):
    # Weather checker!

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx: commands.Context):

        message = await ctx.send("Enter a city")
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel

        try:
            confirm = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await message.edit(content="Search cancelled, timed out.")
            return

        if confirm.content != '':
            city_name = confirm.content
            city_name = str.title(city_name)
        complete_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key

        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":

            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = round((current_temperature - 273.15)* 1.8000 + 32.00)

            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = weather_description.capitalize()

            embed = discord.Embed(title="Weather in " + city_name, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="Weather", icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/282/sun-behind-small-cloud_1f324-fe0f.png")
            embed.add_field(name="Temperature (in Fahrenheit)", value=current_temperature, inline=True)
            embed.add_field(name="Description", value=weather_description, inline=False)
            await ctx.send(embed=embed)

        else:
            await ctx.send("`City Not Found`")

def setup(bot: commands.Bot):
    bot.add_cog(weather(bot))