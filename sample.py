import discord
import random
import asyncio

client = discord.Client() # 接続に使用するオブジェクト

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_reaction_add(reaction, user):
    # author・・・リアクションがついたメッセージを書いた人
    author = reaction.message.author
    await client.send_message(author, f"{user} さんがリアクションをしました")

@client.event
async def on_message(message):
    if message.content.startswith('指定コマンドに変えてください'):
        reply = '''
こ
　ん
　　な
　　　感
　　　　じ
　　　　　で
　　　　　改
　　　　行
　　　で
　　き
　ま
す

↓ソースコードも表示できます↓
```python
import discord #おまじない

client = discord.Client() #おまじない

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
        # メッセージが送られてきたチャンネルへHelloWorld!と送信
        await client.send_message(message.channel, m)

client.run("とーくんをここにはりつけ") #トークンを貼り付けて下さい
```
                '''
        await client.send_message(message.channel, reply)

    if message.content.startswith("指定コマンドに変えてください"): # 指定チャンネルへ発言
        channel = client.get_channel('チャンネルIDをここへ')
        m = "@everyone 通話中！参加者募集中です。聞き専でもどうぞ！"
        await client.send_message(channel, m)

    if message.content.startswith('指定コマンドに変えてください'): # 会話全削除
        clean_flag = True
        while (clean_flag):
            msgs = [msg async for msg in client.logs_from(message.channel)]
            if len(msgs) > 1: # 1発言以下でdelete_messagesするとエラー
                await client.delete_messages(msgs)
            else:
                clean_flag = False
                await client.send_message(message.channel, 'ログの削除が完了しました')

    if message.content.startswith("指定コマンドに変えてください"): # 課題曲サンプル
        number = random.randint(1,2)
        if number == 1:         
            reply = 'Opfer(オンゲキ)'
            await client.send_message(message.channel, reply)
        else:        
            reply = 'Titania(オンゲキ)'
            await client.send_message(message.channel, reply)

client.run('トークンをここに')