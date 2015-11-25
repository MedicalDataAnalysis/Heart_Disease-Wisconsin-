# Train set: 90%
# Test set: 10%
TRAINING_PERCENT = 0.9

def make_train_test_set(dataFrame):
    total_patients = len(dataFrame)
    total_train_set = int(total_patients * TRAINING_PERCENT)

    features_train = []
    labels_train = []
    features_test = []
    labels_test = []

    feature_names = dataFrame.columns

    # Make training set
    for patient in range(total_train_set):
        features = []
        for feature in feature_names:
            if feature == "num":
                labels_train.append(dataFrame[feature][patient])
            else:
                features.append(dataFrame[feature][patient])
        features_train.append(features)

    # Make test set
    for patient in range(total_train_set, total_patients):
        features = []
        for feature in feature_names:
            if feature == "num":
                labels_test.append(dataFrame[feature][patient])
            else:
                features.append(dataFrame[feature][patient])
        features_test.append(features)

    return features_train, labels_train, features_test, labels_test
