import logging
import gensim
from gensim.models import Word2Vec
from gensim import corpora, models, similarities
from nltk.corpus import brown,reuters
#from nltk.book import *
#b = Word2Vec(  brown.sents()+reuters.sents() , workers = 4)
#b.save('/tmp/mymodel')
b = Word2Vec.load('/tmp/mymodel')
print(b.most_similar("baby", topn=10, restrict_vocab=None))
#COCA corpus
#save a mmodels