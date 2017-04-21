import csv
from string import maketrans
from collections import defaultdict

# needed for stop words
MAX_FREQUENCY = 10000


def preprocessing(str_in):
    """ creates a translation from special characters to whitespaces
        then applies the translation to the sentences and splits
        to get each word
        @str_in - sentence needed to preprocess
        returns list of words (questions) without 'empty' words
    """
    outtab = "         "
    intab = "?,!.()'\":"
    trantab = maketrans(intab, outtab)

    str_out = str_in.lower()
    str_out = str_out.translate(trantab, '-').split(" ")
    return [word for word in str_out if word != '']


def read_file(filename):
    """ takes in a file and reads it line-by-line
        if element in line is an integer, cast it
        returns the input data
    """
    inp_data = list()
    with open(filename, 'r') as csvfile:
        in_file = csv.reader(csvfile, delimiter=',')
        for row in in_file:
            line = [int(row[0]), int(row[1]), int(row[2]), row[3], row[4], int(row[5])]
            inp_data.append(line)
    return inp_data


def preprocess_data(data):
    """ goes through each line in the input data and preprocesses each question
        returns the transformed data
        @data - raw data read from csv files
    """
    for question_pair in data:
        question_pair[3] = preprocessing(question_pair[3])
        question_pair[4] = preprocessing(question_pair[4])

    return data


def remove_stop_words(data):
    """ remove stop words using a dictionary to keep word frequencies
        afterwards, keep words that do not exceed the MAX_FREQUENCY
        @data - data after preproccessing
    """
    word_freq = defaultdict(int)
    for question_pair in data:
        for word in question_pair[3]:
            word_freq[word] += 1

        for word in question_pair[4]:
            word_freq[word] += 1

    for question_pair in data:
        question_pair[3] = [word for word in question_pair[3] if word_freq[word] <= MAX_FREQUENCY]
        question_pair[4] = [word for word in question_pair[4] if word_freq[word] <= MAX_FREQUENCY]
    return data
