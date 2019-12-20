from discord.ext import commands
import os
import traceback
import random
import csv
import numpy as np

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
    hifumi=np.random.choice(numbers)+np.random.choice(numbers)+np.random.choice(numbers)+np.random.choice(numbers)
    if hifumi[3]==numbers[0]:
        hifumi=hifumi[:3]+"初"
    hifumin="加藤"+hifumi+"段"
    await ctx.send(hifumin)

@bot.command()
async def senryu(ctx):
    nya=[]
    senryu=""
    with open("senryu.csv","r") as f:
        tmp=csv.reader(f)
        for i in tmp:
            nya.append(i)
    senryu=np.random.choice(nya[0])+np.random.choice(nya[1])+np.random.choice(nya[0])
    await ctx.send(senryu)

@bot.command()
async def senryu10ren(ctx):
    nya=[]
    senryu10ren=[]
    with open("senryu.csv","r") as f:
        tmp=csv.reader(f)
        for i in tmp:
            nya.append(i)
    for i in range(10):
        senryu10ren.append("".join((np.random.choice(nya[0])+np.random.choice(nya[1])+np.random.choice(nya[0])])))
    await ctx.send("\n".join(senryu10ren))

bot.run(token)
