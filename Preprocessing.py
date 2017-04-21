import sys

from data_processing import *


def preprocessing():

    # process both train and test data
    train_data = read_file('training.csv')
    train_data = preprocess_data(train_data)

    test_data = read_file('validation.csv')
    test_data = preprocess_data(test_data)


if __name__ == "__main__":
    preprocessing()
