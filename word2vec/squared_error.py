from gensim.models import Word2Vec
from word2vecRegex import list_of_questions


# To solve the analogy -> a : b :: c : [one of the four options in d]
# Function calculates the distance of vector(a) - vector(b) - vector(c) + vector([each element in d) from origin
# Returns the option in d with least distance
def main(a, b, c, d):
    try:
        vector = model[a] - model[b] - model[c]
    except KeyError as e:
        return 'Key ' + e.args[0] + ' not in corpus'
    dictionary = {}
    for option in d:
        try:
            vector += model[option]  # our goal is to choose an option with vector closest to origin
        except KeyError:
            return 'Key not in corpus'
        squarederror = 0
        for element in vector:
            squarederror += element ** 2
        dictionary[option] = squarederror  # maps each option in d to it's error
    # print(dictionary)
    return min(dictionary.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    model = Word2Vec.load('vals_model.dat')
    answers_text = open('analogy_answers_vals_model.txt', 'w')
    # sample format of query
    print(main('king', 'queen', 'man', ['woman', 'table', 'person', 'royalty']))
    for question in list_of_questions:
        answers_text.write(main(question[0], question[1], question[2], question[3]) + '\n')
    answers_text.close()
