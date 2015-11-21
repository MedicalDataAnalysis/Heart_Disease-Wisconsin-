def NBAccuracy(pred, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """

    # return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    return accuracy
