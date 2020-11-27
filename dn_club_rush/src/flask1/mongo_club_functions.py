#import sqlite3
from typing import final
from gspread.models import Worksheet
from pymongo import MongoClient
#from sheet_functions import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import sys


def sign_user(firstname, lastname, email, club):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
	client = gspread.authorize(creds)
	
	club_signup = client.open("club_signup_2020")
	
	club_sheet = club_signup.worksheet(club)

	try: 
		club_sheet.find(email)
		return "Err: already signed up"
	
	except:
		#raises exception if cell not found (user is not signed up for club yet)
		entry = [firstname, lastname, email]
		club_sheet.append_row(entry)

		mongoclient = MongoClient("db", 27017)
		db = mongoclient.signups

		x = list(db.signup_list.find())
		print(f"x is: {x}", file=sys.stderr)

		if list(db.signup_list.find({"email": email})) != []:
			print("inside if #1", file=sys.stderr)
			entry = list(db.signup_list.find({"email": email}))
			print(f"entry: {entry}", file=sys.stderr)
			print("flag1", file=sys.stderr)
			updated_clubs = entry[0].get("clubs")
			print("flag2", file=sys.stderr)
			updated_clubs.append(club)
			print("flag3", file=sys.stderr)
			
			query = {"email": email}
			change_val = {"$set": {"clubs": updated_clubs}}
			
			db.signup_list.update_one(query, change_val)
			print("flag4", file=sys.stderr)

		elif list(db.signup_list.find({"email": email})) == []:
			print("in else#1", file=sys.stderr)
			entry = db.signup_list.insert_one({"email": email, "clubs": [club]})
			print("else1 good", file=sys.stderr)
		return "signed up"

def delete_user(firstname, lastname, email, club):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
	client = gspread.authorize(creds)
	
	club_signup = client.open("club_signup_2020")
	club_sheet = club_signup.worksheet(club)
	cell = club_sheet.find(email)

	club_sheet.delete_row(cell.row)

	mongoclient = MongoClient("db", 27017)
	db = mongoclient.signups

	entry = list(db.signup_list.find({"email": email}))
	updated_clubs = entry[0].get("clubs")
	updated_clubs.remove(club)

	query = {"email": email}
	change_val = {"$set": {"clubs": updated_clubs}}

	db.signup_list.update_one(query, change_val)

def get_signups(email):
	client = MongoClient("db", 27017)
	db = client.signups

	# if signup_list not in db.list_collection_names():
	# 		db.signup_list
	
	if list(db.signup_list.find({"email": email})) != []:
		entry = list(db.signup_list.find({"email": email}))
		clubs = entry[0].get("clubs")
		print(f"clubs from get_signups: {clubs}", file=sys.stderr)
		
		return clubs

	else:
		return []

def import_clubs(spreadsheet, worksheet):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
	client = gspread.authorize(creds)

	sheet = client.open(spreadsheet)
	club_sheet = sheet.worksheet(worksheet)

	clubs = club_sheet.get_all_values()

	return clubs

def import_club_interests(spreadsheet, worksheet):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
	client = gspread.authorize(creds)

	sheet = client.open(spreadsheet)
	interest_sheet = sheet.worksheet(worksheet)

	interests = interest_sheet.get_all_values()

	return interests

def update_club_interests(interests):
	client = MongoClient("db", 27017)
	db = client.interests

	db.interest_list.drop()

	for i in interests:
		interest = {
			"name": i[0]
		}

		db.interest_list.insert_one(interest)

	return True

def update_club_list(clubs):
	
	client = MongoClient("db", 27017)
	db = client.clubs
	
	db.club_info.drop() #delete old table of club info

	#insert new clubs
	for i in clubs:
		club = {
			"name": i[0],
			"president": i[1],
			"staff": i[2],
			"email": i[3],
			"meeting_times": i[4],
			#"location": i[5],
			"description": i[5],
			"interest1": i[6],
			"interest2": i[7],
			"interest3": i[8]
		}

		db.club_info.insert_one(club)

	return True

def get_all_clubs():
	client = MongoClient("db", 27017)
	db = client.clubs

	clubs = db.club_info.find()

	return clubs

def get_club(name):
	client = MongoClient("db", 27017)
	db = client.clubs

	club = db.club_info.find({"name": name})

	return club[0]

def get_all_interests():
	client = MongoClient("db", 27017)
	db = client.interests

	interests = db.interest_list.find()

	return interests

def search_clubs_by_interest(interests):
	
	client = MongoClient("db", 27017)
	db = client.clubs

	if not interests:
		return get_all_clubs()

	print(interests, file=sys.stderr)

	initial_club_list = []

	for i in interests:

		matches = db.club_info.find({"interest1": i})
		for j in matches:
			initial_club_list.append(j)

		matches = db.club_info.find({"interest2": i})
		for j in matches:
			initial_club_list.append(j)

		matches = db.club_info.find({"interest3": i})
		for j in matches:
			initial_club_list.append(j)

	final_club_list = []
		
	exists = False

	for i in initial_club_list:
		for j in final_club_list:
			if i.get("_id") == j.get("_id"):
				exists = True
		if exists != True:
			final_club_list.append(i)
		exists = False
	
	#print(f"final clubs list: {final_club_list}", file=sys.stderr)
	
	return final_club_list

def search_bar(query_string):

	print(f"query string: {query_string}", file=sys.stderr)

	tokenized_string = query_string.split()

	print(f"tokenized string: {tokenized_string}", file=sys.stderr)

	client = MongoClient("db", 27017)
	db = client.clubs

	initial_club_list = []

	for i in tokenized_string:

		query = f".*{i}.*"
		print(f"query in search for loop: {query}", file=sys.stderr)
	
		initial_club_list.extend(list(db.club_info.find({"name": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"president": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"staff": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"email": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"meeting_times": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"description": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"interest1": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"interest2": {"$regex": query, "$options": "-i"}})))
		initial_club_list.extend(list(db.club_info.find({"interest3": {"$regex": query, "$options": "-i"}})))

	print(f"initial club list: {initial_club_list}", file=sys.stderr)

	final_club_list = []
		
	exists = False

	for i in initial_club_list:
		for j in final_club_list:
			if i.get("_id") == j.get("_id"):
				exists = True
		if exists != True:
			final_club_list.append(i)
		exists = False

	print(f"final club list: {final_club_list}", file=sys.stderr)

	return final_club_list
