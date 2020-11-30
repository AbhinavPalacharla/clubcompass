import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def import_clubs(spreadsheet):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(spreadsheet)
    #club_sheet = sheet.worksheet("clubs")

    #clubs = club_sheet.get_all_values()

    #return clubs