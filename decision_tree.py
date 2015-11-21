from sklearn import tree
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

df = pd.read_csv("processed_data/cleveland_data_no_missing_value.csv")

features_train, labels_train, features_test, labels_test = make_train_test_set(df)

# Create classifier
clf2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf10 = tree.DecisionTreeClassifier(min_samples_split=10)

# Fit the classifier on the training features and labels
clf2 = clf2.fit(features_train, labels_train)
clf10 = clf10.fit(features_train, labels_train)

# Use the trained classifier to predict labels for the test features
pred2 = clf2.predict(features_test)
pred10 = clf10.predict(features_test)

accuracy2 = DTAccuracy(pred2, labels_test)
accuracy10 = DTAccuracy(pred10, labels_test)

print("Decision Tree accuracy: Predict heart disease")
print("-" * 73)
print("distinguish presence from 0 to 4 (min_samples_split=2)  : %.2f %%" % (accuracy2*100))
print("distinguish presence from 0 to 4 (min_samples_split=10) : %.2f %%" % (accuracy10*100))
