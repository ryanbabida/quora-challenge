import csv
from collections import defaultdict

# needed for stop words
MAX_FREQUENCY = 10000


def preprocess(str_in):
    """ creates a translation from special characters to whitespaces
        then applies the translation to the sentences and splits
        to get each word
        @str_in - sentence needed to preprocess
        returns list of words (questions) without 'empty' words
    """
    outtab = "         "
    intab = "?,!.()'\":"
    trantab = str.maketrans(intab, outtab)

    str_out = str_in.lower()
    str_out = str_out.translate(trantab)
    str_out = str_out.replace('-', '')
    str_out = str_out.split(" ")
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
        question_pair[3] = preprocess(question_pair[3])
        question_pair[4] = preprocess(question_pair[4])

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


def get_overlap_scores(data):
    """ calcultes overlapp scores for each question pair
        @data - the data that has been preprocessed
        @scores - calculated scores
    """
    scores = list()
    for question_pair in data:
        overlap_score = 0.0

        # if there are now words in the question, overlap score is 0
        if len(question_pair[3]) + len(question_pair[4]) == 0:
            scores.append(overlap_score)
            continue

        # iterate through both questions sepaerately
        for word in question_pair[3]:
            if word in question_pair[4] and word is not '':
                overlap_score += 1

        for word in question_pair[4]:
            if word in question_pair[3] and word is not '':
                overlap_score += 1

        overlap_score = overlap_score / (len(question_pair[3]) + len(question_pair[4]))
        scores.append(overlap_score)

    return scores


def get_min_mid_max(scores):
    """ gets the min, median, and max overlapping scores
        sorts the scores and gets the three values
        @scores - overlap scores from the data
    """
    scores = sorted(scores)
    return scores[0], scores[int(len(scores) / 2)], scores[len(scores) - 1]


def get_accuracy(scores, data, threshold):
    """ check based on threshold, assign a 0 or 1 with the scores
        compare with actual data from csv and if they are the same
        increase the correct count
        @scores - overlap scores 
        @data - need the data to get the correct target values for comparison
        @threshold - used to classify scores as 0 or 1
        returns the percentage of correct predictions
    """
    correct = 0.0
    for i in range(len(scores)):
        if ((float(scores[i]) - threshold >= 0 and data[i][5] == 1) or
                (float(scores[i]) - threshold <= 0 and data[i][5] == 0)):
            correct += 1

    return correct / len(scores)
