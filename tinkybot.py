# bot.py
import os
import random

import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="seg2911", help="Send a picture of a page of the mat2377 textbook")
async def seg2911(ctx):
    sched = "```SEG2911(Ethics) E00/E01 \n  Lecture:  Thursday, 7:00PM - 9:50PM \n  Tutorial: Monday, 1:00PM - 2:20PM```"
    await ctx.send(sched)

@bot.command(name="seg2106", help="Send a picture of a page of the mat2377 textbook")
async def seg2106(ctx):
    sched = "```SEG2106(Soft. Construction) B00/B01 \n  Lecture 1: Wednesday, 4:00PM - 5:20PM \n  Lecture 2: Friday, 2:30PM - 3:50PM \n  Lab: Tuesday, 11:30AM - 2:20PM```"
    await ctx.send(sched)

@bot.command(name="csi2132", help="Send a picture of a page of the mat2377 textbook")
async def csi2132(ctx):
    sched = "```CSI2132(Databases) B00/B01/B05 \n  Lecture 1: Wednesday, 1:00PM - 2:20PM \n  Lecture 2: Friday, 11:30AM - 12:50PM \n  Lab (B01): Monday, 2:30PM - 3:50PM \n  Tutorial (B05): Monday, 4:00PM - 5:20PM```"
    await ctx.send(sched)

@bot.command(name="mat2377", help="Send a picture of a page of the mat2377 textbook")
async def mat2377(ctx, page: int = -1):
    if(page == -1):
        sched = "```MAT2377(Stats) A00 \n  Lecture 1: Monday, 10:00AM - 11:20AM \n  Lecture 2: Thursday, 8:30AM - 9:50AM```"
        await ctx.send(sched)
    elif(0<page<468):
        if(page>=84):
            fileName = "./mat2377/0001-"+str(page+16)+".jpg"
        else:
            fileName = "./mat2377/0001-0"+str(page+16)+".jpg"
        await ctx.send(file=discord.File(fileName))

@bot.command(name="csi2101", help="Send a picture of a page of the csi2101 textbook")
async def csi2101(ctx, page: int = -1):
    if(page == -1):
        sched = "```CSI2101(Disrete Structs.) B00/B01 \n  Lecture 1: Wednesday, 10:00AM - 11:20AM \n  Lecture 2: Friday, 8:30AM - 9:50AM\n  Tutorial:  Thursday, 5:30PM - 6:50PM```"
        await ctx.send(sched)
    elif(0<page<1051):
        filename = ""
        if(page>=979):
            fileName = "./csi2101/0001-"+str(page+21)+".jpg"
        elif(page>=79):
            fileName = "./csi2101/0001-0"+str(page+21)+".jpg"
        else:
            fileName = "./csi2101/0001-00"+str(page+21)+".jpg"
        await ctx.send(file=discord.File(fileName))


bot.run(TOKEN)