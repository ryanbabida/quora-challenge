import sys

from data_processing import *


def best_threshold():
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    best_thr = 0
    best_accuracy = 0

    # process data
    data = read_file('training.csv')
    data = preprocess_data(data)

    overlap_scores = get_overlap_scores(data)

    for thr in thresholds:
        # makes sure arg is a number
        try:
            float(thr)
        except:
            raise TypeError

        # checks if threshold is valid
        if float(thr) > 1.0:
            raise ValueError

        # uses overlap scores to get accuracy
        accuracy = get_accuracy(overlap_scores, data, thr)

        if best_accuracy < accuracy:
            best_accuracy = accuracy
            best_thr = thr

    print("Best Threshold: ", best_thr, "Best Accuracy: ", "%.4f" % best_accuracy)


if __name__ == "__main__":
    best_threshold()
