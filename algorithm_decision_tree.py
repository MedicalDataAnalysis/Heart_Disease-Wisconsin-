from sklearn import tree
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *
df = pd.read_csv("processed_data2(no_missing_value)/cleveland.csv")
df_n = pd.read_csv("processed_data4(nominal)/cleveland_n.csv")
df01 = pd.read_csv("processed_data2(no_missing_value)/cleveland01.csv")
df01_n = pd.read_csv("processed_data4(nominal)/cleveland01_n.csv")

features_train, labels_train, features_test, labels_test = make_train_test_set(df)
features_train_n, labels_train_n, features_test_n, labels_test_n = make_train_test_set(df_n)
features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(df01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(df01_n)

# Create classifier
clf2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf10 = tree.DecisionTreeClassifier(min_samples_split=10)
clf2_n = tree.DecisionTreeClassifier(min_samples_split=2)
clf10_n = tree.DecisionTreeClassifier(min_samples_split=10)
clf01_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf01_10 = tree.DecisionTreeClassifier(min_samples_split=10)
clf01_2_n = tree.DecisionTreeClassifier(min_samples_split=2)
clf01_10_n = tree.DecisionTreeClassifier(min_samples_split=10)

#
clf01_5_n = tree.DecisionTreeClassifier(min_samples_split=5)
clf01_15_n = tree.DecisionTreeClassifier(min_samples_split=15)
clf01_20_n = tree.DecisionTreeClassifier(min_samples_split=20)

# Fit the classifier on the training features and labels
clf2 = clf2.fit(features_train, labels_train)
clf10 = clf10.fit(features_train, labels_train)
clf2_n = clf2_n.fit(features_train_n, labels_train_n)
clf10_n = clf10_n.fit(features_train_n, labels_train_n)
clf01_2 = clf01_2.fit(features_train01, labels_train01)
clf01_10 = clf01_10.fit(features_train01, labels_train01)
clf01_2_n = clf01_2_n.fit(features_train01_n, labels_train01_n)
clf01_10_n = clf01_10_n.fit(features_train01_n, labels_train01_n)

#
clf01_5_n = clf01_5_n.fit(features_train01_n, labels_train01_n)
clf01_15_n = clf01_15_n.fit(features_train01_n, labels_train01_n)
clf01_20_n = clf01_20_n.fit(features_train01_n, labels_train01_n)

# Use the trained classifier to predict labels for the test features
pred2 = clf2.predict(features_test)
pred10 = clf10.predict(features_test)
pred2_n = clf2_n.predict(features_test_n)
pred10_n = clf10_n.predict(features_test_n)
pred01_2 = clf01_2.predict(features_test01)
pred01_10 = clf01_10.predict(features_test01)
pred01_2_n = clf01_2_n.predict(features_test01_n)
pred01_10_n = clf01_10_n.predict(features_test01_n)

#
pred01_5_n = clf01_5_n.predict(features_test01_n)
pred01_15_n = clf01_15_n.predict(features_test01_n)
pred01_20_n = clf01_20_n.predict(features_test01_n)

accuracy2 = DTAccuracy(pred2, labels_test)
accuracy10 = DTAccuracy(pred10, labels_test)
accuracy2_n = DTAccuracy(pred2_n, labels_test_n)
accuracy10_n = DTAccuracy(pred10_n, labels_test_n)
accuracy01_2 = DTAccuracy(pred01_2, labels_test01)
accuracy01_10 = DTAccuracy(pred01_10, labels_test01)
accuracy01_2_n = DTAccuracy(pred01_2_n, labels_test01_n)
accuracy01_10_n = DTAccuracy(pred01_10_n, labels_test01_n)

#
accuracy01_5_n = DTAccuracy(pred01_5_n, labels_test01_n)
accuracy01_15_n = DTAccuracy(pred01_15_n, labels_test01_n)
accuracy01_20_n = DTAccuracy(pred01_20_n, labels_test01_n)

print("Decision Tree accuracy: Predict heart disease")
print("-" * 73)
print("Original Data - distinguish from 0 to 4 (min_samples_split=2)  : %.2f %%" % (accuracy2*100))
print("Original Data - distinguish from 0 to 4 (min_samples_split=10) : %.2f %%" % (accuracy10*100))
print("Original Data - yes or no (min_samples_split=2)                : %.2f %%" % (accuracy01_2*100))
print("Original Data - yes or no (min_samples_split=10)               : %.2f %%" % (accuracy01_10*100))
print("-" * 73)
print("Nominal Data - distinguish from 0 to 4 (min_samples_split=2)  : %.2f %%" % (accuracy2_n*100))
print("Nominal Data - distinguish from 0 to 4 (min_samples_split=10) : %.2f %%" % (accuracy10_n*100))
print("Nominal Data - yes or no (min_samples_split=2)  : %.2f %%" % (accuracy01_2_n*100))
print("Nominal Data - yes or no (min_samples_split=10) : %.2f %%" % (accuracy01_10_n*100))
print("-" * 73)
print("Nominal Data - yes or no (min_samples_split=5) : %.2f %%" % (accuracy01_5_n*100))
print("Nominal Data - yes or no (min_samples_split=15) : %.2f %%" % (accuracy01_15_n*100))
print("Nominal Data - yes or no (min_samples_split=20) : %.2f %%" % (accuracy01_20_n*100))
