
fn = "C:/Users/hawverm2967/Downloads/Pyhon/CollegeData/data/names.txt"

f = open(fn, "r")
names = f.read().split("\n")

w = open("demofile2.txt", "w+")

for name in names:
    name = name.split("/")[4]
    name = " ".join(name.split("-"))
    name = name.split("   ")[0]
    w.write(name + "\n")
    

w.close()