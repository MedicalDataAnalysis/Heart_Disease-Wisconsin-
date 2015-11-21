import csv
from create_list import *

csv_output = open("processed_data/cleveland_data_76_attributes.csv", 'wt', newline="")
writer = csv.writer(csv_output)
cleveland_data = open("original_data/cleveland_data.txt", "r")
cleveland = create_list(cleveland_data)
total_patients = len(cleveland)
total_labels = len(cleveland[0])

writer.writerow(["id", "ccf", "age", "sex", "painloc", "painexer", "relrest", "pncaden", "cp", "trestbps",\
"htn", "chol", "smoke", "cigs", "years", "fbs", "dm", "famhist", "restecg", "ekgmo",\
"ekgday", "ekgyr", "dig", "prop", "nitr", "pro", "diuretic", "proto", "thaldur", "thaltime"\
"met", "thalach", "thalrest", "tpeakbps", "tpeakbpd", "dummy", "trestbpd", "exang", "xhypo", "oldpeak"\
"slope", "rldv5", "rldv5e", "ca", "restckm", "exerckm", "restef", "restwm", "exeref", "exerwm",\
"thal", "thalsev", "thalpul", "earlobe", "cmo", "cday", "cyr", "num", "lmt", "ladprox",\
"laddist", "diag", "cxmain", "ramus", "om1", "om2", "rcaprox", "rcadist", "lvx1", "lvx2",\
"lvx3", "lvx4", "lvf", "cathef", "junk", "name"])

writer.writerows(cleveland)

csv_output.close()
