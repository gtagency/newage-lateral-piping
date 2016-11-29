import re
import random
from collections import Counter


def main():
    # opening input and output files
    inputFile = open("debate.txt", "r")
    outputClinton = open("clinton.txt", "w")
    outputTrump = open("trump.txt", "w")
    outputHolt = open("holt.txt", "w")

    # formatting input data
    inputFileData = inputFile.read().replace("\n", "")  # remove all new line characters, put entire text in one line
    inputFileData = inputFileData.replace("HOLT:", "\nHOLT:")  # each speech by each speaker is on a distinct line
    inputFileData = inputFileData.replace("CLINTON:", "\nCLINTON:")
    inputFileData = inputFileData.replace("TRUMP:", "\nTRUMP:")
    inputFileData = inputFileData.splitlines()

    trumpText = " ".join(
        line[7:] for line in inputFileData if line.startswith('T'))  # combining all of trump's speeches
    holtText = " ".join(line[6:] for line in inputFileData if line.startswith('H'))
    hilaryText = " ".join(line[9:] for line in inputFileData if line.startswith('C'))

    # removing text enclosed in parenthesis
    trumpText = re.sub(r'\(.*?\)', "", trumpText).lower()
    holtText = re.sub(r'\(.*?\)', "", holtText).lower()
    hilaryText = re.sub(r'\(.*?\)', "", hilaryText).lower()

    # removing punctuations
    for char in ".!?,'$:;-\"":
        trumpText = trumpText.replace(char, "")
        holtText = holtText.replace(char, "")
        hilaryText = hilaryText.replace(char, "")

    length = 2  # setting length to 2 for Bigram
    # generating for clinton only-
    corpus = hilaryText.split()
    # generating Bigrams, sequence of two-word pairings and using Counter to total their occurences
    """e.g. - ["The", "time", "of", "day"] would return {('of', 'day'): 1, ('time', 'of'): 1, ('The', 'time'): 1}"""
    grams = Counter(tuple(corpus[i:i + length]) for i in range(len(corpus) - length + 1))
    # generating prefixes, single words
    """e.g. - ["The", "time", "of", "day"] would return {('The',): 1, ('time',): 1}"""
    prefixes = Counter(tuple(corpus[i:i + length - 1]) for i in range(len(corpus) - length - 1 + 1))
    samples = dict()
    for prefix in prefixes:
        samples[prefix] = []
        for gram in grams:
            if prefix == gram[:-1]:  # list[:-1] returns everything, but last element. Since length of each gram in only
                # two here, gram[:-1] just gives the first word
                samples[prefix].extend([gram[-1]] * grams[gram])  # extend is similar to extend, except that it appends
                # elements from the iterable. Therefore [1, 2].extend([3]) gives [1, 2, 3] and not [1, 2, [3]] as
                # .append([3]) would have given
                # grams[gram] gives the number of occurences of that particular gram
                # gram[-1] returns the last element of the list/tuple
                """E.g. of what samples would look like - {'The' : ['time', 'time', 'lack']} Here, 'The' was a prefix in
                 prefixes; ('The', 'time') : 2 and ('The','lack) : 1 were elements in grams"""
    hilaryText = ""
    for i in range(25): # num of sentences
        first_words = random.choice(list(prefixes.elements()))  # random first word chosen
        sentence = []
        sentence.extend(first_words)
        while random.random() < .92: # this number decides how long/short our sentences are
            sentence.append(random.choice(samples[tuple(sentence[-(length - 1):])]))  # listName[-1:] returns a list
            # containing the last element. listNme[-1] only returns the element, but not as a list
        hilaryText += ' '.join(sentence) + "\n"
    # writing to output files
    outputTrump.write(trumpText)
    outputClinton.write(hilaryText)
    outputHolt.write(holtText)
    inputFile.close()
    outputTrump.close()
    outputClinton.close()
    outputHolt.close()


if __name__ == '__main__':
    main()
