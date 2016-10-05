import random

#user-controlled parameters
ngram_lengths = (7,11,15)
output_length = 1000
fname = '../corpus/war_and_peace.txt'

#initialize other variables
ngram_lengths = tuple(sorted(ngram_lengths, reverse=True))
ngram_dict = {}
corpus = ''

#read from sample
print('source', fname)
with open(fname, 'r') as txtfile:
    generator = (c for c in txtfile.read().replace('\n', ' ')
                   if not c in '.,?!@#$%^&*()\'":;<>/\\|[}{]'
                )
    for char in generator:
        corpus += char
    corpus = corpus.lower()

#crawl over body of text for n-grams
for n in ngram_lengths:
    ngram_dict[n] = {}
    print('learning %d-grams' % n)
    for i in range(len(corpus)-n):
        prev = corpus[i: i+n]
        if prev in ngram_dict[n].keys():
            ngram_dict[n][prev].append(corpus[i+n])
        else:
            ngram_dict[n][prev] = [corpus[i+n]]

for n, subdict in ngram_dict.items():
    #print(n, len(subdict))
    avg = sum(len(item) for item in subdict.values()) / len(subdict)
    print(n, 'has avg of', avg, 'entries per prev key')


print('generating', output_length, 'characters of text')

#initialize text to a random ngram from the longest class
text = random.choice(tuple(ngram_dict[ngram_lengths[0]].keys()))

#generate random text
n_defaults = 0
counts = {}
for n in ngram_lengths:
    counts[n] = 0

for _ in range(output_length):
    n_idx = random.randrange(len(ngram_lengths))
    n_ideal = ngram_lengths[n_idx]
    for n in ngram_lengths[n_idx:]:
        prev = text[-n:]
        if prev in ngram_dict[n].keys():
            text += random.choice(ngram_dict[n][prev])
            if not n == n_ideal:
                #print('ideal is', n_ideal, 'but used', n)
                n_defaults += 1
            counts[n] += 1
            break;

print('length of ngram decreased', n_defaults, 'times')
for n in ngram_lengths:
    print('n=%d used %d times' % (n, counts[n]))

#with open('markov_output.txt', 'w') as output_file:
#    output_file.write(text)

print(text)
