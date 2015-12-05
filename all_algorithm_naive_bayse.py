### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *
from make_training_set import *
from make_test_set import *

af01 = pd.read_csv("processed_data2(no_missing_value)/all01.csv")
af01_n = pd.read_csv("processed_data4(nominal)/all01_n.csv")

features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(af01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(af01_n)

# features_train01, labels_train01 = make_training_set(df01)
# features_train01_n, labels_train01_n = make_training_set(df01_n)
# features_test01, labels_test01 = make_test_set(af01)
# features_test01_n, labels_test01_n = make_test_set(af01_n)

# Create classifier
clf01 = GaussianNB()
clf01_n = GaussianNB()

# Fit the classifier on the training features and labels
clf01.fit(features_train01, labels_train01)
clf01_n.fit(features_train01_n, labels_train01_n)

# Use the trained classifier to predict labels for the test features
pred01 = clf01.predict(features_test01)
pred01_n = clf01_n.predict(features_test01_n)

accuracy01 = NBAccuracy(pred01, labels_test01)
accuracy01_n = NBAccuracy(pred01_n, labels_test01_n)

print("Naive Bayse accuracy: Predict heart disease (All data(50%) -> All data(50%))")
print("-" * 73)
print("Original Data - (yes or no)                        : %.2f %%" % (accuracy01*100))
print("-" * 73)
print("Nominal Data - (yes or no)                        : %.2f %%" % (accuracy01_n*100))