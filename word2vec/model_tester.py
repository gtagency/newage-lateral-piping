from gensim.models import Word2Vec


def test_most_similar(model, pos_words, neg_words, n_results):
	output = model.most_similar_cosmul(positive=pos_words, negative=neg_words, topn=n_results)
	print('+%s -%s = %s' % (str(pos_words), str(neg_words), str(output)))

def test_similar(model, word1, word2):
	output = model.similarity(word1, word2)
	print('similar(%s, %s) = %f' % (str(word1), str(word2), (output)))

existing_model = Word2Vec.load('models/simpleModel Size1000 Min10 SG0')

print('\nresults:')
#test_most_similar(existing_model, ['person','baby','child'], ['dog','tree'], 5)
#test_most_similar(existing_model, ['man'], [], 3)
#test_most_similar(existing_model, ['beginning', 'morning'], ['end'], 3)
#test_most_similar(existing_model, ['tree'], [], 3)
test_similar(existing_model, 'man', 'woman')
test_similar(existing_model, 'soccer', 'football')
test_similar(existing_model, 'woman', 'queen')
test_similar(existing_model, 'envy', 'jealousy')
#print(existing_model.doesnt_match("breakfast cereal dinner lunch".split()))
#print(existing_model.most_similar(positive=['woman', 'king'], negative=['man']))
