import json

class Collage:
    
    class Campus:
        def __init__(self, name= "main"):
            self.name = name
            self.data = Collage.meta_data.copy()
    
    meta_data = {  
        "SAT" : {"math" : [25, 50, 75],
                 "reading" : [25, 50, 75]
                },
        
        "ACT" : 0,
        "GPA" : 0,
        "ACPT Rate" : 0,
        
        "default" : True
    }
    
    def __init__(self, name):
        self.name = name
        self.camps = [Campus()]
        


class CollageDataBase:
    def __init__(self):
        self.collages = []
    
    def add(self, collage):
        self.collages.append(collge)
    
    def search(self, name, camp_name = "main"):
        for collage in self.collages:
            if collage.name.lower() == name.lower():
                for camp in collage.camps:
                    if camp.name.lower() == camp_name.lower():
                        return camp
    
    def load(self, file_name):
        with open(file_name) as fp:
            #self.db = json.load(fp)
            pass
        
    def save(self):
        with open('CollageDB.json', 'w') as fp:
            #json.dump(self.db, fp)
            pass


c = Collage("gg")
db = CollageDataBase()
db.add(c)

c = db.search("gg")
c.data["GPA"] = 11

print(db.search("gg").data)

db.save()
    






