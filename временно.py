import sqlite3

conn = sqlite3.connect('power_panda.sql')
cursor = conn.cursor()
cursor.execute("UPDATE users SET power = 1")
conn.commit()
conn.close()