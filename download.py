import sqlite3
from discord.ext import commands
import discord 
import asyncio
#
#
#
#Connecting to the data base and creating a cursor so we can select files
database = sqlite3.connect("The database used to store the files")
#
cursor = database.cursor()
#
#
#
#Assigning the bot's command prefix
client = commands.Bot(command_prefix = "!")
#
#
#
#
#
#
#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)
@client.command(pass_context=True)
async def download(ctx):
        await client.send_message(ctx.message.author, "Can you tell me the name of the file you want to download? ")
    
        file_name = await client.wait_for_message(author = ctx.message.author)
    
        cursor.execute(SELECT filepath FROM database WHERE filename = file_name AND userid = "The user id of the user")
    
        await client.send_file(ctx.message.author, file)
        await client.send_message(ctx.message.author, "You can always download the file by right-clicking the file and using the discord option.")
#
#
#
#
#


