import sqlite3

def search_by_interest(interests):

	tempclubs = []

	conn = sqlite3.connect("clubs.db")
	c = conn.cursor()

	for i in interests:

		c.execute("""SELECT * FROM club_info WHERE interest1=? OR interest2=? OR interest3=?""", (i, i, i))
		matching_clubs = c.fetchall()
		tempclubs.append(matching_clubs)

	conn.close()

	finalclubs = []
	for i in tempclubs:
		if i not in finalclubs:
			finalclubs.append(i)

	return finalclubs

def get_all_clubs():
	conn = sqlite3.connect("clubs.db")
	c = conn.cursor()

	c.execute("""SELECT * FROM club_info""")
	clubs = c.fetchall()

	conn.close()

	return clubs

def add_to_interest_list():
	pass
