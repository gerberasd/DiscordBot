import discord
import random
import asyncio

client = discord.Client() # �ڑ��Ɏg�p����I�u�W�F�N�g

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_reaction_add(reaction, user):
    # author�E�E�E���A�N�V�������������b�Z�[�W���������l
    author = reaction.message.author
    await client.send_message(author, f"{user} ���񂪃��A�N�V���������܂���")

@client.event
async def on_message(message):
    if message.content.startswith('�w��R�}���h�ɕς��Ă�������'):
        reply = '''
��
�@��
�@�@��
�@�@�@��
�@�@�@�@��
�@�@�@�@�@��
�@�@�@�@�@��
�@�@�@�@�s
�@�@�@��
�@�@��
�@��
��

���\�[�X�R�[�h���\���ł��܂���
```python
import discord #���܂��Ȃ�

client = discord.Client() #���܂��Ȃ�

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # �N���m�F

@client.event
async def on_message(message):
    # �u!test�v�Ŏn�܂�ꍇ
    if message.content.startswith("!test"):
        m = "HelloWorld!"
        # ���b�Z�[�W�������Ă����`�����l����HelloWorld!�Ƒ��M
        await client.send_message(message.channel, m)

client.run("�Ɓ[����������ɂ͂��") #�g�[�N����\��t���ĉ�����
```
                '''
        await client.send_message(message.channel, reply)

    if message.content.startswith("�w��R�}���h�ɕς��Ă�������"): # �w��`�����l���֔���
        channel = client.get_channel('�`�����l��ID��������')
        m = "@everyone �ʘb���I�Q���ҕ�W���ł��B������ł��ǂ����I"
        await client.send_message(channel, m)

    if message.content.startswith('�w��R�}���h�ɕς��Ă�������'): # ��b�S�폜
        clean_flag = True
        while (clean_flag):
            msgs = [msg async for msg in client.logs_from(message.channel)]
            if len(msgs) > 1: # 1�����ȉ���delete_messages����ƃG���[
                await client.delete_messages(msgs)
            else:
                clean_flag = False
                await client.send_message(message.channel, '���O�̍폜���������܂���')

    if message.content.startswith("�w��R�}���h�ɕς��Ă�������"): # �ۑ�ȃT���v��
        number = random.randint(1,2)
        if number == 1:         
            reply = 'Opfer(�I���Q�L)'
            await client.send_message(message.channel, reply)
        else:        
            reply = 'Titania(�I���Q�L)'
            await client.send_message(message.channel, reply)

client.run('�g�[�N����������')