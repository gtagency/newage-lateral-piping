import re
import random
from collections import Counter
with  open("hp.txt.rtf") as f:
    hp = f.read()
    hp.replace('\n',"").replace("?"," " ).replace("."," " ).replace(",", " ").replace("!", " ").replace("'", "")
    hp.replace("$", " ").replace("-"," ")
    hp.splitlines();
    length=3
    corpus = hp.split()
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
