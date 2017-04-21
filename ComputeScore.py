import sys

from data_processing import *


def compute_scores():
    if len(sys.argv) != 2:
        print("Not correct amount of args.")
        quit()

    # process data
    data = read_file(sys.argv[1])
    data = preprocess_data(data)

    overlap_scores = get_overlap_scores(data)

    for i in range(10):
        print("%.4f" % overlap_scores[i])

    _min, _mid, _max = get_min_mid_max(overlap_scores)

    # Not required output format based on assignment
    # print("Min:", _min)
    # print("Med:", _mid)
    # print("Max:", _max)


if __name__ == "__main__":
    compute_scores()
