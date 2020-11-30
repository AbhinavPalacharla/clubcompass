#from sheet_functions import *
from mongo_club_functions import *

sheet = "clubs-testmaster-list"

clubs = import_clubs(sheet)

print(clubs)
