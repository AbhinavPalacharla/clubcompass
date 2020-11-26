import sqlite3

conn = sqlite3.connect("clubs.db")
c = conn.cursor()

c.execute("""CREATE TABLE club_info (
		name blob,
		staff blob,
		president blob,
		email blob,
		meeting_times blob,
		location blob,
		description blob,
		interest1 blob,
		interest2 blob,
		interest3 blob
		)""")

conn.commit()
conn.close()
