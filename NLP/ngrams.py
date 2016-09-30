import re
from collections import Counter
with  open("debate.txt") as f:
    debate = f.read()
    debate = debate.replace('\n',"").replace("?"," " ).replace("."," " ).replace(",", " ").replace("!", " ").replace("'", "")
    debate = debate.replace("CLINTON:","\nC").replace("TRUMP:","\nT").replace("HOLT:", "\nH").replace("$", " ").replace("-"," ")
    debate= debate.splitlines()
    trump_text = " ".join(line[7:] for line in debate if line.startswith('T'))
    clinton_text = " ".join(line[9:]for line in debate if line.startswith('C'))
    
    holt_text = " ".join(line[6:]for line in debate if line.startswith('H'))
    
    re.sub(r"\(.*?\)","",trump_text)
    re.sub(r"\(.*?\)","",clinton_text)
    re.sub(r"\(.*?\)","",holt_text)
    trump_text = trump_text.lower().replace(":", " ").replace(";", " ")
    clinton_text = trump_text.lower().replace(":", " ").replace(";", " ")
    holt_text = holt_text.lower().replace(":", " ").replace(";", " ")
    tc = Counter(trump_text.split())
    cc = Counter(clinton_text.split())
    hc = Counter(holt_text.split())
    length=2
    corpus = trump_text.split()
    thing = Counter(tuple(corpus[i:i+length]) for i in range (len(corpus) - length+1))
    newc = Counter(tuple(corpus[i:i+length]) for i in range (length-1))
    probabilities = {}
    for prefix in prefixes.lines():
        probabilities[prefix] = []
        for newc in phrases.keys():
            if newc[0] == prefix:
                probabilities[prefix].extend(list(phrases[-1]*newc[phrase]))
                
    print(thing)
    
    