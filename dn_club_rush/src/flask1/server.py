from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import url_for
from flask import redirect
from gspread.models import Spreadsheet
from pymongo import MongoClient
from mongo_club_functions import *
import sys

app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
	return redirect(url_for("delnorte"))

@app.route('/delnorte')
def delnorte():
	return render_template("home.html")

@app.route('/delnorte/my_clubs', methods=["POST", "GET"])
def my_clubs():
	if "firstname" not in session or "lastname" not in session or "email" not in session:
			return redirect(url_for("register"))

	if request.method == "GET":
		
		signups = get_signups(session["email"])
		clubs = []
		
		for i in signups:
			clubs.append(get_club(i))

		firstname = session["firstname"]
		lastname = session["lastname"]
		email = session["email"]

		return render_template("my_clubs.html", clubs=clubs, firstname=firstname, lastname=lastname, email=email)

	if request.method == "POST":
		return "you can't make a POST request to this page"

@app.route('/delnorte/register', methods=["POST", "GET"])
def register():
	if request.method == "GET":
		return render_template("user_info.html")
	
	if request.method == "POST":
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		email = request.form["email"]

		session["firstname"] = firstname
		session["lastname"] = lastname
		session["email"] = email

		if 'signed_up_for' not in session:
			session["signed_up_for"] = []

		return redirect(url_for("find_clubs"))

@app.route('/delnorte/find_clubs', methods=["POST", "GET"])
def find_clubs():
	if request.method == "POST":
		if "firstname" not in session or "lastname" not in session or "email" not in session:
			return redirect(url_for("register"))

		interest_list = get_all_interests()

		firstname = session["firstname"]
		lastname = session["lastname"]
		email = session["email"]

		if request.form.getlist("interests") != []:
			interests = request.form.getlist("interests")

			print(f"searching interests: {interests}", file=sys.stderr)

			clubs = search_clubs_by_interest(interests)

			signups = get_signups(session["email"])
			print(f"signups value: {signups}", file=sys.stderr)
			filtered_clubs = []

			if signups:
				for i in clubs:
					if i.get("name") not in signups:
						filtered_clubs.append(i)
			else: 
				filtered_clubs = clubs

			return render_template("show_clubs2.html", clubs=filtered_clubs, interest_list=interest_list, firstname=firstname, lastname=lastname, email=email)
	
		elif request.form.get("search") != None:
			search_query = request.form.get("search")

			print(f"running search query on: {search_query}", file=sys.stderr)

			search_clubs = search_bar(search_query)

			print(f"search_clubs value: {search_clubs}", file=sys.stderr)

			signups = get_signups(session["email"])
			
			filtered_clubs = []

			if signups:
				for i in search_clubs:
					if i.get("name") not in signups:
						filtered_clubs.append(i)
			else:
				filtered_clubs = search_clubs

			return render_template("show_clubs2.html", clubs=filtered_clubs, interest_list=interest_list, firstname=firstname, lastname=lastname, email=email)

		else:
			clubs = get_all_clubs()

			signups = get_signups(session["email"])
			print(f"signups value: {signups}", file=sys.stderr)
			filtered_clubs = []

			if signups:
				for i in clubs:
					if i.get("name") not in signups:
						filtered_clubs.append(i)
			else: 
				filtered_clubs = clubs
				
			return render_template("show_clubs.html", clubs=filtered_clubs, interest_list=interest_list, firstname=firstname, lastname=lastname, email=email)

	if request.method == "GET":
		if "firstname" not in session or "lastname" not in session or "email" not in session:
			return redirect(url_for("register"))

		clubs = get_all_clubs()

		signups = get_signups(session["email"])
		print(f"signups value: {signups}", file=sys.stderr)
		filtered_clubs = []

		if signups:
			for i in clubs:
				if i.get("name") not in signups:
					filtered_clubs.append(i)
		else: 
			filtered_clubs = clubs

		interest_list = get_all_interests()

		firstname = session["firstname"]
		lastname = session["lastname"]
		email = session["email"]

		return render_template("show_clubs.html", clubs=filtered_clubs, interest_list=interest_list, firstname=firstname, lastname=lastname, email=email)

@app.route('/delnorte/signup_user', methods=["POST"])
def signup_user():
	if request.method == "POST":
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		email = request.form["email"]
		club = request.form["club"]

		print("request received", file=sys.stderr)
		print(f"firsntame: {firstname} lastname: {lastname} email: {email} club: {club}", file=sys.stderr)
		
		sign_user(firstname, lastname, email, club)

		return f"firsntame: {firstname} lastname: {lastname} email: {email} club: {club}  --- added"
	
	if request.method == "GET":
		return "can't make get request to this page"

@app.route('/delnorte/remove_user', methods=["POST"])
def remove_user():
	if request.method == "POST":
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		email = request.form["email"]
		club = request.form["club"]
		
		delete_user(firstname, lastname, email, club)

		return f"firsntame: {firstname} lastname: {lastname} email: {email} club: {club}  --- removed"

	if request.method == "GET":
		return "can't make get request to this page"

@app.route('/delnorte/update_clubs')
def update_clubs():
	#spreadsheet = "clubs-testmaster-list"
	spreadsheet = "club_roster_2020"
	worksheet = "all_club_info"
	club_response = update_club_list(import_clubs(spreadsheet, worksheet))
	
	spreadsheet = "dn_club_interests_2020"
	worksheet = "all_interests"
	interest_response = update_club_interests(import_club_interests(spreadsheet, worksheet))

	if club_response and interest_response:
		return "successful"
	
	return "failed"

@app.route('/delnorte/contact')
def contact():
	return render_template("contacts.html")

if __name__ == "__main__":
	app.secret_key = "super_secret_key_123%^&"
	app.run(host="0.0.0.0", debug=True, port=5000)
