import sys

from data_processing import *


def main():
    if len(sys.argv) != 2:
        print "Not correct amount of args."
        quit()

    data = read_file(sys.argv[1])
    data = preprocess_data(data)

    overlap_scores = get_overlap_scores(data)

    for i in range(10):
        print "Score", i, ": ", "%.4f" % overlap_scores[i]

    _min, _mid, _max = get_min_mid_max(overlap_scores)

    print "Min:", _min
    print "Med:", _mid
    print "Max:", _max


if __name__ == "__main__":
    main()
