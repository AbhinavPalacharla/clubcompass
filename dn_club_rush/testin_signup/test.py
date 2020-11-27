from gspread.models import Worksheet
from pymongo import MongoClient
#from sheet_functions import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import sys


def signup_user(firstname, lastname, email, club):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
	client = gspread.authorize(creds)

	club_signup = client.open("club_signup_2020")

	club_sheet = club_signup.worksheet(club)

	entry = [firstname, lastname, email]
	print("made it here", file=sys.stderr)
	
	error = club_sheet.append_row(entry)

	print(f"error: {error}", file=sys.stderr)

	print(f"signed up user with name: {firstname} and club: {club}", file=sys.stderr)

signup_user("abhinav", "palacharla", "abhinav.palacharla@gmail.com", "American Red Cross")