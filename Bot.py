import discord
import asyncio
from discord.ext import commands
import sqlite3
import db as database


#Younes RM Code Section
with sqlite3.connect("BotDB.db") as db: 
    c = db.cursor()
client = discord.Client()



@client.event
async def on_message(message):
    ma = message.author
  
    if message.author == client.user:
        return
      

    if message.content.startswith('!register'):
        
        await rf(ma)
        
    if message.content.startswith('!all'):
        await sendmsg(ma, ma)
        await allusers(ma) 
        
    if message.content.startswith('!delete'):
        await client.delete_message(message)
     



    



    
@client.event   
async def allusers(ma):
    
    data = ("SELECT * from users")
    c.execute(data)
    results = c.fetchall()
    for row in results:
        msg = ("name: " + row[1] + " / Discord ID: " + row[3])
        await sendmsg(ma, msg)
    

async def rf(ma):
    msg = 'Hello, to register please Chose a Username.'
    username = await getmsg(ma, msg, False)
    if username is None:
        await timesup(ma)
    else:
        msg = 'Thank you. Now please enter a memorable word'
        pw = await getmsg(ma, msg, True)
        if pw is None:
            await timesup(ma)
        else:   
            msg= 'Thank you, just to make sure please enter your memorable word once again'
            cpw = await getmsg(ma, msg, True)
            if cpw is None:
                await timesup(ma)
            else:   
                if pw == cpw:
                    await register(username,pw,ma)
                    await sendmsg(ma, 'All Good')
                else:
                    await sendmsg(ma, 'Password did not match')
                    

                

                
async def register(username,pw,ma):
    ma = str(ma)
    data = ("INSERT INTO users(username, passwrod, discord_id, login) VALUES(?, ?, ?, 0)")
    c.execute(data, [(username),(pw),(ma)])  
    db.commit()

                
                
async def sendmsg(ma, msg):
    await client.send_message(ma, msg) 
    

async def getmsg(ma,msg,d):
    await client.send_message(ma, msg)
    answer = await client.wait_for_message(timeout=10.0, author=ma)
    a = answer.content
    
    return a
    
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