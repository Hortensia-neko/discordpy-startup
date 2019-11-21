from discord.ext import commands
import os
import traceback
import random
import csv

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def hifumin(ctx):
    numbers=["一","二","三","四","五","六","七","八","九"]
    hifumi=numbers[random.randrange(len(numbers))]+numbers[random.randrange(len(numbers))]+numbers[random.randrange(len(numbers))]+numbers[random.randrange(len(numbers))]
    if hifumi[3]==numbers[0]:
        hifumi=hifumi[:3]+"初"
    hifumin="加藤"+hifumi+"段"
    await ctx.send(hifumin)

@bot.command()
async def senryu(ctx):
    with open("senryu5moji.csv") as senryu5:
        

bot.run(token)
