from sklearn import tree
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

af01 = pd.read_csv("processed_data2(no_missing_value)/all01.csv")
af01_n = pd.read_csv("processed_data4(nominal)/all01_n.csv")

features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(af01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(af01_n)

# Create classifier
clf01_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf01_5 = tree.DecisionTreeClassifier(min_samples_split=5)
clf01_10 = tree.DecisionTreeClassifier(min_samples_split=10)
clf01_15 = tree.DecisionTreeClassifier(min_samples_split=15)
clf01_20 = tree.DecisionTreeClassifier(min_samples_split=20)
clf01_2_n = tree.DecisionTreeClassifier(min_samples_split=2)
clf01_10_n = tree.DecisionTreeClassifier(min_samples_split=10)

# Fit the classifier on the training features and labels
clf01_2 = clf01_2.fit(features_train01, labels_train01)
clf01_5 = clf01_5.fit(features_train01, labels_train01)
clf01_10 = clf01_10.fit(features_train01, labels_train01)
clf01_15 = clf01_15.fit(features_train01, labels_train01)
clf01_20 = clf01_20.fit(features_train01, labels_train01)
clf01_2_n = clf01_2_n.fit(features_train01_n, labels_train01_n)
clf01_10_n = clf01_10_n.fit(features_train01_n, labels_train01_n)

# Use the trained classifier to predict labels for the test features
pred01_2 = clf01_2.predict(features_test01)
pred01_5 = clf01_5.predict(features_test01)
pred01_10 = clf01_10.predict(features_test01)
pred01_15 = clf01_15.predict(features_test01)
pred01_20 = clf01_20.predict(features_test01)
pred01_2_n = clf01_2_n.predict(features_test01_n)
pred01_10_n = clf01_10_n.predict(features_test01_n)

accuracy01_2 = DTAccuracy(pred01_2, labels_test01)
accuracy01_5 = DTAccuracy(pred01_5, labels_test01)
accuracy01_10 = DTAccuracy(pred01_10, labels_test01)
accuracy01_15 = DTAccuracy(pred01_15, labels_test01)
accuracy01_20 = DTAccuracy(pred01_20, labels_test01)
accuracy01_2_n = DTAccuracy(pred01_2_n, labels_test01_n)
accuracy01_10_n = DTAccuracy(pred01_10_n, labels_test01_n)

print("Decision Tree accuracy: Predict heart disease (All data(50%) -> All data(50%))")
print("-" * 73)
print("Original Data - yes or no (min_samples_split=2) : %.2f %%" % (accuracy01_2*100))
print("Original Data - yes or no (min_samples_split=5) : %.2f %%" % (accuracy01_5*100))
print("Original Data - yes or no (min_samples_split=10): %.2f %%" % (accuracy01_10*100))
print("Original Data - yes or no (min_samples_split=15) : %.2f %%" % (accuracy01_15*100))
print("Original Data - yes or no (min_samples_split=20) : %.2f %%" % (accuracy01_20*100))
print("-" * 73)
print("Nominal Data - yes or no (min_samples_split=2)  : %.2f %%" % (accuracy01_2_n*100))
print("Nominal Data - yes or no (min_samples_split=10) : %.2f %%" % (accuracy01_10_n*100))
print("-" * 73)
