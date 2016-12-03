from gensim.models import Word2Vec
from word2vec_regex import list_of_questions


# To solve the analogy -> a : b :: c : [one of the four options in d]
# Function calculates the distance of vector(a) - vector(b) - vector(c) + vector([each element in d]) from origin
# Returns the option in d with least distance
def main(a, b, c, d):
    dictionary = {}
    try:
        vector = model[a] - model[b] - model[c]
        for option in d:
            vectorTmp = vector + model[option]  # our goal is to choose an option with vector closest to origin
            squarederror = 0
            for element in vectorTmp:
                squarederror += element ** 2
            dictionary[option] = squarederror  # maps each option in d to it's error
        # print(dictionary)
        return min(dictionary.items(), key=lambda x: x[1])[0]
    except KeyError as e:
        return 'Key Error ' + e.args[0]


if __name__ == '__main__':
    model = Word2Vec.load('../models/trained_four.dat')  # loading model

    result_text = open('../output_file/analogy_answers_trained_four.txt', 'w')
    actual_answers_text = open('../input_files/answers.txt', 'r')

    list_of_answers = actual_answers_text.read().splitlines()
    result_text.write('Question'.ljust(40) + 'ActualAnswer'.ljust(20) + 'ModelAnswer'.ljust(25) + '1/0\n\n')
    count_of_correct = 0

    # sample format of query-
    # print(main('fire', 'hot', 'ice', ['cold', 'tired', 'blue']))
    for (question, answer) in zip(list_of_questions, list_of_answers):
        model_answer = main(question[0], question[1], question[2], question[3])
        if model_answer == answer:
            result = 1
            count_of_correct += 1
        else:
            result = 0
        result_text.write(('%s : %s :: %s : ____' % (question[0], question[1], question[2])).ljust(40)
                          + ('%s' % answer).ljust(20) + ('%s' % model_answer).ljust(25)
                          + '%d\n' % result)
    result_text.write('\nAccuracy: %.2f%%' % (count_of_correct/len(list_of_answers) * 100))

    result_text.close()
    actual_answers_text.close()
