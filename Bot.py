import discord
import asyncio
from discord.ext import commands
import sqlite3


#Younes RM Code Section

with sqlite3.connect("BotDB.db") as db: 
    c = db.cursor()
client = discord.Client()



@client.event
async def on_message(message):
  
    if message.author == client.user:
        return
      

    if message.content.startswith('!register'):
        ma = message.author
        await usm.kk(ma)
        await sendmsg(ma ,dm)
     



    
    
@client.event  
async def sendmsg(ma, msg):
    await client.send_message(ma, msg) 
    
    
#Younes RM Code Section End



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  
client.run('NTA1MTYyODI0MjEzODU2MjU2.DrRxzA.AejgQIuwCIx6WGIZBFv0H-fGHrA')