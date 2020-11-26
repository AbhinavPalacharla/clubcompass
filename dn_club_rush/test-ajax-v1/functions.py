def add_to_interest(firstname, lastname, email, work_sheet):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
	client = gspread.authorize(creds)

	sheet = client.open('https://docs.google.com/spreadsheets/d/1LCS5kL1Zw9Bq5jP_Ym9ov9WbRnnyxWTiD_60kcofM14/edit#gid=0')
	club_sheet = sheet.worksheet(work_sheet)

	row = [firstname, lastname, email]

	club_sheet.append_one(row)