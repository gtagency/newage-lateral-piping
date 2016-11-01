import re
import random
from collections import Counter
with  open("../corpus/debate.txt") as f:
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
    corpus = clinton_text.split()
    grams = Counter(tuple(corpus[i:i+length]) for i in range(len(corpus) - length + 1))
    prefixes = Counter(tuple(corpus[i:i+length-1]) for i in range(len(corpus) - length - 1 + 1))


samples = dict()
for prefix in prefixes:
    samples[prefix] = []
    for gram in grams:
        if prefix == gram[:-1]:
            samples[prefix].extend([gram[-1]] * grams[gram])


for i in range(25):
    first_words = random.choice(list(prefixes.elements()))
    sentence = list()
    sentence.extend(first_words)

    while random.random() < .92:  
        sentence.append(random.choice(samples[tuple(sentence[-(length-1):])]))

    print( ' '.join(sentence), end='\n\n')

    
    