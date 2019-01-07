import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # 起動確認

@client.event
async def on_message(message):
    # 「!test」で始まる場合
    if message.content.startswith("!test"):
        m = "HelloWorld!"
        # メッセージが送られてきたチャンネルへメッセージを送る
        await client.send_message(message.channel, m)

client.run("とーくんをここにはりつけ")