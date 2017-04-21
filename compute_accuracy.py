import sys

from data_processing import *


def main():
    if len(sys.argv) != 3:
        print "Not correct amount of args."
        quit()

    data = read_file(sys.argv[1])
    # test_data = read_file('validation.csv')

    data = preprocess_data(data)

    # data = remove_stop_words(data)
    # test_data = preprocess_data(test_data)

    overlap_scores = get_overlap_scores(data)

    # for i in range(10):
    #     print "Sample:", data[i][0], "Score:", overlap_scores[i]

    # _min, _mid, _max = get_min_mid_max(overlap_scores)

    # print "Min:", _min, "Med:", _mid, "Max:", _max

    try:
        float(sys.argv[2])
    except:
        raise TypeError

    threshold = float(sys.argv[2])

    res = get_accuracy(overlap_scores, data, threshold)
    print res


if __name__ == "__main__":
    main()
