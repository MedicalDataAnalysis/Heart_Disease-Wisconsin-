def make_training_set(dataFrame):
    total_patients = len(dataFrame)
    total_train_set = int(total_patients)

    features_train = []
    labels_train = []

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

    return features_train, labels_train
