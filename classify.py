from sklearn.metrics import accuracy_score

def NBAccuracy(pred, labels_test):
    """ compute the accuracy of Naive Bayes classifier """

    # return the accuracy on the test data
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

def SVMAccuracy(pred, labels_test):
    """ compute the accuracy of Support Vector Machines classifier """

    # return the accuracy on the test data
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

def DTAccuracy(pred, labels_test):
    """ compute the accuracy of Support Vector Machines classifier """

    # return the accuracy on the test data
    accuracy = accuracy_score(pred, labels_test)
    return accuracy
