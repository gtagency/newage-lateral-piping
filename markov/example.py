import re
from collections import Counter
import random

with open('debate.txt') as f:
    debate = f.read()

# clean the text and split over clinton and trump
debate = debate.replace('\n', '')
debate = debate.replace('TRUMP:', '\nTRUMP:')
debate = debate.replace('HOLT:', '\nHOLT:')
debate = debate.replace('CLINTON:', '\nCLINTON:')
debate = debate.splitlines()

# get all of trump's text together in one blob
# to do this for clinton, change 7 to 9 and T to C
trump_text = ' '.join([line[7:] for line in debate if line.startswith('T')])
trump_text = re.sub(r'\(.*?\)', '', trump_text)
tt = trump_text.lower()
# remove punctuation
tt = tt.replace('.', ' ')
for char in "',?!-$:;":
    tt = tt.replace(char, '')

corpus = tt.split()
length = 3  # n-gram length, change to 2 for bigrams

# create prefix -> word probability 'table'
# samples[prefix_tuple] = Counter<next_word_string>
samples = dict()
for i in range(len(corpus) - length):
    pref = tuple(corpus[i:i+length-1])
    nxt = (corpus[i+length-1],)
    if not pref in samples.keys():
        samples[pref] = Counter()
    samples[pref].update(nxt)

# on run, create 25 random generated grams, the seed words are chosen at random from the
# seed text, in line with their probability
for i in range(25):
    first_words = random.choice(tuple(samples.keys()))
    sentence = list()
    sentence.extend(first_words)

    while random.random() < .92:  # lazy end condition, since we aren't tracking PERIOD characters
        pref = tuple(sentence[-(length-1):])
        sentence.append(random.choice(tuple(samples[pref].elements())))

    print( ' '.join(sentence), end='\n\n')
