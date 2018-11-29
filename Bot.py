#the following lines includes library from out sourses
import string
import discord
import asyncio
from discord.ext import commands
import sqlite3
import os
import glob
import imageio
import random




#Younes RM Code Section

'''
####################################################Younes RM Code Section##################################################
this is a database check class which will check database for needed value and return true or false based on conditions given
'''
class databaseCheck:
     def __init__(self, ma):
    self.ma = str(ma)
  '''this function inside the class will check a value in a given colum and return true if the value exits. for example if i want 
    to check if a discord id exits in my database then i will call the function as checkdb('discord_id', Value) and the return value
    will be given in true or false. this function only checks Users table. if you need to check items in different table please let
    me know and i will update the function with extra arguement to recieve table name as well.
  ''' 
  def checkdb(self, rn, rv):
    rn = str(rn)
    rv = str(rv)
    data = ("SELECT * from users WHERE " + rn + " = ?")
    c.execute(data, [(rv)])
    results = c.fetchall()
    if results:
        return True
    else:
        return False
  '''this function will check the password for current users based on the value they have given you. so when you call this 
  function you must give one arguement as string and the function will return true if the given value matches the current users
  passwrod. IMPORTANT: this encryption function has been created by YounesRM please do not edit/remove this code'''
  def checkpw(self, pw):
    pw = pw
    z = 0
    w = 0
    data = ("SELECT * from users WHERE discord_id = ?")
    c.execute(data, [(self.ma)])
    results = c.fetchone()
    spw = results[2]
    dcode = results[5]
    for i in dcode:
      i = int(i)
      w = w + i
      if spw[w] != pw[z]:
        return False
      w += 1
      z += 1
    
    return True
      
  '''this function can be called without passing any arguemnt. it only returns true if the current user is logged in. the current
  user discord id will be taken from the class arguemnt which will have the user discord id as default. '''
  def logged(self):
    islogged = ("SELECT * from users WHERE discord_id = ? AND login = 1")
    c.execute(islogged, [(self.ma)])
    results = c.fetchall()
    if results:
        return True
    else:
        return False
    


'''
this section of the code is the connection to our database with a cursor already created for you. the name of the cursor is c 
therefore you can use c.*** to excute any data from the database'''
with sqlite3.connect("BotDB.db") as db:
    c = db.cursor()
'''the following line is the connection to discord client server which will be needed to communicate with discord server
you do not need to use this variable or edit it. therefore please leave as it is'''
client = discord.Client()
'''this dictornory has been created for as file selector for different users, currently im coding the file selector class
therefore i will update once the file selector class is done'''
fileSelector = {}


'''the following function is what we use to communicate with users on discord. this functions has been based on asyncio library
we check every single message by users to find our command to activate another function so thats how the bot works.
'''
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

    




    if message.content.startswith('!slideshow'):
      await slideshow(ma)
    if message.content.startswith('!ch'):
      databaseCheck(ma).checkdb('discord_id', str(ma))
      

    
'''
the function which is called allusers(ma) is only for testing and has been created for development reasons. you not need to 
use/edit/delete this function however if you need to use it. this function will return all the users registered with our bot 
to use please run the bot and use !all command on discord and the message will be send to you with all users
'''
@client.event
async def allusers(ma):
  
  msg = ''
  data = ("SELECT * from users")
  c.execute(data)
  results = c.fetchall()
  for row in results:
    msg = msg +  ("\n name: " + row[1] + " / Discord ID: " + row[3])
  await sendmsg(ma,msg)
        
'''this function will log the user in. to use simply call the function and pass the messsage auther which has been saved in a variable
called ma. it will ask the user for their password and then once all security has been done it will log the user in
you do not need to use this function, to check if the user is logged there is a function in databaseCheck class called logged()'''
async def login(ma):

    if await checkdbusers('discord_id', ma) == False:
        msg = 'You do not have an account with us yet'
        await sendmsg(ma, msg)
        return
    elif await logged(ma) == True:
        msg = 'You are Already logged in. use !logout to Logout from your account'
        await sendmsg(ma, msg)

    if databaseCheck(ma).checkdb('discord_id', ma) == False:
      msg = 'You do not have an account with us yet'
      await sendmsg(ma, msg)
      return
    elif databaseCheck(ma).logged() == True:
      msg = 'You are Already logged in. use !logout to Logout from your account'
      await sendmsg(ma, msg)

    else:
      msg = "please Enter Your Memorable word"
      pw = await getmsg(ma,msg, True)
      if pw == False:
        await timesup(ma)
      if databaseCheck(ma).checkpw(pw) == False:
        msg = "Your Memorable Word is Incorrect"
        await sendmsg(ma,msg)
      elif databaseCheck(ma).checkpw(pw) == True:
        data = ("UPDATE users SET login = 1 WHERE discord_id = ?")
        c.execute(data, [(str(ma))])
        db.commit()
        await sendmsg(ma, 'You have been login')
'''
this function is connected to !logout command and it will simply logout the current users. again there is no need to 
edit/remove/use this function'''
async def logout(ma):

    if databaseCheck(ma).checkdb('discord_id', ma) == False:
        msg = 'You do not have an account with us yet'
        await sendmsg(ma, msg)
        return
    elif databaseCheck(ma).logged() == False:
        msg = 'You are not logged in'
        await sendmsg(ma, msg)
        return
    else:
        data = ("UPDATE users SET login = 0 WHERE discord_id = ?")
        c.execute(data, [(str(ma))])
        db.commit()
        await sendmsg(ma, 'You have been Logout')


'''
this function will handle the register part of the bot. you do not need to edit/remove or use this function 
this funciton can be actiavted in discord using !register command and it will handle the register form '''
async def rf(ma):
    if databaseCheck(ma).checkdb('discord_id', ma) == True:
      msg = 'You already have an account with us'
      await sendmsg(ma, msg)
      return
    msg = 'Hello, to register please Chose a Username.'
    username = await getmsg(ma, msg, False)
    if username is False:
        await timesup(ma)
    else:
        if databaseCheck(ma).checkdb('username', username) == True:

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
    #else:
       # return False

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
'''this function will create a slideshow for the user based on the images they have chose. currently the follwing function does 
not work as i am waiting on my team mates to give me the needed code for file checking and file path database table
once updated i will let you guys know. however this function has been tested by passing the arguements manually'''                    
async def slideshow(ma):
  itemList = await getlist(ma)
  await sendmsg(ma,itemList)
  list = []
  images = await getMultyMessage(ma,list)
  if images == False:
    msg = 'invalid input, please call the bot again'
    await sendmsg(ma,msg)
    return
  #img_dir = "users/" + str(ma)
  #img_list = glob.glob(f"{img_dir}/*.jpg")
  for i in list:
    i = getItem(ma, i)
    images.append(imageio.imread(i))
  name = await nameGenerator(ma, ".gif")
  file = img_dir + '/' + name
  imageio.mimsave(file, images, duration=3)
  await client.send_file(ma, file)
'''
this function has been created to recieve multy messsage from the user and return it to you in a list. to use it simple call the function 
passing the message auther and an empy list and it will take care for you up to how many item the user wants to give you '''
async def getMultyMessage(ma,list):
  msg = "please select your first item using item code"
  item = await getmsg(ma, msg)
  if item == false:
    await timesup(ma)
  try:
    item = int(item)
    if await checkitem(ma,'item', item) == True:
      list.append(item)
      await getMultyMessage(ma, list)
    else:
      msg= 'item does not exitst please check the item code. to exit ingnore this msg'
      await sendmsg(ma,msg)
      await getMultyMessage(ma,list)

  except:
    if item.lower() == 'done':
      return list
    else:
      return False
'''this function has been created to generate an random name for you. you call the function passing the message auther and also 
the extention of your file and the function will create a random name and checks the user folder to make sure that file with 
the same name does not exits and then it will return the name to you as an string'''
async def nameGenerator(ma, fex):
  N = random.randint(1,10)
  name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
  name = str(name) + str(fex)
  d = 'users/' + str(ma) + name
  if os.path.exists(d):
    nameGenerator(ma, fex)
  else:
    return str(name)



'''this function is called once the rf function is done recieving all the needed information. then this fucntion will try 
to insert the new user to our databse and also create a folder for their files'''
async def register(username,pw,ma):
    ma = str(ma)
    pw, dcode = await hashpw(pw)
    data = ("INSERT INTO users(username, passwrod, discord_id, login, dcode) VALUES(?, ?, ?, 0, ?)")
    c.execute(data, [(username),(pw),(ma),(dcode)])
    db.commit()
    directory = "users/" + ma
    if not os.path.exists(directory):
      os.makedirs(directory)
'''this function again is used by rf function to encrypt the user password for more securiry.
IMPORTANT: please do not edit/remove or use this function'''
async def hashpw(pw):
  spw = ''
  d = ''
  for i in pw:
    N = random.randint(1,9)
    s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    d = d + str(N)
    spw = spw + s + i
  return spw, d
    
    
  
'''this function hsa been made for testing and development reason and it simple does remove your current account from the
database so you can create new account and test needed functions. to use simply use !dm command in discord'''
async def delete(ma):
    ma = str(ma)
    data = ("DELETE FROM users WHERE discord_id = ?")
    c.execute(data, [(ma)])
    db.commit()

'''function has been made to make communcation easier with the user. simply call the function passing the reciever and your message
as string and it will take care of sending your file.'''
async def sendmsg(ma, msg):
    await client.send_message(ma, msg) 
    

'''
this function again has been made to make the job easier. call the function passing the reciever and the message as string to 
tell them what you want from them. and this function will take care of reciving their message and pass it to you as string 
if the user does not reply then it will return false'''
async def getmsg(ma,msg,d):
    await client.send_message(ma, msg)
    answer = await client.wait_for_message(timeout=10.0, author=ma)
    if answer is None:
        return False
    else:

        a = answer.content
        return a
'''times up has been created to let the user know they have took too long to reply and the current command has been disabled 
and they need to call the bot again. simple call timesups passing reciever and it will let them know.'''
async def timesup(ma):
    msg = 'You have took to long to responde. use !command to start again.'
    await sendmsg(ma, msg)

    

'''
######################################Younes RM Code Section End#######################################
'''

'''
#####################################Guilherme's Code Section###########################################
'''
''' 
Download Function 
This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function). 
You can call the function by simply passing the author of the message, in this case it is the variable ma(message.author = Discord ID).                                  
The functionality of the function is to ask the user for a code, which is assigned to his file. 
when uploaded, and then search for this code(file_code column in the database). When the code is found, the function grabs the file path 
in the same row as the code and sends the file from that file path to the user as a message. 
'''  
	  
	                   
async def download(ma):    
	if databaseCheck(ma).logged() == True:                                                                                                        
	  
#Getting user's id  
		msg = 'Can you tell me the code of the file you want to download?'                                                                        
		code = await getmsg(ma, msg, False)  
	              
		if code == False:  
			await timesup(ma)                             
			return  
	  
#Checking database            
		if await checkdbfiles('file_code', code) == True:  
			execution = "SELECT file_path FROM files WHERE file_code = ? AND user = ?"  
	  
			filepath1 = c.execute(execution, [str(code), str(ma)])  
			filepath2 = c.fetchone()[0]  
	  
			await client.send_file(ma, filepath2)  
	  
			msg = 'You can always download the file by right-clicking the file and using the discord option.'  
			await sendmsg(ma, msg)  
	  
#Re-download  
			msg = 'Do you want to download another file? (y/n)'  
			response = await getmsg(ma, msg, False)  
	  
			if response == False:  
				await timesup(ma)  
				return  
	  
	  
			if response == 'Y' or response == 'y':  
				await download(ma)  
	  
	  
			elif response == 'N' or response == 'n':  
				msg = 'I will see you next time!'  
	  
				await sendmsg(ma, msg)  
				return  
	  
	  
			else:  
				msg = 'That is not a valid answer please try again with !download.'  
	  
				await sendmsg(ma, msg)  
				return  
	  
	  
		else:  
			msg = "The file you asked for doesn't seem to exist, recheck the file code and try again."  
	  
			await sendmsg(ma, msg)  
			return  
	  
	  
        else:  
		msg = 'You are not logged in, please log in with !login before trying to download a file'  
	  
                await sendmsg(ma, msg)  
                return  
	  
	  
	  
'''                                                                                       
My Files Function                                                                             
This function was made in order to show the users the files they have stored in our storage bot.
It can be called like the download function just by passing the user's ma (Discord ID).
In quick terms, the function searches the database for the column file_name and file_code and 
shows the user the file_name and the respective assigned code, all this is made by searching the 
database for the row where the user's ma (Discord ID) is.  
'''  
	  
	  
async def myfiles(ma):  
	  
        if databaseCheck(ma).logged() == True:  
	  
#Showing users their files  
                query = "SELECT file_name, file_code FROM files WHERE user = ?"  
	  
                data = c.execute(query, [(str(ma))])  
	  
                results = c.fetchall()  
	                                                                                                                            
                for i in results:  
                        msg = "File name: " + str(i[0]) + "   /   File code: " + str(i[1])  
	               
	                await sendmsg(ma, msg)
			
		return
	  
	 
        else:  
                msg = 'You are not logged in, please log in with !login before trying to read your files'  
	  
                await sendmsg(ma, msg)
		return

'''
#####################################Guilherme's Code Section End######################################
'''


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('token of the bot is inserted here')
