import discord
from discord.ext import commands
from config import TOKEN
from random_think import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def password(ctx):
    await ctx.channel.send("rastgele şifreniz: "+gen_pass(10))    
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f600") 
bot.run(TOKEN)
