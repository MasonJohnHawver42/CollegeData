from CollageDataBase import *
from csv import reader


valerr = 0

def NUM(s):
    try: 
        v = float(s)
        return v
    except ValueError:
        global valerr
        valerr += 1
        return "Nan"

def OR(v1, v2):
    iv1 = INT(v1)
    iv2 = INT(v2)
    
    if iv1 == "Nan" and iv2 == "Nan":
        return "Nan"
    elif type(iv1) is int and iv2 == "Nan":
        return iv1
    elif type(iv2) is int and iv1 == "Nan":
        return iv2
    return iv1


fn = "C:/Users/hawverm2967/Downloads/Pyhon/CollegeData/data/Aliases.txt"

f = open(fn, "r")
names = f.read().split("\n")

fn = "C:/Users/hawverm2967/Downloads/Pyhon/CollegeData/data/CollegeScorecard_Raw_Data_01192021/Raw Data Files/MERGED2018_19_PP.csv"

with open(fn, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    
    name_i = header.index("INSTNM")
    
    amdr_i1 = header.index("ADM_RATE_ALL")
    amdr_i2 = header.index("ADM_RATE")
    
    msat75_i = header.index("SATMT75")
    msat50_i = header.index("SATMTMID")
    msat25_i = header.index("SATMT25")
    
    rsat75_i = header.index("SATVR75")
    rsat50_i = header.index("SATVRMID")
    rsat25_i = header.index("SATVR25")
    
    act_i = header.index("ACTCMMID")
    
    db = CollageDataBase()
    
    i = 0
    j = 0
    while i < 3000:
        row = next(csv_reader)
        
        rn = row[name_i]
        
        name = rn.split("-")
        camp = name[1] if len(name) > 1 else ""
        name = name[0].lower()
        
        if name in names:
            print(name, camp, j)
            j += 1
        
        #c = Collage(name)
        
        #p = valerr
        #c.data["SAT"]["math"] = [NUM(row[msat25_i]), NUM(row[msat50_i]), NUM(row[msat75_i])]
        #c.data["SAT"]["reading"] = [NUM(row[rsat25_i]), NUM(row[rsat50_i]), NUM(row[rsat75_i])]
        
        #c.data["ACT"] = NUM(row[act_i])
        
        #c.data["ACPT Rate"] = NUM(row[amdr_i1])
        
        #if valerr - p == 0 and c.data["ACPT Rate"] < .2:
        #    print(name, c.data)
        
    
    print(j)
    
        