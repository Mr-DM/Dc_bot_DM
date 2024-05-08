import discord
from discord.ext import commands
from function import gen_pass , coin_toss , gen_emo 

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

bot.run("Токен")
