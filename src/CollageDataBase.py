import json

class Collage:
    
    aliases = {
        "nick name" : "offical name",
        "UIUC" : "University of Illinois Urban Champaighn"    
    }
    
    meta_data = {  
        "SAT" : {"math" : [25, 50, 75],
                 "reading" : [25, 50, 75]
                },
        
        "ACT" : 0,
        "GPA" : 0,
        "ACPT Rate" : 0
    }
    
    def __init__(self, name):
        
        if (name in Collage.aliases):
            self.name = Collage.aliases[name]
        else:
            self.name = name
        
        self.data = Collage.meta_data


class CollageDataBase:
    def __init__(self):
        self.db = {}
    
    def add(self, collage):
        self.db[collage.name] = collage.data
    
    def load(self, file_name):
        with open(file_name) as fp:
            self.db = json.load(fp)
        
    def save(self):
        with open('CollageDB.json', 'w') as fp:
            json.dump(self.db, fp)


c = Collage("gg")
db = CollageDataBase()
db.add(c)

db.save()
    






