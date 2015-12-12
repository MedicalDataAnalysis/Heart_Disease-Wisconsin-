from sklearn.metrics import accuracy_score

wei = 0.8
def NBAccuracy(pred, labels_test):
    """ compute the accuracy of Naive Bayes classifier """
    # return the accuracy on the test data
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

def NBAccuracy1(pred, labels_test):
    """ compute the accuracy of Naive Bayes classifier """
    score=0.0
    error=0
    # return the accuracy on the test data
    for i in range(len(pred)):
        error=pred[i]-labels_test[i]
        if pred[i]==0|pred[i]==1:
            if abs(error)==0:
                score=score+1
            elif labels_test[i]==1:
                if pred[i]==2:
                    score=score+wei
            elif labels_test[i]==2:
                if pred[i]==1:
                    score=score+wei
                if pred[i]==3:
                    score=score+wei

            else:
                score=score

        else:
            if abs(error)==0:
                score=score+1
            if abs(error)==1:
                score=score+wei
            if abs(error)==2:
                score=score+0
            if abs(error)==3:
                score=score+0
            if abs(error)==4:
                score=score

    return score/len(pred)

def SVMAccuracy(pred, labels_test):
    """ compute the accuracy of Support Vector Machines classifier """

    # return the accuracy on the test data
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

def SVMAccuracy1(pred, labels_test):
    """ compute the accuracy of Naive Bayes classifier """
    score=0.0
    error=0
    # return the accuracy on the test data
    for i in range(len(pred)):
        error=pred[i]-labels_test[i]
        if pred[i]==0|pred[i]==1:
            if abs(error)==0:
                score=score+1
            elif labels_test[i]==1:
                if pred[i]==2:
                    score=score+wei
            elif labels_test[i]==2:
                if pred[i]==1:
                    score=score+wei
                if pred[i]==3:
                    score=score+wei

            else:
                score=score

        else:
            if abs(error)==0:
                score=score+1
            if abs(error)==1:
                score=score+wei
            if abs(error)==2:
                score=score+0
            if abs(error)==3:
                score=score+0
            if abs(error)==4:
                score=score

    return score/len(pred)

# Decision Tree
def DTAccuracy(pred, labels_test):
    """ compute the accuracy of Support Vector Machines classifier """

    # return the accuracy on the test data
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

def DTAccuracy1(pred, labels_test):
    """ compute the accuracy of Naive Bayes classifier """
    score=0.0
    error=0
    # return the accuracy on the test data
    for i in range(len(pred)):
        error=pred[i]-labels_test[i]
        if pred[i]==0|pred[i]==1:
            if abs(error)==0:
                score=score+1
            elif labels_test[i]==1:
                if pred[i]==2:
                    score=score+wei
            elif labels_test[i]==2:
                if pred[i]==1:
                    score=score+wei
                if pred[i]==3:
                    score=score+wei

            else:
                score=score

        else:
            if abs(error)==0:
                score=score+1
            if abs(error)==1:
                score=score+wei
            if abs(error)==2:
                score=score+0
            if abs(error)==3:
                score=score+0
            if abs(error)==4:
                score=score

    return score/len(pred)
