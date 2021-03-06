import os
import glob
import gensim
import itertools
import re
from lxml import html

ignore = re.compile('\n|\"|\(|\)|,|')
punct = re.compile('\?|!')

file_dir = '../../../simplewiki'
filenames = ( #an iterable over file names
    itertools.chain.from_iterable(
        glob.glob(os.path.join(x[0], 'wiki_*')) for x in os.walk(file_dir)
    )
)


def wiki_data():
    for name in filenames:
        with open(name, encoding= 'utf-8') as f:
            print(name)
            data = process(f.read())
            for s in data:
                for x in s:
                    yield [w for w in x.split()]

def process(file_contents):
    tree = html.fromstring(file_contents)
    tagless = html.tostring(tree, encoding='utf-8', method='text').lower().decode("utf-8")
    sentences = ignore.sub('', punct.sub('.', tagless)).split('.')
    yield sentences

class WikiIterator:
    def __init__(self, f):
        self.f = f
        self.gen = f()

    def __iter__(self):
        gen = self.gen
        self.gen = self.f()
        return gen

_min_count = 50
_size = 100

b = gensim.models.Word2Vec(WikiIterator(wiki_data), 
    workers=4, size=_size, min_count=_min_count,  sg=1, window=4
)
b.save('models/simplewiki_model_min%d_size%d' % (_min_count, _size))
