

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
    return scores[0], scores[len(scores) / 2], scores[len(scores) - 1]


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



