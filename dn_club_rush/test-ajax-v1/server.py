from sys import stderr
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
from functions import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("newIndex.html")

@app.route('/save_user_to_cookies', methods=["POST"])
def save_user_to_cookies():

    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
    #need to handle exceptions like when one of these isnt given in the post request
        session["firstname"] = firstname
        session["lastname"] = lastname
        session["email"] = email

        return f"saved user -- firstname_cookies: {session['firstname']} lastname: {session['lastname']} email: {session['email']}"

    else:
        return "whoops, looked like something went wrong, go back to the main page"

@app.route('/debug_cookies')
def debug_cookies():
    return f"firstname_cookies: {session['firstname']} lastname: {session['lastname']} email: {session['email']}"

@app.route('/add_to_interest', methods=["POST"])
def add_to_interest():
    if request.method == "POST":
        firstname = session["firstname"]
        lastname = session["lastname"]
        email = session["email"]
        sheet = request.form["sheet"]

        add_to_interest(firstname, lastname, email, sheet)

        return f"added this info -- firstname: {firstname} lastname {lastname} email: {email} sheet: {sheet}"



# @app.route('/add_to_interest', methods=["GET", "POST"])
# def add_to_interest():
#     if request.method == "POST":
#         firstname = request.form["firstname"]
#         lastname = request.form["lastname"]
#         email = request.form["email"]
#         sheet = request.form["sheet"]

#         print(f"firstname: {firstname}", file=stderr)
#         print(f"lastname: {lastname}", file=stderr)
#         print(f"email: {email}", file=stderr)
#         print(f"sheet: {sheet}", file=stderr)
        
#         # row = [firstname, lastname, email]

#         # scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#         # spreadsheet = "https://docs.google.com/spreadsheets/d/1LCS5kL1Zw9Bq5jP_Ym9ov9WbRnnyxWTiD_60kcofM14/edit#gid=0"
#         # creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
#         # client = gspread.authorize(creds)

#         # sheet = client.open(spreadsheet)
#         # club_sheet = sheet.worksheet(sheet)

#         # club_sheet.insert_row(row)
#         return f"firstname: {firstname} lastname: {lastname} email: {email} sheet: {sheet}"

if __name__ == "__main__":
	app.secret_key = "super_secret_key_123%^&"
	app.run(host="0.0.0.0", debug=True, port=5000)