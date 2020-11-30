#import sqlite3
from pymongo import MongoClient

def search_by_interest(db, interests):

	tempclubs = []

	#conn = sqlite3.connect("clubs.db")
	#c = conn.cursor()

	for i in interests:
		matching_clubs = db.clubs.find({"interest1": i, "interest2": i, "interest3": i})
		tempclubs.append(matching_clubs)
		#c.execute("""SELECT * FROM club_info WHERE interest1=? OR interest2=? OR interest3=?""", (i, i, i))
		#matching_clubs = c.fetchall()
		#tempclubs.append(matching_clubs)

	#conn.close()

	finalclubs = []
	for i in tempclubs:
		if i not in finalclubs:
			finalclubs.append(i) #filter out duplicate clubs

	return finalclubs

def get_all_clubs(db):
	#conn = sqlite3.connect("clubs.db")
	#c = conn.cursor()

	#c.execute("""SELECT * FROM club_info""")
	#clubs = c.fetchall()
	clubs = db.clubs.find()
	#conn.close()

	return clubs

def add_to_interest_list():
	pass
