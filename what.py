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
indob = []

fill(indob, 'indobj.txt')
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
snoun4 = scho(noun)
sverb = scho(verb)
sverb2 = scho(verb)
sverb3 = scho(verb)
sadj = scho(adj)
sadj2 = scho(adj)
sadj3 = scho(adj)
sadv = scho(adv)
sadv2 = scho(adv)
sadv3 = scho(adv)
spron = scho(pron)
spron2 = scho(pron)
spron3 = scho(pron)
spronposs = scho(pronposs)
scart = scho(art)
scart2 = scho(art)
scart3 = scho(art)
sprep = scho(prep)
sprep2 = scho(prep)
sprep3 = scho(prep)
sque = scho(que)
sdemo = scho(demo)
sdemo2 = scho(demo)
sindob = scho(indob)
sindob2 = scho(indob)

def chooseart(x, y):
    if x == 'a' or x == 'an':
        if y[0] == 'a' or y[0] == 'e' or y[0] == 'i' or y[0] == 'o' or y[0] == 'u':
            return str(x[2])
        else:
            return str(x[0])
    else:
        return str(x[1])

sart = str(chooseart(art, snoun))
sart2 = str(chooseart(art, snoun2))
sart3 = str(chooseart(art, snoun3))
sart4 = str(chooseart(art, snoun4))
sartadj = str(chooseart(art, sadj))
sartadj2 = str(chooseart(art, sadj2))

def demopl(x,y):
    if x == 'these' or x == 'those':
        if y[-1] == 'y' and y[-1] == 'o':
            return str(y + 's')
        elif y[-1] == 'y' and y[-1] == 'u':
            return str(y + 's')
        elif y[-1] == 'y' and y[-1] == 'a':
            return str(y + 's')
        elif y[-1] == 'y' and y[-1] == 'e':
            return str(y + 's')
        elif y[-1] == 'y':
            return str(y.replace(y[-1], 'ies'))
        elif y[-1] != 'y':
            return str(y + "s")
    else:
        return str(y)

snounsing = demopl(sdemo, snoun)
snounsing2 = demopl(sdemo, snoun2)
snounsing3 = demopl(sdemo, snoun3)
def verbsing(x, y):
    if y == 'they' or y == 'I' or y == 'you':
        return str(x)
    elif y == 'he' or y == 'she' or y == 'it':
        if x[-1] == 'i' or x[-1] == 's' or x[-1] == 'o' or x[-1] == 'h' or x[-1] == 'x':
            return str(x + "es")
        elif x[-1] == 'y':
            return str(x.replace(x[-1], "ies"))
        else:
            return str(x + 's')
    else:
        if x[-1] == 'i' or x[-1] == 's' or x[-1] == 'o' or x[-1] == 'h' or x[-1] == 'x':
            return str(x + "es")
        elif x[-1] == 'y':
            return str(x.replace(x[-1], "ies"))
        else:
            return str(x + "s")
  

svsingpron1 = verbsing(sverb, spron)
svsingpron2 = verbsing(sverb2, spron2)
svsingpron3 = verbsing(sverb3, spron3)
svsing3pron2 = verbsing(sverb3, spron2)
svsingnoun1 = verbsing(sverb, snoun)
svsingnoun2 = verbsing(sverb2, snoun2)
svsingnoun3 = verbsing(sverb3, snoun3)
svsing2noun1 = verbsing(sverb2, snoun)

def verbdemo(x,y):
    if x == 'these' or x == 'those':
        return str(y)
    else:
        if y[-1] == 'y' and 'a':
            return str(y + 's')
        elif y[-1] == 'y' and 'o':
            return str(y + 's')
        elif y[-1] == 'y' and 'u':
            return str(y + 's')
        elif y[-1] == 'y' and 'e':
            return str(y + 's')
        elif y[-1] == 'y':
            return str(replace.y(y[-1], 'ies'))
        elif y[-1] == 'h' or y[-1] == 's' or y[-1] == 'x':
            return str(y + 'es')
        else:
            return str(y + 's')
        
sverb1demo1 = verbdemo(sdemo, sverb)

def verbpron(x,y):
  if y == 'he' or y == 'she' or y == 'it':
    if x[-1] == 'a':
      return str(x + "s")
    elif x[-1] == 'i' or x[-1] == 'o' or x[-1] == 'h' or x[-1] == 's' or x[-1] == 'x':
      return str(x + "es")
    elif x[-1] == 'y' and x[-2] == 'o':
      return str(x + 's')
    elif x[-1] == 'y' and x[-2] == 'a':
      return str(x + 's')
    elif x[-1] == 'y' and x[-2] == 'e':
      return str(x + 's')
    elif x[-1] == 'y' and x[-2] == 'u':
      return str(x + 's')
    elif x[-1] == 'y':
      return str(x.replace(x[-1], "ies"))
    else:
      return str(x + "s")
  else:
    return str(x)
sverbpron = str(verbpron(sverb,spron))
sverbpron2 = str(verbpron(sverb2,spron))
sverbpron3 = str(verbpron(sverb3,spron))

def pluralnoun(x):
  if x[-1] == 'y' and x[-2] == 'a':
    return(x + "s")
  elif x[-1] == 'y' and x[-2] == 'e':
    return(x + "s")
  elif x[-1] == 'y' and x[-2] == 'o':
    return(x + "s")
  elif x[-1] == 'y' and x[-2] == 'u':
    return(x + "s")
  elif x[-1] == 'y':
    return str(x.replace(x[-1], "ies"))
  elif x[-1] == 'h':
    return(x + "es")
  else:
    return str(x + "s")

nounpl = pluralnoun(snoun)
nounpl2 = pluralnoun(snoun2)
nounpl3 = pluralnoun(snoun3)

sentence1 = sart + " " + snoun + " " + sadv + " " + svsingnoun1
sentence2 = spron + " " + sverbpron + " " + sprep + " " + sadj + " " + snoun + ", " + sartadj2 + " " + sadj2 + " " + snoun2 + " " + svsingnoun2
sentence3 = spron + " " + sverbpron + " " + sprep + " " + sartadj + " " + sadj + " " + snoun
sentence4 = sque + " " + sdemo + " " + snounsing + " " + sverb1demo1 + ", " + spron + " " + sverbpron2 + " " + sadv
sentence5 = snoun + " " + svsingnoun1 + " " + snoun2 + " " + sadv
sentence6 = sart + " " + snoun + " " + svsingnoun1 + " " + sque + " " + snoun2 + " " + svsingnoun2
sentence7 = spron + " " + sadv + " " + svsingpron1 + " " + snoun + ", " + sart2 + " " + snoun2 + " " + svsingnoun2 + " " + sprep2 + " " + sart3 + " " + snoun3
sentence8 = spron + " " + sverbpron + " " + sque + " " + sart + ' ' + snoun + " " + svsing2noun1
sentence9 = sdemo + " " + snounsing + " " + sverb1demo1 + " " + sindob
sentence10 = sartadj + ' ' + sadj + ' ' + snoun + ' ' + svsingnoun1 + ' ' + sindob
sentence11 = sart4 + " " + snoun4 + ' ' + svsing3pron2 + " " + sart3 + ' ' + snoun3 + ' ' + sprep + " " + sartadj2 + " " + sadj2 + " " + snoun2 

structure = [sentence11, sentence1, sentence2, sentence3, sentence4, sentence5, sentence6, sentence7, sentence8, sentence9, sentence10]

def scho2(x):
    do2 = random.choice(x)
    return str(do2)
sentence = scho2(structure)

sentfile = open("what-out.txt","w")
sentfile.write(sentence.capitalize())
sentfile.close()
