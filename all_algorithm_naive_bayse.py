### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_verification_set import *
from randomize_dataset import *
import csv

csv_output = open("test_verification/all_naive_bayse.csv", "w", newline = '')
HeartDiseaseWriter = csv.writer(csv_output)
HeartDiseaseWriter.writerow(["Test", "Test_n", "Test01", "Test01_n", \
  "Verification", "Verification_n", "Verification01", "Verification01_n"])

training_time = 10

ta = []
va = []

for i in range(training_time):
    randomize()

    af = pd.read_csv("processed_data5(randomize)/all.csv")
    af_n = pd.read_csv("processed_data5(randomize)/all_n.csv")
    af01 = pd.read_csv("processed_data5(randomize)/all01.csv")
    af01_n = pd.read_csv("processed_data5(randomize)/all01_n.csv")

    features_train, labels_train, features_test, labels_test, features_verification, labels_verification = make_train_test_verification_set(af)
    features_train_n, labels_train_n, features_test_n, labels_test_n, features_verification_n, labels_verification_n = make_train_test_verification_set(af_n)
    features_train01, labels_train01, features_test01, labels_test01, features_verification01, labels_verification01 = make_train_test_verification_set(af01)
    features_train01_n, labels_train01_n, features_test01_n, labels_test01_n, features_verification01_n, labels_verification01_n = make_train_test_verification_set(af01_n)

    # Create classifier
    clf = GaussianNB()
    clf_n = GaussianNB()
    clf01 = GaussianNB()
    clf01_n = GaussianNB()

    # Fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    clf_n.fit(features_train_n, labels_train_n)
    clf01.fit(features_train01, labels_train01)
    clf01_n.fit(features_train01_n, labels_train01_n)

    # Use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    pred_n = clf_n.predict(features_test_n)
    pred01 = clf01.predict(features_test01)
    pred01_n = clf01_n.predict(features_test01_n)

    accuracy = NBAccuracy1(pred, labels_test)
    accuracy_n = NBAccuracy1(pred_n, labels_test_n)
    accuracy01 = NBAccuracy(pred01, labels_test01)
    accuracy01_n = NBAccuracy(pred01_n, labels_test01_n)

    # Use the trained classifier to predict labels for the verification features
    vpred = clf.predict(features_verification)
    vpred_n = clf_n.predict(features_verification_n)
    vpred01 = clf01.predict(features_verification01)
    vpred01_n = clf01_n.predict(features_verification01_n)

    vaccuracy = NBAccuracy1(vpred, labels_verification)
    vaccuracy_n = NBAccuracy1(vpred_n, labels_verification_n)
    vaccuracy01 = NBAccuracy(vpred01, labels_verification01)
    vaccuracy01_n = NBAccuracy(vpred01_n, labels_verification01_n)

    ta.append((round(accuracy, 2), round(accuracy_n, 2), round(accuracy01, 2), round(accuracy01_n, 2)))
    va.append((round(vaccuracy, 2), round(vaccuracy_n, 2), round(vaccuracy01, 2), round(vaccuracy01_n, 2)))

    HeartDiseaseWriter.writerow([ta[i][0], ta[i][1], ta[i][2], ta[i][3], va[i][0], va[i][1], va[i][2], va[i][3]])

csv_output.close()

print("Naive Bayse accuracy: Predict heart disease (Training(60%) -> Test(20%))")
print("-" * 73)
print("Original Data - (yes or no)                       : %.2f %%" % (accuracy01*100))
print("-" * 73)
print("Nominal Data - (yes or no)                        : %.2f %%" % (accuracy01_n*100))
print("-" * 73)
print("Original Data - (0, 1, 2, 3, 4)                   : %.2f %%" % (accuracy*100))
print("-" * 73)
print("Nominal Data - (0, 1, 2, 3, 4)                    : %.2f %%" % (accuracy_n*100))

print("Verification Set accuracy: Predict heart disease (Training(60%) -> Verification(20%))")
print("-" * 73)
print("Original Data - (yes or no)                       : %.2f %%" % (vaccuracy01*100))
print("-" * 73)
print("Nominal Data - (yes or no)                        : %.2f %%" % (vaccuracy01_n*100))
print("-" * 73)
print("Original Data - (0, 1, 2, 3, 4)                   : %.2f %%" % (vaccuracy*100))
print("-" * 73)
print("Nominal Data - (0, 1, 2, 3, 4)                    : %.2f %%" % (vaccuracy_n*100))
