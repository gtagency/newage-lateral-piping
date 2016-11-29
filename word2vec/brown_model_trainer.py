from nltk.corpus import brown
from gensim.models import Word2Vec

Word2Vec(brown.sents()).save('trained_brown')
