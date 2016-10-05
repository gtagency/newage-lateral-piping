from collections import Counter
import random
import sys

if len(sys.argv) < 2:
    print('please pass me a file')

with open(sys.argv[1], 'r') as f:
    text = f.read()

print('cleaning text...')
# clean the text
text = text.replace('\n', ' ').lower()

# remove punctuation
for char in ".-/\\":
    text = text.replace(char, ' ')
for char in "'(),?!$%^&*:;\"":
    text = text.replace(char, '')

print('creating prefix-to-word probability table...')
corpus = text.split()
length = 4  # n-gram length, change to 2 for bigrams

# samples[prefix_tuple] = Counter<next_word_string>
samples = dict()
for i in range(len(corpus) - length):
    pref = tuple(corpus[i:i+length-1])
    nxt = (corpus[i+length-1],)
    if not pref in samples.keys():
        samples[pref] = Counter()
    samples[pref].update(nxt)

# on run, create 25 random generated grams.
# the seed words are chosen at random from the
# seed text, in line with their probability
print('generating text...')
for i in range(25):
    first_words = random.choice(tuple(samples.keys()))
    sentence = list()
    sentence.extend(first_words)

    # lazy end condition, since we aren't tracking PERIOD characters
    while random.random() < .95:
        pref = tuple(sentence[-(length-1):])
        sentence.append(random.choice(tuple(samples[pref].elements())))

    print( ' '.join(sentence), end='\n\n')
