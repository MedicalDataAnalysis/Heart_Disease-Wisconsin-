from sklearn import tree
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

af = pd.read_csv("processed_data2(no_missing_value)/all.csv")
af_n = pd.read_csv("processed_data4(nominal)/all_n.csv")
af01 = pd.read_csv("processed_data2(no_missing_value)/all01.csv")
af01_n = pd.read_csv("processed_data4(nominal)/all01_n.csv")

features_train, labels_train, features_test, labels_test = make_train_test_set(af)
features_train_n, labels_train_n, features_test_n, labels_test_n = make_train_test_set(af_n)
features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(af01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(af01_n)

# Create classifier
clf_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf_5 = tree.DecisionTreeClassifier(min_samples_split=5)
clf_10 = tree.DecisionTreeClassifier(min_samples_split=10)
clf_2_n = tree.DecisionTreeClassifier(min_samples_split=2)
clf_5_n = tree.DecisionTreeClassifier(min_samples_split=5)
clf_10_n = tree.DecisionTreeClassifier(min_samples_split=10)
clf01_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf01_5 = tree.DecisionTreeClassifier(min_samples_split=5)
clf01_10 = tree.DecisionTreeClassifier(min_samples_split=10)
clf01_2_n = tree.DecisionTreeClassifier(min_samples_split=2)
clf01_5_n = tree.DecisionTreeClassifier(min_samples_split=5)
clf01_10_n = tree.DecisionTreeClassifier(min_samples_split=10)

clf_max2 = tree.DecisionTreeClassifier(max_depth=2)
clf_max3 = tree.DecisionTreeClassifier(max_depth=3)
clf_max4 = tree.DecisionTreeClassifier(max_depth=4)
clf_max2_n = tree.DecisionTreeClassifier(max_depth=2)
clf_max3_n = tree.DecisionTreeClassifier(max_depth=3)
clf_max4_n = tree.DecisionTreeClassifier(max_depth=4)
clf01_max2 = tree.DecisionTreeClassifier(max_depth=2)
clf01_max3 = tree.DecisionTreeClassifier(max_depth=3)
clf01_max4 = tree.DecisionTreeClassifier(max_depth=4)
clf01_max2_n = tree.DecisionTreeClassifier(max_depth=2)
clf01_max3_n = tree.DecisionTreeClassifier(max_depth=3)
clf01_max4_n = tree.DecisionTreeClassifier(max_depth=4)

# Fit the classifier on the training features and labels
clf_2 = clf_2.fit(features_train, labels_train)
clf_5 = clf_5.fit(features_train, labels_train)
clf_10 = clf_10.fit(features_train, labels_train)
clf_2_n = clf_2_n.fit(features_train_n, labels_train_n)
clf_5_n = clf_5_n.fit(features_train_n, labels_train_n)
clf_10_n = clf_10_n.fit(features_train_n, labels_train_n)
clf01_2 = clf01_2.fit(features_train01, labels_train01)
clf01_5 = clf01_5.fit(features_train01, labels_train01)
clf01_10 = clf01_10.fit(features_train01, labels_train01)
clf01_2_n = clf01_2_n.fit(features_train01_n, labels_train01_n)
clf01_5_n = clf01_5_n.fit(features_train01_n, labels_train01_n)
clf01_10_n = clf01_10_n.fit(features_train01_n, labels_train01_n)

clf_max2 = clf_max2.fit(features_train, labels_train)
clf_max3 = clf_max3.fit(features_train, labels_train)
clf_max4 = clf_max4.fit(features_train, labels_train)
clf_max2_n = clf_max2_n.fit(features_train_n, labels_train_n)
clf_max3_n = clf_max3_n.fit(features_train_n, labels_train_n)
clf_max4_n = clf_max4_n.fit(features_train_n, labels_train_n)
clf01_max2 = clf01_max2.fit(features_train01, labels_train01)
clf01_max3 = clf01_max3.fit(features_train01, labels_train01)
clf01_max4 = clf01_max4.fit(features_train01, labels_train01)
clf01_max2_n = clf01_max2_n.fit(features_train01_n, labels_train01_n)
clf01_max3_n = clf01_max3_n.fit(features_train01_n, labels_train01_n)
clf01_max4_n = clf01_max4_n.fit(features_train01_n, labels_train01_n)

# Use the trained classifier to predict labels for the test features
pred_2 = clf_2.predict(features_test)
pred_5 = clf_5.predict(features_test)
pred_10 = clf_10.predict(features_test)
pred_2_n = clf_2_n.predict(features_test_n)
pred_5_n = clf_5_n.predict(features_test_n)
pred_10_n = clf_10_n.predict(features_test_n)
pred01_2 = clf01_2.predict(features_test01)
pred01_5 = clf01_5.predict(features_test01)
pred01_10 = clf01_10.predict(features_test01)
pred01_2_n = clf01_2_n.predict(features_test01_n)
pred01_5_n = clf01_5_n.predict(features_test01_n)
pred01_10_n = clf01_10_n.predict(features_test01_n)

pred_max2 = clf_max2.predict(features_test)
pred_max3 = clf_max3.predict(features_test)
pred_max4 = clf_max4.predict(features_test)
pred_max2_n = clf_max2_n.predict(features_test_n)
pred_max3_n = clf_max3_n.predict(features_test_n)
pred_max4_n = clf_max4_n.predict(features_test_n)
pred01_max2 = clf01_max2.predict(features_test01)
pred01_max3 = clf01_max3.predict(features_test01)
pred01_max4 = clf01_max4.predict(features_test01)
pred01_max2_n = clf01_max2_n.predict(features_test01_n)
pred01_max3_n = clf01_max3_n.predict(features_test01_n)
pred01_max4_n = clf01_max4_n.predict(features_test01_n)

accuracy_2 = DTAccuracy(pred_2, labels_test)
accuracy_5 = DTAccuracy(pred_5, labels_test)
accuracy_10 = DTAccuracy(pred_10, labels_test)
accuracy_2_n = DTAccuracy(pred_2_n, labels_test_n)
accuracy_5_n = DTAccuracy(pred_5_n, labels_test_n)
accuracy_10_n = DTAccuracy(pred_10_n, labels_test_n)
accuracy01_2 = DTAccuracy(pred01_2, labels_test01)
accuracy01_5 = DTAccuracy(pred01_5, labels_test01)
accuracy01_10 = DTAccuracy(pred01_10, labels_test01)
accuracy01_2_n = DTAccuracy(pred01_2_n, labels_test01_n)
accuracy01_5_n = DTAccuracy(pred01_5_n, labels_test01_n)
accuracy01_10_n = DTAccuracy(pred01_10_n, labels_test01_n)

accuracy_max2 = DTAccuracy(pred_max2, labels_test)
accuracy_max3 = DTAccuracy(pred_max3, labels_test)
accuracy_max4 = DTAccuracy(pred_max4, labels_test)
accuracy_max2_n = DTAccuracy(pred_max2_n, labels_test_n)
accuracy_max3_n = DTAccuracy(pred_max3_n, labels_test_n)
accuracy_max4_n = DTAccuracy(pred_max4_n, labels_test_n)
accuracy01_max2 = DTAccuracy(pred01_max2, labels_test01)
accuracy01_max3 = DTAccuracy(pred01_max3, labels_test01)
accuracy01_max4 = DTAccuracy(pred01_max4, labels_test01)
accuracy01_max2_n = DTAccuracy(pred01_max2_n, labels_test01_n)
accuracy01_max3_n = DTAccuracy(pred01_max3_n, labels_test01_n)
accuracy01_max4_n = DTAccuracy(pred01_max4_n, labels_test01_n)

print("Decision Tree accuracy: Predict heart disease (All data(50%) -> All data(50%))")
print("-" * 73)
print("Original Data - 0, 1, 2, 3, 4 (min_samples_split=2) : %.2f %%" % (accuracy_2*100))
print("Original Data - 0, 1, 2, 3, 4 (min_samples_split=5) : %.2f %%" % (accuracy_5*100))
print("Original Data - 0, 1, 2, 3, 4 (min_samples_split=10): %.2f %%" % (accuracy_10*100))
print("-" * 73)
print("Nominal Data - 0, 1, 2, 3, 4 (min_samples_split=2)  : %.2f %%" % (accuracy_2_n*100))
print("Nominal Data - 0, 1, 2, 3, 4 (min_samples_split=5)  : %.2f %%" % (accuracy_5_n*100))
print("Nominal Data - 0, 1, 2, 3, 4 (min_samples_split=10) : %.2f %%" % (accuracy_10_n*100))
print("-" * 73)
print("Original Data - yes or no (min_samples_split=2) : %.2f %%" % (accuracy01_2*100))
print("Original Data - yes or no (min_samples_split=5) : %.2f %%" % (accuracy01_5*100))
print("Original Data - yes or no (min_samples_split=10): %.2f %%" % (accuracy01_10*100))
print("-" * 73)
print("Nominal Data - yes or no (min_samples_split=2)  : %.2f %%" % (accuracy01_2_n*100))
print("Nominal Data - yes or no (min_samples_split=5)  : %.2f %%" % (accuracy01_5_n*100))
print("Nominal Data - yes or no (min_samples_split=10) : %.2f %%" % (accuracy01_10_n*100))
print("-" * 73)
print("Original Data - 0, 1, 2, 3, 4 (max_depth=2) : %.2f %%" % (accuracy_max2*100))
print("Original Data - 0, 1, 2, 3, 4 (max_depth=3) : %.2f %%" % (accuracy_max3*100))
print("Original Data - 0, 1, 2, 3, 4 (max_depth=4) : %.2f %%" % (accuracy_max4*100))
print("-" * 73)
print("Nominal Data - 0, 1, 2, 3, 4 (max_depth=2) : %.2f %%" % (accuracy_max2_n*100))
print("Nominal Data - 0, 1, 2, 3, 4 (max_depth=3) : %.2f %%" % (accuracy_max2_n*100))
print("Nominal Data - 0, 1, 2, 3, 4 (max_depth=4) : %.2f %%" % (accuracy_max2_n*100))
print("-" * 73)
print("Original Data - yes or no (max_depth=2) : %.2f %%" % (accuracy01_max2*100))
print("Original Data - yes or no (max_depth=3) : %.2f %%" % (accuracy01_max3*100))
print("Original Data - yes or no (max_depth=4) : %.2f %%" % (accuracy01_max4*100))
print("-" * 73)
print("Nominal Data - yes or no (max_depth=2) : %.2f %%" % (accuracy01_max2_n*100))
print("Nominal Data - yes or no (max_depth=3) : %.2f %%" % (accuracy01_max3_n*100))
print("Nominal Data - yes or no (max_depth=4) : %.2f %%" % (accuracy01_max4_n*100))

tree.export_graphviz(clf_max3, out_file='tree_max3.dot')
