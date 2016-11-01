import sys
from gensim.models import Word2Vec

if len(sys.argv) < 2:
    print("Usage: python file_trainer.py [filepath]")
    sys.exit()

filepath = sys.argv[1]
print('reading from', filepath, '...')
sents = []
delete_chars = '@#$%^&*()=}]{[<>\t1234567890'
separator_chars = '.;:?!-_+,\"\n'
with open(filepath, 'r') as file:
    for line in file:
        s = ''
        for char in line.lower():
            if not char in delete_chars:
                s += ' ' if char in separator_chars else char
        sents.append(s)

# sentence format: [['Hi', ',', my', 'name', 'is', 'Evan', '.'],
#                   ['It's', 'nice', 'to', 'meet', 'you', '.']]
corpus = []
for sentence in sents:
    corpus.append(sentence.split())
#print(corpus)

print('starting training ...')
model = Word2Vec(corpus, size=100, iter=5)

print('saving ...')
model.save('mymodel.dat')

print('done.')
