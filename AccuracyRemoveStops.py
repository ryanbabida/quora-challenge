import sys

from data_processing import *


def accuracy_remove_stops():
    if len(sys.argv) != 3:
        print("Not correct amount of args.")
        quit()

    # makes sure arg is a number
    try:
        float(sys.argv[2])
    except:
        raise TypeError

    # checks if threshold is valid
    if float(sys.argv[2]) > 1.0:
        raise ValueError

    # process data and remove the stop words
    data = read_file(sys.argv[1])
    data = preprocess_data(data)
    data = remove_stop_words(data)

    overlap_scores = get_overlap_scores(data)

    threshold = float(sys.argv[2])

    # uses overlap scores to calculate accuracy
    accuracy = get_accuracy(overlap_scores, data, threshold)
    print("%.4f" % accuracy)


if __name__ == "__main__":
    accuracy_remove_stops()
