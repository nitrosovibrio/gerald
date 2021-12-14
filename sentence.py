def fill(x,y):
	with open(y,'r') as filehandle:
		filecontents = filehandle.readlines()	
	for line in filecontents:
		current_place = line[:-1]
		x.append(current_place)
demo = []
adj = []
noun = []
verb = []
adv = []
pron = []
pronposs = []
art = []
prep = []
que = []
fill(demo, 'demo.txt')
fill(adj, 'adj.txt')
fill(noun, 'noun.txt')
fill(verb, 'verb.txt')
fill(adv, 'adv.txt')
fill(pron, 'pronoun.txt')
fill(pronposs, 'pron-poss.txt')
fill(art, 'article.txt')
fill(prep, 'prep.txt')
fill(que, 'questionwords.txt')

def scho(x):
	do = random.choice(x)
	return str(do)

import random
snoun = scho(noun)
snoun2 = scho(noun)
snoun3 = scho(noun)
sverb = scho(verb)
sverb2 = scho(verb)
sadj = scho(adj)
sadj2 = scho(adj)
sadv = scho(adv)
sadv2 = scho(adv)
spron = scho(pron)
spronposs = scho(pronposs)
sart = scho(art)
sart2 = scho(art)
sprep = scho(prep)
sprep2 = scho(prep)
sque = scho(que)
sdemo = scho(demo)
sdemo2 = scho(demo)

def chooseart(x, y):
	if y[0] == 'a':
		return x[2]
	elif y[0] == 'e':
		return x[2]
	elif y[0] == 'i':
		return x[2]
	elif y[0] == 'o':
		return x[2]
	elif y[0] == 'u':
		return x[2]
	else:
		return x[0]

sart = str(chooseart(art, snoun))
sart2 = str(chooseart(art, snoun2))
sart3 = str(chooseart(art, snoun3))
sartadj = str(chooseart(art, sadj))
sartadj2 = str(chooseart(art, sadj2))

def verbsing(x):
	if x[-1] == 'a':
		return str(x + "S")
	elif x[-1] == 'i' or x[-1] == 's' or x[-1] == 'o':
		return str(x + "es")
	elif x[-1] == 'y':
		return str(x.replace(x[-1], "ies"))
	else:
		return str(x + "s")

sverbsing1 = verbsing(sverb)
sverbsing2 = verbsing(sverb2)

def verbpron(x,y):
  if y == 'he' or y == 'she' or y == 'it':
    if x[-1] == 'a':
      return str(x + "S")
    elif x[-1] == 'i':
      return str(x + "es")
    elif x[-1] == 'o':
      return str(x + "es")
    elif x[-1] == 'y':
      return str(x.replace(x[-1], "ies"))
    else:
      return str(x + "s")
  else:
    return str(x)
sverbpron = str(verbpron(sverb,spron))
sverbpron2 = str(verbpron(sverb2,spron))

def pluralnoun(x):
  if x[-1] == 'y' and x[-2] == 'a':
    return(x + "s")
  elif x[-1] == 'y' and x[-2] == 'e':
    return(x + "s")
  elif x[-1] == 'y' and x[-2] == 'o':
    return(x + "s")
  elif x[-1] == 'y':
    return str(x.replace(x[-1], "ies"))
  else:
    return str(x + "s")

nounpl = pluralnoun(snoun)
nounpl2 = pluralnoun(snoun2)
nounpl3 = pluralnoun(snoun3)

sentence1 = sart + " " + snoun + " " + sadv + " " + sverbsing1 + " " + sprep + " " + spron

sentence2 = sverb + " " + sprep + " " + sadj + " " + snoun + " " + sprep2 + " " + sartadj2 + " " + sadj2 + " " + snoun2

sentence3 = spron + " " + sverbpron + " " + sprep + " " + sartadj + " " + sadj + " " + snoun + " " + sverbsing2

sentence4 =  sque + " " + sdemo + " " + snoun + " " + sverbsing1 + " " + spron + " " + sverbpron2 + " " + sadv

sentence5 = snoun + " " + sverbsing1 + " " + snoun2 + " " + sprep + " " + sdemo + " " + sadj + " " + snoun3

sentence6 = sart + " " + snoun + " " + sverbsing1 + " " + sque + " " + snoun2 + " " + sverbsing2

structure = [sentence1, sentence2, sentence3, sentence4, sentence5, sentence6]

def scho2(x):
	do2 = random.choice(x)
	return str(do2)
sentence = scho2(structure)

sentfile = open("sentenceout.txt","w")
sentfile.write(sentence.capitalize())
sentfile.close()
