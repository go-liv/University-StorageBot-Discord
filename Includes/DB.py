import sqlite3

db = sqlite3.connect('Includes/BotDB.db')

c = db.cursor()

c.execute('''
  CREATE TABLE shops(id INTEGER PRIMARY KEY, username TEXT, passwrod TEXT, discord_id TEXT, login INTEGER)

''')

db.commit()