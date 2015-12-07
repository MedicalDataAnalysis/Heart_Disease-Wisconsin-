from sklearn.svm import SVC
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

af = pd.read_csv("processed_data2(no_missing_value)/all.csv")
af_n = pd.read_csv("processed_data4(nominal)/all_n.csv")
af_fs = pd.read_csv("processed_data3(feature_scaled)/all_fs.csv")
af01 = pd.read_csv("processed_data2(no_missing_value)/all01.csv")
af01_n = pd.read_csv("processed_data4(nominal)/all01_n.csv")
af01_fs = pd.read_csv("processed_data3(feature_scaled)/all01_fs.csv")

features_train, labels_train, features_test, labels_test = make_train_test_set(af)
features_train_n, labels_train_n, features_test_n, labels_test_n = make_train_test_set(af_n)
features_train_fs, labels_train_fs, features_test_fs, labels_test_fs = make_train_test_set(af_fs)
features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(af01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(af01_n)
features_train01_fs, labels_train01_fs, features_test01_fs, labels_test01_fs = make_train_test_set(af01_fs)

# Create classifier
clf = SVC(kernel = "rbf")
clf_n = SVC(kernel = "rbf")
clf_fs = SVC(kernel = "rbf")
clf01 = SVC(kernel = "rbf")
clf01_n = SVC(kernel = "rbf")
clf01_fs = SVC(kernel = "rbf")

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

accuracy = SVMAccuracy(pred, labels_test)
accuracy_n = SVMAccuracy(pred_n, labels_test_n)
accuracy_fs = SVMAccuracy(pred_fs, labels_test_fs)
accuracy01 = SVMAccuracy(pred01, labels_test01)
accuracy01_n = SVMAccuracy(pred01_n, labels_test01_n)
accuracy01_fs = SVMAccuracy(pred01_fs, labels_test01_fs)

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
