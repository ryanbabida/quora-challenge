from preprocessing import *
from training import *


def main(): 
    train_data = read_file('training.csv')
    test_data = read_file('validation.csv')

    train_data = preprocess_data(train_data)
    test_data = preprocess_data(test_data)

    overlap_scores = get_overlap_scores(train_data)

    for i in range(10):
        print "Sample:", train_data[i][0], "Score:", overlap_scores[i]

    _min, _mid, _max = get_min_mid_max(overlap_scores)

    print "Min:", _min, "Med:", _mid, "Max:", _max


if __name__ == "__main__":
    main()
