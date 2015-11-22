from sklearn.svm import SVC
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_set import *

df = pd.read_csv("processed_data/cleveland_data_no_missing_value.csv")
df_n = pd.read_csv("processed_data/cleveland_data_nominal_no_missing_value.csv")
df01 = pd.read_csv("processed_data/cleveland_data_no_missing_value_01.csv")
df01_n = pd.read_csv("processed_data/cleveland_data_nominal_no_missing_value_01.csv")
df_fs = pd.read_csv("feature_scaled_data/feature_scaled_cleveland_data_no_missing_value.csv")
df01_fs = pd.read_csv("feature_scaled_data/feature_scaled_cleveland_data_no_missing_value_01.csv")

features_train, labels_train, features_test, labels_test = make_train_test_set(df)
features_train_n, labels_train_n, features_test_n, labels_test_n = make_train_test_set(df_n)
features_train01, labels_train01, features_test01, labels_test01 = make_train_test_set(df01)
features_train01_n, labels_train01_n, features_test01_n, labels_test01_n = make_train_test_set(df01_n)
features_train_fs, labels_train_fs, features_test_fs, labels_test_fs = make_train_test_set(df_fs)
features_train01_fs, labels_train01_fs, features_test01_fs, labels_test01_fs = make_train_test_set(df01_fs)

# Create classifier
clf = SVC()
clf_n = SVC()
clf01 = SVC()
clf01_n = SVC()
clf_fs = SVC()
clf01_fs = SVC()

# Fit the classifier on the training features and labels
clf.fit(features_train, labels_train)
clf_n.fit(features_train_n, labels_train_n)
clf01.fit(features_train01, labels_train01)
clf01_n.fit(features_train01_n, labels_train01_n)
clf_fs.fit(features_train_fs, labels_train_fs)
clf01_fs.fit(features_train01_fs, labels_train01_fs)

# Use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)
pred_n = clf_n.predict(features_test_n)
pred01 = clf01.predict(features_test01)
pred01_n = clf01_n.predict(features_test01_n)
pred_fs = clf_fs.predict(features_test_fs)
pred01_fs = clf01_fs.predict(features_test01_fs)

accuracy = SVMAccuracy(pred, labels_test)
accuracy_n = SVMAccuracy(pred_n, labels_test_n)
accuracy01 = SVMAccuracy(pred01, labels_test01)
accuracy01_n = SVMAccuracy(pred01_n, labels_test01_n)
accuracy_fs = SVMAccuracy(pred_fs, labels_test_fs)
accuracy01_fs = SVMAccuracy(pred01_fs, labels_test01_fs)

print("Support Vector Machines accuracy")
print("-" * 73)
print("Predict heart disease (distinguish presence from 0 to 4)        : %.2f %%" % (accuracy*100))
print("Predict heart disease (distinguish presence from 0 to 4 Nominal): %.2f %%" % (accuracy_n*100))
print("-" * 73)
print("Predict heart disease (yes or no)         : %.2f %%" % (accuracy01*100))
print("Predict heart disease (yes or no nominal) : %.2f %%" % (accuracy01_n*100))
print("-" * 73)
print("Feature Scaled Data - Predict heart disease (0 to 4)   : %.2f %%" % (accuracy_fs*100))
print("Feature Scaled Data - Predict heart disease (yes or no) : %.2f %%" % (accuracy01_fs*100))
