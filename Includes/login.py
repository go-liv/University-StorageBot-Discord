import sqlite3

with sqlite3.connect("Includes/BotDB.db") as db:
  c = db.cursor()


def login(discord_id):
  
  if logged(discord_id) == True:
    print("you are not logged in")
  elif logged(discord_id) == False:
    print("You are already Logged in / use !logout command to logout")

   
    
    

    

    
    
def logged(discord_id):
  islogged = ("SELECT * from users WHERE discord_id = ?")
  c.execute(islogged, [(discord_id)])
  results = c.fetchall()
  if results:
    return False
  else:
    return True
    