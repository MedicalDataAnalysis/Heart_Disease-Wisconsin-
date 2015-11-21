# Train set: 90%
# Test set: 10%
def make_train_test_set(dataFrame):
    total_patients = len(dataFrame)
    total_train_set = int(total_patients * 0.9)

    features_train = []
    labels_train = []
    features_test = []
    labels_test = []
    # Make training set
    for patient in range(total_train_set):
        features = []
        features.append(dataFrame["age"][patient])
        features.append(dataFrame["sex"][patient])
        features.append(dataFrame["cp"][patient])
        features.append(dataFrame["trestbps"][patient])
        features.append(dataFrame["chol"][patient])
        features.append(dataFrame["fbs"][patient])
        features.append(dataFrame["restecg"][patient])
        features.append(dataFrame["thalach"][patient])
        features.append(dataFrame["exang"][patient])
        features.append(dataFrame["oldpeak"][patient])
        features.append(dataFrame["slope"][patient])
        features.append(dataFrame["ca"][patient])
        features.append(dataFrame["thal"][patient])

        features_train.append(features)
        labels_train.append(dataFrame["num"][patient])

    # Make test set
    for patient in range(total_train_set, total_patients):
        features = []
        features.append(dataFrame["age"][patient])
        features.append(dataFrame["sex"][patient])
        features.append(dataFrame["cp"][patient])
        features.append(dataFrame["trestbps"][patient])
        features.append(dataFrame["chol"][patient])
        features.append(dataFrame["fbs"][patient])
        features.append(dataFrame["restecg"][patient])
        features.append(dataFrame["thalach"][patient])
        features.append(dataFrame["exang"][patient])
        features.append(dataFrame["oldpeak"][patient])
        features.append(dataFrame["slope"][patient])
        features.append(dataFrame["ca"][patient])
        features.append(dataFrame["thal"][patient])

        features_test.append(features)
        labels_test.append(dataFrame["num"][patient])

    return features_train, labels_train, features_test, labels_test
