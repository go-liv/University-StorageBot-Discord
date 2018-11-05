import discord
import asyncio
from discord.ext import commands
import sqlite3


<<<<<<< HEAD

#Younes RM Code Section
=======
>>>>>>> 59ca35a3f1513732bb68218f800acd04baf2e709


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
    
    if message.content.startswith('!login'):
        await login(ma)
        
    if message.content.startswith('!logout'):
        await logout(ma)
        
    if message.content.startswith('!all'):
        await sendmsg(ma, ma)
        await allusers(ma) 
        
    if message.content.startswith('!delete'):
        await client.delete_message(message)
        
    if message.content.startswith('!dm'):
        await delete(ma)



    



    
@client.event   
async def allusers(ma):
    
    data = ("SELECT * from users")
    c.execute(data)
    results = c.fetchall()
    for row in results:
        msg = ("name: " + row[1] + " / Discord ID: " + row[3])
        await sendmsg(ma, msg)
    

async def login(ma):
    if await checkdb('discord_id', ma) == False:
        msg = 'You do not have an account with us yet'
        await sendmsg(ma, msg)
        return
    elif await logged(ma) == True:
        msg = 'You are Already logged in. use !logout to Logout from your account'
        await sendmsg(ma, msg)
    else:
        data = ("UPDATE users SET login = 1 WHERE discord_id = ?")
        c.execute(data, [(str(ma))])
        db.commit()
        await sendmsg(ma, 'You have been login')
        
async def logout(ma):
    if await checkdb('discord_id', ma) == False:
        msg = 'You do not have an account with us yet'
        await sendmsg(ma, msg)
        return
    elif await logged(ma) == False:
        msg = 'You are not logged in'
        await sendmsg(ma, msg)
        return
    else:
        data = ("UPDATE users SET login = 0 WHERE discord_id = ?")
        c.execute(data, [(str(ma))])
        db.commit()
        await sendmsg(ma, 'You have been Logout')
        
async def logged(ma):
    ma = str(ma)
    islogged = ("SELECT * from users WHERE discord_id = ? AND login = 1")
    c.execute(islogged, [(ma)])
    results = c.fetchall()
    if results:
        return True
    else:
        return False


async def rf(ma):
    msg = 'Hello, to register please Chose a Username.'
    username = await getmsg(ma, msg, False)
    if username is False:
        await timesup(ma)
    else:
        if await checkdb('username', username) == True:
            msg = 'This username already exists! call the bot again'
            await sendmsg(ma, msg)
            return
        msg = 'Thank you. Now please enter a memorable word'
        pw = await getmsg(ma, msg, True)
        if pw is False:
            await timesup(ma)
        else:   
            msg= 'Thank you, just to make sure please enter your memorable word once again'
            cpw = await getmsg(ma, msg, True)
            if cpw is False:
                await timesup(ma)
            else:   
                if pw == cpw:
                    await register(username,pw,ma)
                    await sendmsg(ma, 'All Good')
                else:
                    await sendmsg(ma, 'Password did not match')
                    

                

async def checkdb(rn, rv):
    rn = str(rn)
    rv = str(rv)
    data = ("SELECT * from users WHERE " + rn + " = ?")
    c.execute(data, [(rv)])
    results = c.fetchall()
    if results:
        return True
    else:
        return False


async def register(username,pw,ma):
    ma = str(ma)
    data = ("INSERT INTO users(username, passwrod, discord_id, login) VALUES(?, ?, ?, 0)")
    c.execute(data, [(username),(pw),(ma)])  
    db.commit()

async def delete(ma):
    ma = str(ma)
    data = ("DELETE FROM users WHERE discord_id = ?")
    c.execute(data, [(ma)])  
    db.commit()
                
                
async def sendmsg(ma, msg):
    await client.send_message(ma, msg) 
    

async def getmsg(ma,msg,d):
    await client.send_message(ma, msg)
    answer = await client.wait_for_message(timeout=10.0, author=ma)
    if answer is None:
        return False
    else:
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