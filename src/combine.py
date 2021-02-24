from CollageDataBase import *
import json

fn = "C:/Users/hawverm2967/Downloads/Pyhon/CollegeData/src/collegedataniche.json"

with open(fn) as fp:
    jdata = json.load(fp)


db = CollageDataBase()
db.load("C:/Users/hawverm2967/Downloads/Pyhon/CollegeData/src/CollageDB.json")

for collage in db.collages:
    print(collage.data["SAT"])