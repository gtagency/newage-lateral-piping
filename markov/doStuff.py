import re
from collections import Counter
import random

with open("debate.txt") as f:
    debate = f.read()

debate = debate.replace('\n',"")

debate=debate.replace("TRUMP:","\nTRUMP:")
debate=debate.replace("HOLT:","\nHOLT:")
debate=debate.replace("CLINTON:","\nCLINTON:")
debate=debate.splitlines()

trump_text = " ".join(line[7:]for line in debate if line.startswith("T"))
trump_text = re.sub('\(.*?\)',"",trump_text)

hillary_text = " ".join(line[7:]for line in debate if line.startswith("C"))
hillary_text = re.sub('\(.*?\)',"",hillary_text)

trump_text=trump_text.lower()
hillary_text=hillary_text.lower()


punctuation="?!.,'$:;"

for char in "?!.,'$:;-1234567890":
    trump_text=trump_text.replace(char,"")
    hillary_text=hillary_text.replace(char,"")
#print(trump_text)
#trump_counter=Counter(trump_text.split(" ")) #single word


length=2
trump_text=trump_text.split()
phrasesT=Counter(tuple(trump_text[i:i+length]) for i in range(len(trump_text)-length+1))
probabilitiesT = {}
length=1
prefixesT = Counter(tuple(trump_text[i:i+length]) for i in range(len(trump_text)-length+1))

length=2
hillary_text=hillary_text.split()
phrasesC=Counter(tuple(hillary_text[i:i+length]) for i in range(len(hillary_text)-length+1))
probabilitiesC = {}
length=1
prefixesC = Counter(tuple(hillary_text[i:i+length]) for i in range(len(hillary_text)-length+1))

for prefix in prefixesT:
    probabilitiesT[prefix]=[]
    for phrase in phrasesT:
        if(phrase[0]==prefix[0]):
            probabilitiesT[prefix].extend((int(phrasesT[phrase])*str(" "+phrase[1])).split())


for prefix in prefixesC:
    probabilitiesC[prefix]=[]
    for phrase in phrasesC:
        if(phrase[0]==prefix[0]):
            probabilitiesC[prefix].extend((int(phrasesC[phrase])*str(" "+phrase[1])).split())


word = "i"
s=""
for i in range(20):
    s +=" "+word
    if(word,) in probabilitiesT.keys():
        l = probabilitiesT[(word,)]
        r = int(random.random()*(len(l)-2))
        word= l[r]
print("Trump:"+s)

word = "i"
s=""
for i in range(20):
    s +=" "+word
    if(word,) in probabilitiesC.keys():
        l = probabilitiesC[(word,)]
        r = int(random.random()*(len(l)-2))
        word= l[r]
print("Hilary:"+s)

#type of markov chains
#?.! as words
#train multiple corpuses
#compare to common words
#distribution of words clinton vs trump
