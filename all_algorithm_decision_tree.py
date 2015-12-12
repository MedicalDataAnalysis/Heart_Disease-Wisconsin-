from sklearn import tree
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
from classify import *
from make_train_test_verification_set import *
from randomize_dataset import *
import csv

csv_output = open("test_verification/all_decision_tree.csv", "w", newline = '')
HeartDiseaseWriter = csv.writer(csv_output)
HeartDiseaseWriter.writerow([\
  "TestSpl2", "TestSpl5", "TestSpl10",\
  "TestSpl2_n", "TestSpl5_n", "TestSpl10_n",\
  "TestSpl2_01", "TestSpl5_01", "TestSpl10_01",\
  "TestSpl2_01_n", "TestSpl5_01_n", "TestSpl10_01_n",\
  "TestDep2", "TestDep3", "TestDep4",\
  "TestDep2_n", "TestDep3_n", "TestDep4_n",\
  "TestDep2_01", "TestDep3_01", "TestDep4_01",\
  "TestDep2_01_n", "TestDep3_01_n", "TestDep4_01_n",\
  "VerifSpl2", "VerifSpl5", "VerifSpl10",\
  "VerifSpl2_n", "VerifSpl5_n", "VerifSpl10_n",\
  "VerifSpl2_01", "VerifSpl5_01", "VerifSpl10_01",\
  "VerifSpl2_01_n", "VerifSpl5_01_n", "VerifSpl10_01_n",\
  "VerifDep2", "VerifDep3", "VerifDep4",\
  "VerifDep2_n", "VerifDep3_n", "VerifDep4_n",\
  "VerifDep2_01", "VerifDep3_01", "VerifDep4_01",\
  "VerifDep2_01_n", "VerifDep3_01_n", "VerifDep4_01_n"
])

training_time = 10

ta = []
va = []

for i in range(training_time):
    randomize()

    af = pd.read_csv("processed_data5(randomize)/all.csv")
    af_n = pd.read_csv("processed_data5(randomize)/all_n.csv")
    af01 = pd.read_csv("processed_data5(randomize)/all01.csv")
    af01_n = pd.read_csv("processed_data5(randomize)/all01_n.csv")

    features_train, labels_train, features_test, labels_test, features_verification, labels_verification = make_train_test_verification_set(af)
    features_train_n, labels_train_n, features_test_n, labels_test_n, features_verification_n, labels_verification_n = make_train_test_verification_set(af_n)
    features_train01, labels_train01, features_test01, labels_test01, features_verification01, labels_verification01 = make_train_test_verification_set(af01)
    features_train01_n, labels_train01_n, features_test01_n, labels_test01_n, features_verification01_n, labels_verification01_n = make_train_test_verification_set(af01_n)

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

    accuracy_2 = DTAccuracy1(pred_2, labels_test)
    accuracy_5 = DTAccuracy1(pred_5, labels_test)
    accuracy_10 = DTAccuracy1(pred_10, labels_test)
    accuracy_2_n = DTAccuracy1(pred_2_n, labels_test_n)
    accuracy_5_n = DTAccuracy1(pred_5_n, labels_test_n)
    accuracy_10_n = DTAccuracy1(pred_10_n, labels_test_n)
    accuracy01_2 = DTAccuracy(pred01_2, labels_test01)
    accuracy01_5 = DTAccuracy(pred01_5, labels_test01)
    accuracy01_10 = DTAccuracy(pred01_10, labels_test01)
    accuracy01_2_n = DTAccuracy(pred01_2_n, labels_test01_n)
    accuracy01_5_n = DTAccuracy(pred01_5_n, labels_test01_n)
    accuracy01_10_n = DTAccuracy(pred01_10_n, labels_test01_n)

    accuracy_max2 = DTAccuracy1(pred_max2, labels_test)
    accuracy_max3 = DTAccuracy1(pred_max3, labels_test)
    accuracy_max4 = DTAccuracy1(pred_max4, labels_test)
    accuracy_max2_n = DTAccuracy1(pred_max2_n, labels_test_n)
    accuracy_max3_n = DTAccuracy1(pred_max3_n, labels_test_n)
    accuracy_max4_n = DTAccuracy1(pred_max4_n, labels_test_n)
    accuracy01_max2 = DTAccuracy(pred01_max2, labels_test01)
    accuracy01_max3 = DTAccuracy(pred01_max3, labels_test01)
    accuracy01_max4 = DTAccuracy(pred01_max4, labels_test01)
    accuracy01_max2_n = DTAccuracy(pred01_max2_n, labels_test01_n)
    accuracy01_max3_n = DTAccuracy(pred01_max3_n, labels_test01_n)
    accuracy01_max4_n = DTAccuracy(pred01_max4_n, labels_test01_n)

    # Use the trained classifier to predict labels for the verification features
    vpred_2 = clf_2.predict(features_verification)
    vpred_5 = clf_5.predict(features_verification)
    vpred_10 = clf_10.predict(features_verification)
    vpred_2_n = clf_2_n.predict(features_verification_n)
    vpred_5_n = clf_5_n.predict(features_verification_n)
    vpred_10_n = clf_10_n.predict(features_verification_n)
    vpred01_2 = clf01_2.predict(features_verification01)
    vpred01_5 = clf01_5.predict(features_verification01)
    vpred01_10 = clf01_10.predict(features_verification01)
    vpred01_2_n = clf01_2_n.predict(features_verification01_n)
    vpred01_5_n = clf01_5_n.predict(features_verification01_n)
    vpred01_10_n = clf01_10_n.predict(features_verification01_n)

    vpred_max2 = clf_max2.predict(features_verification)
    vpred_max3 = clf_max3.predict(features_verification)
    vpred_max4 = clf_max4.predict(features_verification)
    vpred_max2_n = clf_max2_n.predict(features_verification_n)
    vpred_max3_n = clf_max3_n.predict(features_verification_n)
    vpred_max4_n = clf_max4_n.predict(features_verification_n)
    vpred01_max2 = clf01_max2.predict(features_verification01)
    vpred01_max3 = clf01_max3.predict(features_verification01)
    vpred01_max4 = clf01_max4.predict(features_verification01)
    vpred01_max2_n = clf01_max2_n.predict(features_verification01_n)
    vpred01_max3_n = clf01_max3_n.predict(features_verification01_n)
    vpred01_max4_n = clf01_max4_n.predict(features_verification01_n)

    vaccuracy_2 = DTAccuracy1(vpred_2, labels_verification)
    vaccuracy_5 = DTAccuracy1(vpred_5, labels_verification)
    vaccuracy_10 = DTAccuracy1(vpred_10, labels_verification)
    vaccuracy_2_n = DTAccuracy1(vpred_2_n, labels_verification_n)
    vaccuracy_5_n = DTAccuracy1(vpred_5_n, labels_verification_n)
    vaccuracy_10_n = DTAccuracy1(vpred_10_n, labels_verification_n)
    vaccuracy01_2 = DTAccuracy(vpred01_2, labels_verification01)
    vaccuracy01_5 = DTAccuracy(vpred01_5, labels_verification01)
    vaccuracy01_10 = DTAccuracy(vpred01_10, labels_verification01)
    vaccuracy01_2_n = DTAccuracy(vpred01_2_n, labels_verification01_n)
    vaccuracy01_5_n = DTAccuracy(vpred01_5_n, labels_verification01_n)
    vaccuracy01_10_n = DTAccuracy(vpred01_10_n, labels_verification01_n)

    vaccuracy_max2 = DTAccuracy1(vpred_max2, labels_verification)
    vaccuracy_max3 = DTAccuracy1(vpred_max3, labels_verification)
    vaccuracy_max4 = DTAccuracy1(vpred_max4, labels_verification)
    vaccuracy_max2_n = DTAccuracy1(vpred_max2_n, labels_verification_n)
    vaccuracy_max3_n = DTAccuracy1(vpred_max3_n, labels_verification_n)
    vaccuracy_max4_n = DTAccuracy1(vpred_max4_n, labels_verification_n)
    vaccuracy01_max2 = DTAccuracy(vpred01_max2, labels_verification01)
    vaccuracy01_max3 = DTAccuracy(vpred01_max3, labels_verification01)
    vaccuracy01_max4 = DTAccuracy(vpred01_max4, labels_verification01)
    vaccuracy01_max2_n = DTAccuracy(vpred01_max2_n, labels_verification01_n)
    vaccuracy01_max3_n = DTAccuracy(vpred01_max3_n, labels_verification01_n)
    vaccuracy01_max4_n = DTAccuracy(vpred01_max4_n, labels_verification01_n)

    ta.append((round(accuracy_2, 2), round(accuracy_5, 2), round(accuracy_10, 2),\
      round(accuracy_2_n, 2), round(accuracy_5_n, 2), round(accuracy_10_n, 2),\
      round(accuracy01_2, 2), round(accuracy01_5, 2), round(accuracy01_10, 2),\
      round(accuracy01_2_n, 2), round(accuracy01_5_n, 2), round(accuracy01_10_n, 2),\
      round(accuracy_max2, 2), round(accuracy_max3, 2), round(accuracy_max4, 2),\
      round(accuracy_max2_n, 2), round(accuracy_max3_n, 2), round(accuracy_max4_n, 2),\
      round(accuracy01_max2, 2), round(accuracy01_max3, 2), round(accuracy01_max4, 2),\
      round(accuracy01_max2_n, 2), round(accuracy01_max3_n, 2), round(accuracy01_max4_n, 2)
    ))
    va.append((round(vaccuracy_2, 2), round(vaccuracy_5, 2), round(vaccuracy_10, 2),\
      round(vaccuracy_2_n, 2), round(vaccuracy_5_n, 2), round(vaccuracy_10_n, 2),\
      round(vaccuracy01_2, 2), round(vaccuracy01_5, 2), round(vaccuracy01_10, 2),\
      round(vaccuracy01_2_n, 2), round(vaccuracy01_5_n, 2), round(vaccuracy01_10_n, 2),\
      round(vaccuracy_max2, 2), round(vaccuracy_max3, 2), round(vaccuracy_max4, 2),\
      round(vaccuracy_max2_n, 2), round(vaccuracy_max3_n, 2), round(vaccuracy_max4_n, 2),\
      round(vaccuracy01_max2, 2), round(vaccuracy01_max3, 2), round(vaccuracy01_max4, 2),\
      round(vaccuracy01_max2_n, 2), round(vaccuracy01_max3_n, 2), round(vaccuracy01_max4_n, 2)
    ))

    HeartDiseaseWriter.writerow([\
      ta[i][0], ta[i][1], ta[i][2], ta[i][3], ta[i][4], ta[i][5],\
      ta[i][6], ta[i][7], ta[i][8], ta[i][9], ta[i][10], ta[i][11],\
      ta[i][12], ta[i][13], ta[i][14], ta[i][15], ta[i][16], ta[i][17],\
      ta[i][18], ta[i][19], ta[i][20], ta[i][21], ta[i][22], ta[i][23],\
      va[i][0], va[i][1], va[i][2], va[i][3], va[i][4], va[i][5],\
      va[i][6], va[i][7], va[i][8], va[i][9], va[i][10], va[i][11],\
      va[i][12], va[i][13], va[i][14], va[i][15], va[i][16], va[i][17],\
      va[i][18], va[i][19], va[i][20], va[i][21], va[i][22], va[i][23]
    ])

csv_output.close()


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
