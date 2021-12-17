import discord
from discord.ext import commands
import asyncio
from random import *

class blackjack(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = 'bj', description = 'Play crude game of blackjack')
    async def bj(self, ctx: commands.Context):
        # Super basic black jack game

        def cardpull(): # Generates random card
            playerCard = randint(1, 13)
            card = ''
            if playerCard == 1:
                card = 'A'
            elif playerCard == 11:
                card = 'J'
                playerCard = 10
            elif playerCard == 12:
                card = 'Q'
                playerCard = 10
            elif playerCard == 13:
                card = 'K'
                playerCard = 10

            suit = randint(1, 4)
            if suit == 1:
                emote = ':heart:'
            elif suit == 2:
                emote = ':diamonds:'
            elif suit == 3:
                emote = ':clubs:'
            elif suit == 4:
                emote = ':spades:'

            return [playerCard, emote, card]

        message = await ctx.send("Type hit to start")
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel

        try:
            confirm = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await message.edit(content="Game cancelled, timed out.")
            return

        if confirm.content == 'hit':
            playerTot = 0
            computerTot = 0

            while playerTot < 21 and confirm.content == 'hit':
                player = cardpull()
                if player[2] != '':
                    await ctx.send(player[1] + ' ' + str(player[2]))
                else:
                    await ctx.send(player[1] + ' ' + str(player[0]))
                playerTot += player[0]

                if playerTot >= 21:
                    break

                computer = cardpull()
                computerTot += computer[0]
                if computerTot >= 21 and playerTot < 21:
                    break
                
                message = await ctx.send("hit or stand")
                check = lambda m: m.author == ctx.author and m.channel == ctx.channel

                try:
                    confirm = await self.bot.wait_for("message", check=check, timeout=30)
                except asyncio.TimeoutError:
                    await message.edit(content="Game cancelled, timed out.")
                    return
            
            if playerTot == 21 and computerTot != 21:
                winner = 'Player'
            if playerTot > computerTot and playerTot <= 21:
                winner = 'Player'
            elif computerTot > playerTot and computerTot <= 21:
                winner = 'Computer'
            elif playerTot == computerTot and playerTot <= 21:
                winner = 'Tie'
            elif playerTot > 21:
                winner = 'Computer'
            elif computerTot > 21:
                winner = 'Player'

            embed = discord.Embed(title="A game of black jack", description='Winner: ' + winner, colour=0x87CEEB)
            embed.add_field(name="Player Score", value=playerTot, inline=True)
            embed.add_field(name="Dealer Score", value=computerTot, inline=False)
            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(blackjack(bot))