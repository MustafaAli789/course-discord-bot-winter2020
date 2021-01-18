# bot.py
import os
import random
import io
import discord

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

def skewupper(): 
    low = 0
    high = 100
    mode = 80
    return random.triangular(low, high, mode) 
  
def skewlower(): 
    low = 0
    high = 100
    mode = 20
    return random.triangular(low, high, mode) 

# Function to convert into spongemock 
# with more lower case charcters 
def spongemocklower(input_text): 
    output_text = "" 
    for char in input_text: 
        if char.isalpha(): 
            if random.random() >= 0.5: 
                output_text += char.upper() 
            else: 
                output_text += char.lower() 
        else: 
            output_text += char 
    return output_text 

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='sb', help='hah frick u')
async def sb(ctx, text: str = None):

    message = text
    messages = await ctx.channel.history(limit=200).flatten()
    if (text == None or text.strip() == ""):
        #getting latest text message
        for count, msg in enumerate(messages):
            if(msg.content.endswith(".jpg") or msg.content.endswith(".png") or msg.content.endswith(".jpeg")):          
                print("Image - Skip")
            elif (count != 0 and msg.content.strip() != ""):
                message = msg.content
                break

    if (message == None):
        message = "Standard"

    #initializing drawing object, loading image, and translating text to mock
    img = Image.open("./sb.png")
    draw = ImageDraw.Draw(img)
    shadowcolor = "black"
    msg = spongemocklower(message)

    #scaling font to fit inside image
    fontsize = 1
    img_fraction = 0.98
    font = ImageFont.truetype("./impact.ttf", fontsize)

    while font.getsize(msg)[0] < img_fraction*img.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("./impact.ttf", fontsize)

    if (fontsize > 150):
        fontsize = 150
    font = ImageFont.truetype("./impact.ttf", fontsize)
        
    w, h = draw.textsize(msg, font)

    x, y = (img.width-w)/2, 20
    

    draw.text((x-2, y-2), msg, font=font, fill=shadowcolor)
    draw.text((x+2, y-2), msg, font=font, fill=shadowcolor)
    draw.text((x-2, y+2), msg, font=font, fill=shadowcolor)
    draw.text((x+2, y+2), msg, font=font, fill=shadowcolor)
    draw.text((x,y),msg,(255,255,255),font=font)
    
    arr = io.BytesIO()
    img.save(arr, format='PNG')
    arr.seek(0)

    await ctx.send(file=discord.File(arr, 'spongebobify.png'))

@bot.command(name="seg2911", help="Shows scheduke for SEG2911")
async def seg2911(ctx):
    sched = "```SEG2911(Ethics) E00/E01 \n  Lecture:  Thursday, 7:00PM - 9:50PM \n  Tutorial: Monday, 1:00PM - 2:20PM```"
    await ctx.send(sched)

@bot.command(name="seg2106", help="Shows schedule of SEG2106")
async def seg2106(ctx):
    sched = "```SEG2106(Soft. Construction) B00/B01 \n  Lecture 1: Wednesday, 4:00PM - 5:20PM \n  Lecture 2: Friday, 2:30PM - 3:50PM \n  Lab: Tuesday, 11:30AM - 2:20PM```"
    await ctx.send(sched)

@bot.command(name="csi2132", help="Shows schedule of CSI2132 (and send a pic if flippin ali added the db)")
async def csi2132(ctx):
    sched = "```CSI2132(Databases) B00/B01/B05 \n  Lecture 1: Wednesday, 1:00PM - 2:20PM \n  Lecture 2: Friday, 11:30AM - 12:50PM \n  Lab (B01): Monday, 2:30PM - 3:50PM \n  Tutorial (B05): Monday, 4:00PM - 5:20PM```"
    await ctx.send(sched)

@bot.command(name="mat2377", help="Shows schedule of MAT2377 or sends a picture of a specific page from textbook if specified as arg 0")
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

@bot.command(name="csi2101", help="Shows schedule of csi2101 or sends a picture of a specific page from textbook if specified as arg 0")
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
