import logging
from gensim.models import Word2Vec
from gensim import corpora, models, similarities
new_model = gensim.models.Word2Vec.load('/tmp/mymodel')
print(new_model.most_similar(positive=['person','baby','child'],negative = ['dog','tree'], topn=5))