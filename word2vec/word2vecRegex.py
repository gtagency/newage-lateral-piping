# Sample query answer - ['train', 'board', 'horse', ['stable', 'shoe', 'ride', 'mount']] if question if of form
# ______ : horse :: board : train
# a.
# stable
# b.
# shoe
# c.
# ride
# d.
# mount
import re

questions_text = open('analogy_questions.txt', 'r')

text_input = questions_text.read() + '\n-1.'  # -1. is added to denote end of file
question_numbers = re.findall(r'\d+\.', text_input)
list_of_questions = []

for i in range(len(question_numbers) - 1):
    # split text_input on current and next question number to extract the current question
    # splitlines() is performed to obtain each line of the question as a list element
    entire_question = text_input.split(question_numbers[i])[1].strip().split(question_numbers[i + 1])[0].splitlines()

    # tmp stores the question prompt and the options given
    tmp = re.findall(r'\w+', entire_question[0])
    pos = re.findall(r'\w+', entire_question[0]).index('______')
    tmp.pop(pos)
    options = re.findall(r'\w{3,}', " ".join(entire_question[1:]))
    tmp.append(options)

    # the index of blank is used to standardize all questions to the form -> a : b :: c : ______
    if pos == 0:
        tmp[0], tmp[2] = tmp[2], tmp[0]
    elif pos == 1:
        tmp[0], tmp[1], tmp[2] = tmp[1], tmp[2], tmp[0]
    elif pos == 2:
        tmp[0], tmp[1] = tmp[1], tmp[0]

    list_of_questions.append(tmp)
questions_text.close()
