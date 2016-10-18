import logging
from gensim.models import Word2Vec
from gensim import corpora, models, similarities
from nltk.corpus import brown
b = Word2Vec(brown.sents())
print(b.most_similar_cosmul(positive=['person','baby'],negative = ["dog"], topn=5))
#COCA corpus
#save a mmodel