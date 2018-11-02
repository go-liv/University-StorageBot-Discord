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
        await rf(ma)
     



    


    
@client.event

async def rf(ma):
    msg = 'Hello, to register please Chose a Username.'
    username = await getmsg(ma, msg)
    if username is None:
        await timesup(ma)
    else:
        msg = 'Thank you. Now please enter a memorable word'
        pw = await getmsg(ma, msg)
        if pw is None:
            await timesup(ma)
        else:   
            msg= 'Thank you, just to make sure please enter your memorable word once again'
            cpw = await getmsg(ma, msg)
            if cpw is None:
                await timesup(ma)
            else:   
                if pw == cpw:
                    await sendmsg(ma, 'All Good')
                    print(username +"/"+ pw + "/"+ cpw)
                else:
                    await sendmsg(ma, 'Password did not match')
                    print(pw)
                    print(cpw)

                
                
async def sendmsg(ma, msg):
    await client.send_message(ma, msg) 
    

async def getmsg(ma,msg):
    await client.send_message(ma, msg)
    answer = await client.wait_for_message(timeout=10.0, author=ma)
    return answer.content
    
async def timesup(ma):
    msg = 'You have took to long to responde. use !command to start again.'
    await sendmsg(ma, msg) 
    
#Younes RM Code Section End



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  
client.run('NTA1MTYyODI0MjEzODU2MjU2.DrRxzA.AejgQIuwCIx6WGIZBFv0H-fGHrA')