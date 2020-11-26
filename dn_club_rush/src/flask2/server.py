from flask import request
from flask import Flask
from flask import render_template
from club_functions import *
from pymongo import MongoClient

app = Flask(__name__, static_folder='./static')
client = MongoClient("db", 27017)
db = client.clubs

@app.route('/')
def home():
	#return render_template("home.html")
	return "flask2"
	
@app.route('/search_clubs', methods=["POST", "GET"])
def search_clubs():
	if request.method == "POST":

		interests = request.form.getlist("myCheckbox")
		#print(interests)

		clubs = search_by_interest(db, interests) #clubs is an list
		print(clubs)
		return render_template("show_clubs.html", clubs=clubs) #show recommended clubs once they have entered the info

	if request.method == "GET":
		return render_template("get_interests.html") #render page to get info from user

@app.route('/club_catalog')
def club_catalog():
	clubs = get_all_clubs(db) #returns list of all clubs, clubs in list are represented as a club object
	return render_template("club_catalog.html", clubs=clubs)
	#return render_template("new_club_catalog.html", clubs=clubs)

@app.route('/featured_news')
def featured_news():
	return render_template("featured_news.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5000)
