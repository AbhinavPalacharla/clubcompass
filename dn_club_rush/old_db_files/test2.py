import sqlite3

conn = sqlite3.connect("clubs.db")
c = conn.cursor()
c.execute("""SELECT * FROM club_info""")
clubs = c.fetchall()

conn.close()

for i in clubs:
	print(i)
