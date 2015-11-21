### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

df = pd.read_csv("processed_data/cleveland_data_no_missing_value.csv")
df_n = pd.read_csv("processed_data/cleveland_data_nominal_no_missing_value.csv")

features_train, labels_train, features_test, labels_test = make_train_test_set(df)
features_train_n, labels_train_n, features_test_n, labels_test_n = make_train_test_set(df_n)

# Create classifier
clf = GaussianNB()
clf_n = GaussianNB()
# Fit the classifier on the training features and labels
clf.fit(features_train, labels_train)
clf_n.fit(features_train_n, labels_train_n)
# Use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)
pred_n = clf_n.predict(features_test_n)

accuracy = NBAccuracy(pred, labels_test)
accuracy_n = NBAccuracy(pred_n, labels_test_n)
print("Naive Bayse accuracy          : %.2f %%" % (accuracy*100))
print("Naive Bayse accuracy (Nominal): %.2f %%" % (accuracy_n*100))
