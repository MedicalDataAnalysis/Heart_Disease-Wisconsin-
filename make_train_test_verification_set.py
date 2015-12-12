# Train set: 60%
# Test set: 20%
# Verification set: 20%

TRAINING_PERCENT = 0.6
TEST_PERCENT = 0.2

def make_train_test_verification_set(dataFrame):
    total_patients = len(dataFrame)
    total_train_set = int(total_patients * TRAINING_PERCENT)
    total_train_test_set = total_train_set + int(total_patients * TEST_PERCENT)

    features_train = []
    labels_train = []
    features_test = []
    labels_test = []
    features_verification = []
    labels_verification = []

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
    for patient in range(total_train_set, total_train_test_set):
        features = []
        for feature in feature_names:
            if feature == "num":
                labels_test.append(dataFrame[feature][patient])
            else:
                features.append(dataFrame[feature][patient])
        features_test.append(features)

    # Make verification set
    for patient in range(total_train_test_set, total_patients):
        features = []
        for feature in feature_names:
            if feature == "num":
                labels_verification.append(dataFrame[feature][patient])
            else:
                features.append(dataFrame[feature][patient])
        features_verification.append(features)

    return features_train, labels_train, features_test, labels_test, features_verification, labels_verification
