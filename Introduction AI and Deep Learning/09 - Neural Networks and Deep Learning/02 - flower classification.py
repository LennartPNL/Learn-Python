import os
import collections
import itertools

import numpy as np
import pandas as pd
import tensorflow as tf

from six.moves import urllib

print(np.__version__)
print(pd.__version__)
print(tf.__version__)

# The Iris dataset is also available here: https://archive.ics.uci.edu/ml/datasets/iris

URL_TRAIN_PATH = "http://download.tensorflow.org/data/iris_training.csv"
URL_TEST_PATH = "http://download.tensorflow.org/data/iris_test.csv"

DOWNLOADED_FILENAME_TRAIN = "iris_training.csv"
DOWNLOADED_FILENAME_TEST = "iris_test.csv"


def download_data():
    if not os.path.exists(DOWNLOADED_FILENAME_TRAIN):
        filename, _ = urllib.request.urlretrieve(URL_TRAIN_PATH, DOWNLOADED_FILENAME_TRAIN)

    print('Found and verified file from this path: ', URL_TRAIN_PATH)
    print('Downloaded file: ', DOWNLOADED_FILENAME_TRAIN)

    if not os.path.exists(DOWNLOADED_FILENAME_TEST):
        filename, _ = urllib.request.urlretrieve(URL_TEST_PATH, DOWNLOADED_FILENAME_TEST)

    print('Found and verified file from this path: ', URL_TEST_PATH)
    print('Downloaded file: ', DOWNLOADED_FILENAME_TEST)


download_data()

FEATURE_NAMES = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm'
]


def parse_csv(line):
    parsed_line = tf.decode_csv(line, [[0.], [0.], [0.], [0.], [0]])

    # Labels are 0, 1 or 2
    labels = parsed_line[-1:]

    del parsed_line[-1]

    features = dict(zip(FEATURE_NAMES, parsed_line))

    return features, labels


def get_features_labels(filename, shuffle=False, repeat_count=1):
    dataset = (tf.data.TextLineDataset(filename).skip(1).map(parse_csv))

    if shuffle:
        dataset = dataset.shuffle(buffer_size=256)

    dataset = dataset.repeat(repeat_count)
    dataset = dataset.batch(32)

    iterator = dataset.make_one_shot_iterator()

    batch_features, batch_labels = iterator.get_next()

    return batch_features, batch_labels


batch_features, batch_labels = get_features_labels(DOWNLOADED_FILENAME_TRAIN)

batch_features

batch_labels

feature_columns = [tf.feature_column.numeric_column(k) for k in FEATURE_NAMES]

classifier_model = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[16, 12, 16],
    n_classes=3)

classifier_model.train(
    input_fn=lambda: get_features_labels(DOWNLOADED_FILENAME_TRAIN, shuffle=True, repeat_count=20))

results = classifier_model.evaluate(
    input_fn=lambda: get_features_labels(DOWNLOADED_FILENAME_TEST, shuffle=False, repeat_count=4))

for key in sorted(results):
    print("%s: %s" % (key, results[key]))

predict_results = classifier_model.predict(
    input_fn=lambda: get_features_labels(DOWNLOADED_FILENAME_TEST, shuffle=False))

predictions = [prediction["class_ids"][0] for idx, prediction in enumerate(predict_results)]

df = pd.read_csv(DOWNLOADED_FILENAME_TEST, names=FEATURE_NAMES + ['Labels'], skiprows=1)

df['PredictedLabels'] = predictions

df
