import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

roster = client.open("club_roster_2020")
all_club_info = roster.worksheet("all_club_info")

clubs = all_club_info.get_all_values()

#print(clubs)

club_signup = client.open("club_signup_2020")

for i in clubs:
    club_name = i[0]
    club_signup.add_worksheet(title=club_name, rows=100, cols=20)