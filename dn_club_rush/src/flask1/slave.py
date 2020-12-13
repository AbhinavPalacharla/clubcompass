from pymongo import MongoClient
#from datetime import time
import time

client = MongoClient("db", 27017)
db = client.signups


while True:
    email = "testing@gmail.com"
    club = "testing"

    db.signup_list.insert_one({"email": email, "clubs": [club]})

    time.sleep(120)

    db.signup_list.remove({"email": email})

    time.sleep(120)
