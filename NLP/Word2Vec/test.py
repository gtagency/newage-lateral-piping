import logging
import gensim
from gensim.models import Word2Vec
from gensim import corpora, models, similarities
from nltk.corpus import brown
#b = Word2Vec(  brown.sents(), workers = 4)
#b.save('/tmp/mymodel')

new_model = gensim.models.Word2Vec.load('/tmp/mymodel')
print(new_model.similar_by_vector([9,8], topn=10, restrict_vocab=None))
#COCA corpus
#save a mmodels