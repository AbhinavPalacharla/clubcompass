from sys import stderr
from flask import Flask
from flask import render_template
from flask import request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys

app = Flask(__name__)

@app.route('/add_to_interest', methods=["GET", "POST"])
def add_to_interest():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        sheet = request.form["sheet"]

        print(f"firstname: {firstname}", file=stderr)
        print(f"lastname: {lastname}", file=stderr)
        print(f"email: {email}", file=stderr)
        print(f"sheet: {sheet}", file=stderr)
        
        # row = [firstname, lastname, email]

        # scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        # spreadsheet = "https://docs.google.com/spreadsheets/d/1LCS5kL1Zw9Bq5jP_Ym9ov9WbRnnyxWTiD_60kcofM14/edit#gid=0"
        # creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        # client = gspread.authorize(creds)

        # sheet = client.open(spreadsheet)
        # club_sheet = sheet.worksheet(sheet)

        # club_sheet.insert_row(row)
        return f"firstname: {firstname} lastname: {lastname} email: {email} sheet: {sheet}"

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5000)