from sklearn.svm import SVC
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_verification_set import *
from randomize_dataset import *
import csv

csv_output = open("test_verification/all_SVM_linear.csv", "w", newline = '')
HeartDiseaseWriter = csv.writer(csv_output)
HeartDiseaseWriter.writerow(["Test", "Test_n", "Test_fs", "Test01", "Test01_n", "Test01_fs",\
  "Verification", "Verification_n", "Verification_fs", "Verification01", "Verification01_n", "Verification01_fs"])

training_time = 10

ta = []
va = []

for i in range(training_time):
    randomize()

    af = pd.read_csv("processed_data5(randomize)/all.csv")
    af_n = pd.read_csv("processed_data5(randomize)/all_n.csv")
    af_fs = pd.read_csv("processed_data5(randomize)/all_fs.csv")
    af01 = pd.read_csv("processed_data5(randomize)/all01.csv")
    af01_n = pd.read_csv("processed_data5(randomize)/all01_n.csv")
    af01_fs = pd.read_csv("processed_data5(randomize)/all01_fs.csv")

    features_train, labels_train, features_test, labels_test, features_verification, labels_verification = make_train_test_verification_set(af)
    features_train_n, labels_train_n, features_test_n, labels_test_n, features_verification_n, labels_verification_n = make_train_test_verification_set(af_n)
    features_train_fs, labels_train_fs, features_test_fs, labels_test_fs, features_verification_fs, labels_verification_fs = make_train_test_verification_set(af_fs)
    features_train01, labels_train01, features_test01, labels_test01, features_verification01, labels_verification01 = make_train_test_verification_set(af01)
    features_train01_n, labels_train01_n, features_test01_n, labels_test01_n, features_verification01_n, labels_verification01_n = make_train_test_verification_set(af01_n)
    features_train01_fs, labels_train01_fs, features_test01_fs, labels_test01_fs, features_verification01_fs, labels_verification01_fs = make_train_test_verification_set(af01_fs)

    # Create classifier
    clf = SVC(kernel = "linear")
    clf_n = SVC(kernel = "linear")
    clf_fs = SVC(kernel = "linear")
    clf01 = SVC(kernel = "linear")
    clf01_n = SVC(kernel = "linear")
    clf01_fs = SVC(kernel = "linear")

    # Fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    clf_n.fit(features_train_n, labels_train_n)
    clf_fs.fit(features_train_fs, labels_train_fs)
    clf01.fit(features_train01, labels_train01)
    clf01_n.fit(features_train01_n, labels_train01_n)
    clf01_fs.fit(features_train01_fs, labels_train01_fs)

    # Use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    pred_n = clf_n.predict(features_test_n)
    pred_fs = clf_fs.predict(features_test_fs)
    pred01 = clf01.predict(features_test01)
    pred01_n = clf01_n.predict(features_test01_n)
    pred01_fs = clf01_fs.predict(features_test01_fs)

    accuracy = SVMAccuracy1(pred, labels_test)
    accuracy_n = SVMAccuracy1(pred_n, labels_test_n)
    accuracy_fs = SVMAccuracy1(pred_fs, labels_test_fs)
    accuracy01 = SVMAccuracy(pred01, labels_test01)
    accuracy01_n = SVMAccuracy(pred01_n, labels_test01_n)
    accuracy01_fs = SVMAccuracy(pred01_fs, labels_test01_fs)

    # Use the trained classifier to predict labels for the test features
    vpred = clf.predict(features_verification)
    vpred_n = clf_n.predict(features_verification_n)
    vpred_fs = clf_fs.predict(features_verification_fs)
    vpred01 = clf01.predict(features_verification01)
    vpred01_n = clf01_n.predict(features_verification01_n)
    vpred01_fs = clf01_fs.predict(features_verification01_fs)

    vaccuracy = SVMAccuracy1(vpred, labels_verification)
    vaccuracy_n = SVMAccuracy1(vpred_n, labels_verification_n)
    vaccuracy_fs = SVMAccuracy1(vpred_fs, labels_verification_fs)
    vaccuracy01 = SVMAccuracy(vpred01, labels_verification01)
    vaccuracy01_n = SVMAccuracy(vpred01_n, labels_verification01_n)
    vaccuracy01_fs = SVMAccuracy(vpred01_fs, labels_verification01_fs)

    ta.append((round(accuracy, 2), round(accuracy_n, 2), round(accuracy_fs, 2),\
      round(accuracy01, 2), round(accuracy01_n, 2), round(accuracy01_fs, 2)))
    va.append((round(vaccuracy, 2), round(vaccuracy_n, 2), round(vaccuracy_fs, 2),\
      round(vaccuracy01, 2), round(vaccuracy01_n, 2), round(vaccuracy01_fs, 2)))

    HeartDiseaseWriter.writerow([ta[i][0], ta[i][1], ta[i][2], ta[i][3], ta[i][4], ta[i][5],\
      va[i][0], va[i][1], va[i][2], va[i][3], va[i][4], va[i][5]])

csv_output.close()

print("Support Vector Machines accuracy: Predict heart disease (All data(50%) -> All data(50%))")
print("-" * 73)
print("Original Data - (0, 1, 2, 3, 4)                   : %.2f %%" % (accuracy*100))
print("-" * 73)
print("Nominal Data - (0, 1, 2, 3, 4)                    : %.2f %%" % (accuracy_n*100))
print("-" * 73)
print("Feature Scaled Data - (0, 1, 2, 3, 4)             : %.2f %%" % (accuracy_fs*100))
print("-" * 73)
print("Original Data - (yes or no)                       : %.2f %%" % (accuracy01*100))
print("-" * 73)
print("Nominal Data - (yes or no)                        : %.2f %%" % (accuracy01_n*100))
print("-" * 73)
print("Feature Scaled Data - (yes or no)                 : %.2f %%" % (accuracy01_fs*100))
