from gensim.models import Word2Vec


def test_most_similar(model, pos_words, neg_words, n_results):
	output = model.most_similar(positive=pos_words, negative=neg_words, topn=n_results)
	print('+%s -%s = %s' % (str(pos_words), str(neg_words), str(output)))



existing_model = Word2Vec.load('mymodel.dat')

print('\nresults:')
test_most_similar(['person','baby','child'], ['dog','tree'], 5)
test_most_similar(['man'], [], 3)
test_most_similar(['tree'], [], 3)
test_most_similar(['beginning', 'morning'], ['end'], 3)
