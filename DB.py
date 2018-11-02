import sqlite3

db = sqlite3.connect('Includes/BotDB.db')

c = db.cursor()

c.execute('''
  CREATE TABLE shops(id INTEGER PRIMARY KEY, name TEXT, address TEXT, link TEXT)

''')

db.commit()