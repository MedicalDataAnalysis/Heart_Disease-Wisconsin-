def make_test_set(dataFrame):
    total_patients = len(dataFrame)
    total_test_set = int(total_patients)

    features_test = []
    labels_test = []

    feature_names = dataFrame.columns

    # Make testing set
    for patient in range(total_test_set):
        features = []
        for feature in feature_names:
            if feature == "num":
                labels_test.append(dataFrame[feature][patient])
            else:
                features.append(dataFrame[feature][patient])
        features_test.append(features)

    return features_test, labels_test
