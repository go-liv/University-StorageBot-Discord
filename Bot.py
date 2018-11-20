import discord
import asyncio
from discord.ext import commands
import sqlite3


#<<<<<<< HEAD

#Younes RM Code Section
#=======
#>>>>>>> 59ca35a3f1513732bb68218f800acd04baf2e709


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

    #####################-------Guilherme's Code-------###########################
    #                                                                            #
    #                                                                            #    
    if message.content.startswith('!download'):                                  #
        await download(ma)                                                       #
    #                                                                            #        
    #                                                                            #    
    if message.content.startswith('!myfiles'):                                   #
        await myfiles(ma)                                                        #
    #                                                                            #
    #                                                                            #
    #####################----End of Guilherme's code----##########################

    



    
@client.event   
async def allusers(ma):
    
    data = ("SELECT * from users")
    c.execute(data)
    results = c.fetchall()
    for row in results:
        msg = ("name: " + row[1] + " / Discord ID: " + row[3])
        await sendmsg(ma, msg)
    

async def login(ma):
    if await checkdbusers('discord_id', ma) == False:
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
    if await checkdbusers('discord_id', ma) == False:
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
        if await checkdbusers('username', username) == True:
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
                    

                

async def checkdbusers(rn, rv):
    rn = str(rn)
    rv = str(rv)
    data = ("SELECT * from users WHERE " + rn + " = ?")
    c.execute(data, [(rv)])
    results = c.fetchall()
    if results:
        return True
    else:
        return False
    
async def checkdbfiles(rn, rv):
    rn = str(rn)
    rv = str(rv)
    data = ("SELECT * from files WHERE " + rn + " = ?")
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
    

async def getmsg(ma,msg, l = False):
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


##################################################--------Guilherme's Code--------###################################################################
#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)#
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
async def download(ma):                                                                                                                             #                                                                                                                                                   #
        if await logged(ma) == True:                                                                                                                 
###---------Getting user's id---------###############################################################################################################                                                                                                                      #                                                                                              #                                                                                                                                        #                              
            msg = 'Can you tell me the code of the file you want to download?'                                                                      #
            code = await getmsg(ma, msg) 
        
            if code == False:
                await timesup(ma)
                return
                                                                                                                                                    #            
            if await checkdbfiles('file_code', code) == True:                                                                                            #
                execution = "SELECT file_path FROM files WHERE file_code = ? AND discord_id = ?"
                filepath1 = c.execute(execution, [str(code), str(ma)])
                filepath2 = c.fetchone()[0]
                #filepath3 = str(filepath2).strip("'[(]),")                                                                                                       #                                                                                                                               #
         
                await client.send_file(ma, filepath2)                                                                                                    #
                msg = 'You can always download the file by right-clicking the file and using the discord option.'                                   #
                await sendmsg(ma, msg) 
                
                
                msg = 'Do you want to download another file? (y/n)'
                response = await getmsg(ma, msg)
                if response == False:
                    await timesup(ma)
                    return
                
                if response == 'Y' or response == 'y':
                    await download(ma)
                
                elif response.content == 'N' or response.content == 'n':
                    msg = 'I will see you next time!'
                    
                    await sendmsg(ma, msg)
                    return
                
                else:
                    msg = 'That is not a valid answer please try again with !download.'
                    
                    await sendmsg(ma, msg)
                    return
                    
                    
            else:                                                                                                                                   #
                msg = "The file you asked for doesn't seem to exist, recheck the file code and try again."                                          #
                await sendmsg(ma, msg)                                                                                                              #
                await download(ma)                                                                                                                  #
                                                                                                                                                    #
        else:                                                                                                                                       #
            msg = 'You are not logged in, please log in with !login before trying to download a file'                                               #
            await sendmsg(ma, msg)  
            return
#                                                                                                                                                   #
#                                                                                                                                                   #                                                                                                                                                              
#                                                                                                                                                   #                        
#                                                                                                                                                   #                                    
#                                                                                                                                                   #                                                
##########################--------This fucntion allows the user to read the files he has in his folder--------#######################################                                                                            
async def myfiles(ma):                                                                                                                              #
        if await logged(ma) == True:                                                                                                                      #
###---------Showing users their files---------####################################################################################################### 
            query = "SELECT file_name, file_code FROM files WHERE discord_id = ?"
            data = c.execute(query, [(str(ma))])                                                       #
            results = c.fetchall()                                                                                                                  #
                                                                                                                                                    #            
            for i in results:                                                                                                                       #
                msg = "File name: " + str(i[0]) + "   /   File code: " + str(i[1])                                                                            #
                                                                                                                                                    #             
                await sendmsg(ma, msg)                                                                                                              #
                                                                                                                                                    #            
                                                                                                                                                    #
        else:                                                                                                                                       #
            msg = 'You are not logged in, please log in with !login before trying to read your files'                                               #
            await sendmsg(ma, msg)                                                                                                                  #
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #        
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
###############################################--------End of Guilherme's Code--------###############################################################                                                                                                                                                  #



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  
client.run('NTA1MTYyODI0MjEzODU2MjU2.DrRxzA.AejgQIuwCIx6WGIZBFv0H-fGHrA')