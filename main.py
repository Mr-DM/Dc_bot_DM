import discord
from discord.ext import commands
from function import gen_pass , coin_toss , gen_emo 
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def coin_flip(ctx):
    await ctx.send(coin_toss())

@bot.command()
async def new_pass(ctx):
    await ctx.send(gen_pass(8))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emo())

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def my_code(ctx):
    await ctx.send('https://github.com/Mr-DM/Dc_bot_DM')

@bot.command()
async def helps(ctx):  
    await ctx.send(f'В боте {bot.user} есть функцы как (hello, coin_flip, new_pass, emoji, my_code, repeat, helps) не забудь в начале $ ')


@bot.command()
async def mem(ctx):
    # А вот так можно подставить имя файла из переменной!
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:   
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)




def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("Токен")
