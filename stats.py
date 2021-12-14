f1 = open("output-stats.txt","w")
import random
stats = ["Vitality ","Attunement","Endurance","Strength","Dexterity","Resistance","Intelligence","Faith"]
def level(x):
	dothis = random.choices(stats, k=x)
	return(dothis)
val = int(input("How many levels? "))
dothen = str(level(val))[1:-1]
thendo = dothen.replace("'","")
thendo2 = thendo.replace(",","\n")
thendo3 = thendo2.replace(" ","")
f1.write("Gerald chooses\n to level:\n" + thendo3)
f1.close()