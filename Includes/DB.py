import sqlite3

db = sqlite3.connect('Includes/BotDB.db')

c = db.cursor()

#c.execute('''
#  CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, passwrod TEXT, discord_id TEXT, login INTEGER)
#
#''')


c.execute('''
      INSERT INTO users(username, passwrod, discord_id, login) VALUES("younesrm", "passwrod", "younesrm#6384", 1)
''')
db.commit()