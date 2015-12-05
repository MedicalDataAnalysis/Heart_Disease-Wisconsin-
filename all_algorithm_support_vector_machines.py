from sklearn.svm import SVC
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

af01 = pd.read_csv("processed_data2(no_missing_value)/all01.csv")
af01_n = pd.read_csv("processed_data4(nominal)/all01_n.csv")
af01_fs = pd.read_csv("processed_data3(feature_scaled)/all01_fs.csv")

features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(af01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(af01_n)
features_train01_fs, labels_train01_fs, features_test01_fs, labels_test01_fs = make_train_test_set(af01_fs)

# Create classifier
clf01 = SVC()
clf01_n = SVC()
clf01_fs = SVC()

# Fit the classifier on the training features and labels
clf01.fit(features_train01, labels_train01)
clf01_n.fit(features_train01_n, labels_train01_n)
clf01_fs.fit(features_train01_fs, labels_train01_fs)

# Use the trained classifier to predict labels for the test features
pred01 = clf01.predict(features_test01)
pred01_n = clf01_n.predict(features_test01_n)
pred01_fs = clf01_fs.predict(features_test01_fs)

accuracy01 = SVMAccuracy(pred01, labels_test01)
accuracy01_n = SVMAccuracy(pred01_n, labels_test01_n)
accuracy01_fs = SVMAccuracy(pred01_fs, labels_test01_fs)

print("Support Vector Machines accuracy: Predict heart disease (All data(50%) -> All data(50%))")
print("-" * 73)
print("Original Data - (yes or no)                       : %.2f %%" % (accuracy01*100))
print("-" * 73)
print("Nominal Data - (yes or no)                        : %.2f %%" % (accuracy01_n*100))
print("-" * 73)
print("Feature Scaled Data - (yes or no)                 : %.2f %%" % (accuracy01_fs*100))
