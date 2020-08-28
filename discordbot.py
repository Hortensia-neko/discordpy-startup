from discord.ext import commands
import os
import traceback
import random
import csv
import re

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
    hifumi=random.sample(numbers,k=4)
    hifumin="加藤"+"".join(hifumi[:3])+"初段" if hifumi[3]==numbers[0] else "加藤"+"".join(hifumi)+"段"
    res="あ、あなたは伝説の"+hifumin+"！　ここでこんなとは" if hifumi[:3] ==["一","二","三"] else "あなたは"+hifumin+"です"
    await ctx.send(res)

@bot.command()
async def senryu(ctx):
    nya=[]
    senryu=""
    with open("senryu.csv","r") as f:
        tmp=csv.reader(f)
        for i in tmp:
            nya.append(i)
    senryu=random.choice(nya[0])+random.choice(nya[1])+random.choice(nya[0])
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
        senryu10ren.append(random.choice(nya[0])+random.choice(nya[1])+random.choice(nya[0]))
    await ctx.send("\n".join(senryu10ren))

@bot.command()
async def dice(ctx,arg):
    diceSize=list(map(int,re.split("d|D|\+|-",arg)))
    rolled=sorted([random.randint(1,diceSize[1]) for i in range(diceSize[0])])
    deme=sum(rolled)+diceSize[2] if "+" in arg else sum(rolled)-diceSize[2] if "-" in arg else sum(rolled)
    if "+" in arg:
        res=arg+"→"+str(sum(rolled))+str(rolled)+"+"+str(diceSize[2])+"→"+str(deme)
    elif "-" in arg:
        res=arg+"→"+str(sum(rolled))+str(rolled)+"-"+str(diceSize[2])+"→"+str(deme)
    else:
        res=arg+"→"+str(sum(rolled))+str(rolled)+"→"+str(deme)
    await ctx.send(res)

def dxRoll(num,C,res):
    rolled=sorted([random.randint(1,10) for i in range(num)])
    criticaled=list(filter(lambda x:x>=C,rolled))
    tmp=max(rolled)
    if tmp>=C:
        res+=10
        a=dxRoll(len(criticaled),C,res)
        return "10"+"["+"+".join(map(str,rolled))+"]"+"+"+a[0],a[1]
    else:
        res+=tmp
        return [str(tmp)+"["+"+".join(map(str,rolled))+"]",str(res)]
        
def DoubleCross(string):
    tmp=re.split("dx|\+|-|>=",string)
    if tmp[1]=="":
        tmp[1]="10"
    if ("-" in string):
        tmp[2]=str(-int(tmp[2]))
    elif not("+" in string):
        if len(tmp)==2:
            tmp+=["0"]
        else:
            tmp=tmp[:2]+["0",tmp[2]]
    res=dxRoll(int(tmp[0]),int(tmp[1]),int(tmp[2]))
    ans="("+string+")"+"→"+res[0]+tmp[2]+"→"+res[1] if "-" in string else "("+string+")"+"→"+res[0]+"+"+tmp[2]+"→"+res[1]
    if len(tmp)<4:
        return ans
    elif int(tmp[3])<=int(res[1]):
        return ans+">="+tmp[3]+"\n成功"
    else:
        return ans+">="+tmp[3]+"\n失敗"

@bot.command()
async def dx(ctx,arg):
    res=DoubleCross(arg)
    await ctx.send(res)

bot.run(token)
