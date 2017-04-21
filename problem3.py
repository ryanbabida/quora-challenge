import sys

from data_processing import *


def main():
    if len(sys.argv) != 3:
        print "Not correct amount of args."
        quit()

    try:
        float(sys.argv[2])
    except:
        raise TypeError

    if sys.argv[2] > 1.0:
        raise ValueError

    data = read_file(sys.argv[1])
    data = preprocess_data(data)

    overlap_scores = get_overlap_scores(data)

    threshold = float(sys.argv[2])

    accuracy = get_accuracy(overlap_scores, data, threshold)
    print accuracy


if __name__ == "__main__":
    main()
