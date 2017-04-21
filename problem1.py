import sys

from data_processing import *


def main():
    if len(sys.argv) != 3:
        print "Not correct amount of args."
        quit()

    train_data = read_file('training.csv')
    train_data = preprocess_data(train_data)

    test_data = read_file('validation.csv')
    test_data = preprocess_data(test_data)


if __name__ == "__main__":
    main()
