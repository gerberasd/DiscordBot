import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
   if message.content.startswith('!334'):
        slot_list = ['3', '3', '4']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        await client.send_message(message.channel, "%s%s%s" % (A, B, C))

client.run('とーくん')