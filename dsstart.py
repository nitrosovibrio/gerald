#load to file
#rename dsstart.py
#run 'py dsstart.py'
#exports to 'outstart.txt'
outstart = open("outstart.txt",'w')
dsclasses = []
with open('dsclasses.txt','r') as filehandle:
  filecontents = filehandle.readlines()
  for line in filecontents:
    current_place = line[:-1]
    dsclasses.append(current_place)
dsgifts = []
with open('dsgifts.txt','r') as filehandle:
  filecontents = filehandle.readlines()
  for line in filecontents:
    current_place = line[:-1]
    dsgifts.append(current_place)
import random
do = str(random.choice(dsclasses))
do2 = str(random.choice(dsgifts))
do3 = "Class: " + do + "\n" + "Burial Gift: " + do2
outstart.write(do3)
outstart.close()