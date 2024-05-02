import discord
from function import gen_pass , coin_toss , gen_emo 



# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$new pass'):
        await message.channel.send(gen_pass(8))
    elif message.content.startswith('$coin toss'):
        await message.channel.send(coin_toss)
    elif message.content.startswith('$random emo'):
        await message.channel.send(gen_emo())
    else:
        await message.channel.send(message.content)

client.run("Токен")
