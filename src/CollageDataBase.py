import json
  
def normalize_name(n):
    name = n.lower()
    name = name.strip()
    name = name.replace("  ", " ")
    name = name.replace("  ", " ")
    name = "".join([ word for word in name.split(" ") if word not in ["and", "of", "at"]])
    name = "".join([ char for char in name if char.isalpha()])
    return name


class Collage:
    
    meta_data = {
        
        "rank": "-1",
        
        "SAT" : {"math" : [25, 50, 75],
                 "reading" : [25, 50, 75]
                },
        
        "ACT" : {"math" : [25, 50, 75],
                 "reading" : [25, 50, 75]
                },
        
        "ACPT Rate" : 0,
        
        "Net": 0,
        "Starting": 0,
        
        "Enrolment": 0,
        "Grad Rate": 0,
        "SF ratio": 0,
        
        "Address": "",
        
        "conference": "",
        "division": "",
        
        "Majors" : [("Basket Weaving", 100)],
        
        "default" : True
    }
    
    def __init__(self, name):
        self.name = name.split("-")[0].strip().lower()
        self.subname = name.split("-")[1].strip().lower() if "-" in name else ""
        self.asubname = name.split("~")[1] if "~" in self.name else "Main Campus"
        
        self.data = Collage.meta_data.copy()
    
    def getName(self):
        return self.name + (("-" + self.subname) if self.subname != "" else "")
        


class CollageDataBase:
    
    def __init__(self):
        self.collages = []
    
    def add(self, collage):
        self.collages.append(collage)
    
    def search(self, name):
        
        name = name.split("-")
        sname = name[1] if len(name) > 1 else ""
        name = name[0]
        
        for collage in self.collages:
            if normalize_name(collage.name) == normalize_name(name):
                if normalize_name(collage.subname) == normalize_name(sname):
                    return collage
                elif normalize_name(sname) == normalize_name(collage.asubname):
                    return collage
                else:
                    print(name, "!!!", collage.subname, " | " , sname)
    
    def load(self, file_name):
        with open(file_name) as fp:
            self.collages = []
            data = json.load(fp)
            
            for k, v in data.items():
                c = Collage(k)
                c.data = v
                self.add(c)
        
    def save(self):
        with open('CollageDB.json', 'w') as fp:
            data = {}
            for collage in self.collages:
                data[collage.getName()] = collage.data
            
            json.dump(data, fp, indent=4)
    
    def __repr__(self):
        pass


fn = "C:/Users/hawverm2967/Downloads/Pyhon/CollegeData/data/Aliases.txt"

f = open(fn, "r")
names = f.read().split("\n")

db = CollageDataBase()

for name in names:
    normalize_name(name)
    c = Collage(name)
    db.add(c)

db.save()





