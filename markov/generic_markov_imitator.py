import re
from collections import Counter
import random
import sys

if len(sys.argv) < 2:
    print('please pass me a file')

with open(sys.argv[1], 'r') as f:
    text = f.read()

print('cleaning text...')
# clean the text
text = text.replace('\n', ' ')

text = text.lower()
# remove punctuation
text = text.replace('.', ' ')
for char in "'(),?!-$:;":
    text = text.replace(char, '')

corpus = text.split()

print('scanning for ngrams...')
length = 3  # n-gram length, change to 2 for bigrams
grams = Counter(tuple(corpus[i:i+length]) for i in range(len(corpus) - length + 1))
prefixes = Counter(tuple(corpus[i:i+length-1]) for i in range(len(corpus) - length))

print('creating prefix -> word probability table...')
# create prefix -> word probability 'table'
samples = dict()
for prefix in prefixes:
    samples[prefix] = []
    for gram in grams:
        if prefix == gram[:-1]:
            samples[prefix].extend([gram[-1]] * grams[gram])

# on run, create 25 random generated grams.
# the seed words are chosen at random from the
# seed text, in line with their probability
print('generating text...')
for i in range(25):
    first_words = random.choice(list(prefixes.elements()))
    sentence = list()
    sentence.extend(first_words)

    # lazy end condition, since we aren't tracking PERIOD characters
    while random.random() < .95:
        sentence.append(random.choice(samples[tuple(sentence[-(length-1):])]))

    print( ' '.join(sentence), end='\n\n')
