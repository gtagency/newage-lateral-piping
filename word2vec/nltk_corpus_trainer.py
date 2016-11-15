from gensim.models import Word2Vec
from nltk import corpus

print('training model...')
b = Word2Vec(corpus.brown.sents())
b.save('brown_model.dat')
