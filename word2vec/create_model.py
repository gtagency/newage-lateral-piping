import os
import glob
import gensim
import itertools
import re
from lxml import html

ignore = re.compile('\n|\"|\(|\)|,|')
punct = re.compile('\?|!')

file_dir = '/mnt/e/wiki/out/'
filenames = (itertools.chain.from_iterable(glob.glob(os.path.join(x[0], 'wiki_*')) for x in os.walk(file_dir)))


def wiki_data():
    for name in filenames:
        with open(name) as f:
            print(name)
            data = process(f.read())
            for s in data:
                for x in s:
                    yield [w for w in x.split()]

def process(file_contents):
    tree = html.fromstring(file_contents)
    tagless = html.tostring(tree, encoding='utf-8', method='text').lower()
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

b = gensim.models.Word2Vec(WikiIterator(wiki_data), workers=4, size=50, min_count=4,  sg=1, window=4)
b.save('/mnt/e/wiki/model')
