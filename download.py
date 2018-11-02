import sqlite3
import requests
from discord.ext import commands
import discord 
import asyncio



"""
    define download(userid, file path, file):
        knowing the userid and the file name go to table and get file path
        with file path send message to the user with the file
        let user know that discord has a function that allows the user to download the file to the pc.

"""

#connecting to the data base and creating a cursor so we can select files
database = sqlite3.connect("The database used to store the files")

cursor = database.cursor()



@client.command
async def download_file(userid, filepath, filename):
    cursor.execute(SELECT filepath FROM database WHERE filename = "The name of the file the user is looking for" AND userid = "The user id of the user")
    
    file = requests.get(filepath)
    
    await client.send_file(message.author, file)



