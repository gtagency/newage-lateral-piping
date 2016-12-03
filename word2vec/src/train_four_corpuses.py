from nltk.corpus import brown, reuters, europarl_raw, gutenberg
from gensim.models import Word2Vec

Word2Vec(brown.sents() + reuters.sents() + europarl_raw.english.sents() + gutenberg.sents()).save('../models/trained_four.dat')
