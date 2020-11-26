import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("test-clubs-list")

club_sheet = sheet.worksheet("Sheet2")

#club_sheet.append_row("abhinav.palacharla@gmail.com", "Abhinav", "Palacharla")

#club_sheet.append_row(["email", "firstname", "lastname"])

#pprint(club_sheet.get_all_records())
pprint(club_sheet.get_all_values())