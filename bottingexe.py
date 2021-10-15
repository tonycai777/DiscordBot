import discord
import random

client = discord.Client()
prefix = '\\'

@client.event
async def on_ready():
    print('Started {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('`Hello!`')

    if message.content.startswith(prefix + 'help'):
        await message.channel.send('`You made this, you need help?`')

    if message.content.startswith(prefix + 'img'):
        char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz'
        link = ''
        for len in range(5):
            link += char[random.randint(0, 51)]
        await message.channel.send('https://i.imgur.com/' + link + '.jpg')

client.run('ODk4MzgzMDEyMzQ0MDA0NjE5.YWjaYQ.3_e2ehvAZNGJLRnR2BaxnUc10JM')
