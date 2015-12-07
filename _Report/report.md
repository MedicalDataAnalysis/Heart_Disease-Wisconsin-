# Bigdata Analysis Final Project
## Diagnostic Aid for Heart Disease Using Data
### Seed Project for Medical Platform
--------------------------------------------------------------------------   ___Hankyu Jang, Jihoon Lee___

## 1.Introduction

  The topic of this report is the diagnosing of heart disease. More specifically the possibility of diagnosing a patient without having to interact with other assistant.

  First of all, we have to consider what kind of topic to analyze. Both of us have interest in medical industry to provide diagnosing platform. The platform could help doctor to diagnosing with high confidence because doctor often diagnose with their own instinct which depends their experience and career. But there is always human error in everywhere. One of our student almost lost his mother due to several misdiagnosis. She sprained her ankle. Her ankle was infected by germs after getting an intramuscular shot. She suffered chronic gastritis due to overuse of antibiotics. When she was hospitalized, she even had a hypoglycemic shock which almost took her life away. Fortunately, a doctor finally found that she was suffering from a thyroid disease and she finally recovered her health with appropriate treatment.

  In reality like this situation, some doctor don't have enough time to listen to patients for they rush their visit by limiting the meeting time to strictly less than ten minutes. We believe more data should be used when diagnosing a patient. The data from individual devices which include the personal medical history stored in the medical personal platform. The platform will observe the data and give notice to patients if it detects something unusual. It will recommend a proper hospital to the patents and send their data to the hospital. This will help doctors make better diagnosis and eventually prevent disease from getting worse.

  Our project goal is took data from users which contains symptoms of disease and analyzed symptoms to find out whether users get disease or not. First of all we want diagnosis data which contains symptoms and diagnosing result. In gathering dataset we separate the disease with rules that categorize with part of body section like heart disease, bronchial pneumonia. We find the 'Heart Disease Databases' consist of 'cleveland.data, hungarian.data, long-beach-va.data, switzerland.data' with 76 attributes and 920 examples.

### 1.1 Project Plan
1. Find data

2. Data cleaning

3. Data description

4. Create data set

5. Select methodology

6. Find model

7. Improve model accuracy

8. Conclusion

## 1.2 Data outline

### 1.2.1 Data description

1. Title : Heart Disease Databases

- Source Information:

  (a) Creators:

  1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.

  2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.

  3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.

  4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:
  Robert Detrano, M.D., Ph.D.

  (b) Donor: David W. Aha (aha@ics.uci.edu) (714) 856-8779

  (c) Date: July, 1988

3. Relevant Information:

      This database contains 76 attributes, but all published experiments
      refer to using a subset of 14 of them.  In particular, the Cleveland
      database is the only one that has been used by ML researchers to
      this date.  The "goal" field refers to the presence of heart disease
      in the patient.  It is integer valued from 0 (no presence) to 4.
      Experiments with the Cleveland database have concentrated on simply
      attempting to distinguish presence (values 1,2,3,4) from absence (value
      0).
      - The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

4. Number of Instances:

  Database: # of instances:
  - Cleveland: 303

  - Hungarian: 294

  - Switzerland: 123

  - Long Beach VA: 200

5. Number of Attributes: 76 (including the predicted attribute)

6. Attribute Information:

  __Only 14 used__

  1. 3  (age) age in years

  - 4  (sex) (1 = male; 0 = female)

  - 9  (cp) chest pain type

  - 10 (trestbps) resting blood pressure

  - 12 (chol) serum cholestoral in mg/dl

  - 16 (fbs) fasting blood sugar > 120mg/dl (1 = true; 0 = false)

  - 19 (restecg) resting electrocardiographic results

  - 32 (thalach) maximum heart rate achieved

  - 38 (exang) exercise induced angina (1 = yes; 0 = no)

  -  40 (oldpeak) ST depression induced by exercise relative to rest

  -  41 (slope) the slope of the peak exercise ST segment

  -  44 (ca) number of major vessals (0-3) colored by flourosopy

  -  51 (thal) 3 = normal; 6 = fixed defect; 7 = reversable defect

  -  58 (num) diagnosis of heart disease (the predicted attribute)

  Complete attribute documentation:
  1. id: patient identification number
  2. ccf: social security number (I replaced this with a dummy value of 0)
  3. age: age in years
  4. sex: sex (1 = male; 0 = female)
  5. painloc: chest pain location (1 = substernal; 0 = otherwise)
  6. painexer (1 = provoked by exertion; 0 = otherwise)
  7. relrest (1 = relieved after rest; 0 = otherwise)
  8. pncaden (sum of 5, 6, and 7)
  9. cp: chest pain type       
      - Value 1: typical angina
      - Value 2: atypical angina
      - Value 3: non-anginal pain
      - Value 4: asymptomatic

  10. trestbps: resting blood pressure (in mm Hg on admission to the hospital)
  11. htn
  12. chol: serum cholestoral in mg/dl
  13. smoke: I believe this is 1 = yes; 0 = no (is or is not a smoker)
  14. cigs (cigarettes per day)
  15. years (number of years as a smoker)
  16. fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)
  17. dm (1 = history of diabetes; 0 = no such history)
  18. famhist: family history of coronary artery disease (1 = yes; 0 = no)
  19. restecg: resting electrocardiographic results
  -- Value 0: normal
  -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST
  elevation or depression of > 0.05 mV)
  -- Value 2: showing probable or definite left ventricular hypertrophy
  by Estes' criteria
  20. ekgmo (month of exercise ECG reading)
  21. ekgday(day of exercise ECG reading)
  22. ekgyr (year of exercise ECG reading)
  23. dig (digitalis used furing exercise ECG: 1 = yes; 0 = no)
  24. prop (Beta blocker used during exercise ECG: 1 = yes; 0 = no)
  25. nitr (nitrates used during exercise ECG: 1 = yes; 0 = no)
  26. pro (calcium channel blocker used during exercise ECG: 1 = yes; 0 = no)
  27. diuretic (diuretic used used during exercise ECG: 1 = yes; 0 = no)
  28. proto: exercise protocol
    - 1 = Bruce
    - 2 = Kottus
    - 3 = McHenry
    - 4 = fast Balke
    - 5 = Balke
    - 6 = Noughton
    - 7 = bike 150 kpa min/min
    - 8 = bike 125 kpa min/min
    - 9 = bike 100 kpa min/min
    - 10 = bike 75 kpa min/min
    - 11 = bike 50 kpa min/min
    - 12 = arm ergometer
  29. thaldur: duration of exercise test in minutes
  30. thaltime: time when ST measure depression was noted
  31. met: mets achieved
  32. thalach: maximum heart rate achieved
  33. thalrest: resting heart rate
  34. tpeakbps: peak exercise blood pressure (first of 2 parts)
  35. tpeakbpd: peak exercise blood pressure (second of 2 parts)
  36. dummy
  37. trestbpd: resting blood pressure
  38. exang: exercise induced angina (1 = yes; 0 = no)
  39. xhypo: (1 = yes; 0 = no)
  40. oldpeak = ST depression induced by exercise relative to rest
  41. slope: the slope of the peak exercise ST segment
    - Value 1: upsloping
    - Value 2: flat
    - Value 3: downsloping
  42. rldv5: height at rest
  43. rldv5e: height at peak exercise
  44. ca: number of major vessels (0-3) colored by flourosopy
  45. restckm: irrelevant
  46. exerckm: irrelevant
  47. restef: rest raidonuclid (sp?) ejection fraction
  48. restwm: rest wall (sp?) motion abnormality
    - 0 = none
    - 1 = mild or moderate
    - 2 = moderate or severe
    - 3 = akinesis or dyskmem (sp?)
  49. exeref: exercise radinalid (sp?) ejection fraction
  50. exerwm: exercise wall (sp?) motion
  51. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
  52. thalsev: not used
  53. thalpul: not used
  54. earlobe: not used
  55. cmo: month of cardiac cath (sp?)  (perhaps "call")
  56. cday: day of cardiac cath (sp?)
  57. cyr: year of cardiac cath (sp?)
  58. num: diagnosis of heart disease (angiographic disease status)
    - Value 0: < 50% diameter narrowing
    - Value 1: > 50% diameter narrowing
    - (in any major vessel: attributes 59 through 68 are vessels)
  59. lmt
  60. ladprox
  61. laddist
  62. diag
  63. cxmain
  64. ramus
  65. om1
  66. om2
  67. rcaprox
  68. rcadist
  69. lvx1: not used
  70. lvx2: not used
  71. lvx3: not used
  72. lvx4: not used
  73. lvf: not used
  74. cathef: not used
  75. junk: not used
  76. name: last name of patient

   (I replaced this with the dummy string "name")

7. Missing Attribute Values: Several.  Distinguished with value -9.0.

### 1.2.2 Sample data outline

<img src='/img/sampledata.jpg' width=800/>

### 1.2.3 Data assessment

  1. Missing values

    <img src='/img/missingV.jpg' width=550/>

  missing value is '-9' or '0'. But we figure out that actual missing value is '?' or '-9'. We exchange missing value with other features value's average value. For example feature 'col' has -9 which is missing value we replaced as below.

  ```
  'col'== '-9' or '?' to 'col'= avg value of (feature 'col')
  ```

  We used pandas for replacing. And also used round function to insert integer value to examples.


  2. Outliers

  <img src="/img/outliers.jpg" width=300/>

    Fortunately in 14 features of dataset has two outliers which are 'trestbps' and 'ca' feature. 'trestbps'is maximum heart rate but in Long Beach data one example has value ='0'. And 'ca' range (0~3) but the hungarian data has the 'ca' value is '9'. so we deleted both examples.

#### 1.2.3.1 Descriptive Statistics

  <img src='/img/describe.PNG' width=700/>
- Summary of each features in Heart disease database.

  <img src='/img/histogram.JPG' width=700/>
- histogram of features 'age','blood pressure','cholestoral' and 'Maximum heart rate'

  <img src='/img/scatter.JPG' width=700/>
- Scatter plot with x_label 'age' y_label='blood pressure', 'cholestoral' and 'Maximum heart rate'

<p><img src='/img/bloodP_age.JPG' width=350>
<img src='/img/chol_age.JPG' width=350/></p>

<img src='/img/MaxH_Age.JPG' width=350/>

- In Age- cholesterol scatter plot we recognized that 'switzerland' data which is blue dots are value '0' in every examples. So we have '0' missing value in 'switzerland' data 'cholesterol' feature.

## 2.Body

### 2.1 Methodology

#### 2.1.1 Goal: Predict Heart Disease with given features
1. __Make several datasets__

  - Make presence to absence data

    - Original Data: 0, 1, 2, 3, 4

    - New Data: 0, 1

  - Make feature scaled data

    - Use in SVM

    - Scale each features to have values in 0 and 1

  - Make nominal data

    - Find 25%, 50%, 75% points

    - Divide data into 4 parts

    - Set each parts with values 1 ~ 4

  - Combine all data into one (total 918 patients)

    - Cleveland

    - Hungarian

    - Switzerland

    - VA

2. __Make training set & test set__

  - Cleveland data: few missing values

  - Used Cleveland data + some other data as training set.

  - Find ratio of training set and test set that best predicts heart disease

3. __Algorithms__

  - Naive Bayse

  - Support Vector Machines

  - Decision Tree

#### 2.1.2 Naive Bayse
__Naive Bayes__ methods are a set of supervised learning algorithms based on applying Bayes’ theorem with the “naive” assumption of independence between every pair of features.

#### 2.1.3 Support Vector Machines
__Support vector machines (SVMs)__ are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:
- Effective in high dimensional spaces.
- Still effective in cases where number of dimensions is greater than the number of samples.
- Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
- Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

##### Parameter which makes huge difference in decision boundaries
- Kernel

<img src = "/img/2_SVM_kernel_diagram.PNG" width = 700/>

####  2.1.4 Tree
##### Parameter which makes huge difference in decision boundaries

- Number of samples at leaf node

- Max depth

<img src = "/img/3_Decision_tree_max_depth.PNG" width = 600/>

### 2.2 Working environment

#### 2.2.1 Language
- Python3 (Anaconda)

- Python2 (IPythonNotebook)

#### 2.2.2 Library
- Numpy

- Pandas

- Matplotlib

- Sklearn

- Pydot

#### 2.2.3 Analysis Time

|Week|Activity  |
|----|:--------:|
|4~11|Data Mining (Request data)|
|12|Data Cleaning|
|13~14|Data Analysis|
|15|Prepare Report|

### 2.3 Finding

#### 2.3.1 Naive Bayse

- All Data (Training: 50%, Test: 50%)

|Data Type|Scale|Accuracy|
|---|:---:|:---:|
|___Original___|___0, 1___|___81.30 %___|
|Nominal|0, 1|74.35 %|
|Original|0, 1, 2, 3, 4|37.39 %|
|___Nominal___|___0, 1, 2, 3, 4___|___40.87 %___|

#### 2.3.2 Support Vector Machines

- All Data (Training: 40%, Test: 60%)
chol 0 -> average value

|Data Type|Scale|Kernel|Accuracy|
|---|:---:|:---:|:---:|
|Original|0, 1|rbf|36.96 %|
|Nominal|0, 1|rbf|73.73 %|
|Feature Scaled|0, 1|rbf|77.72 %|
|Original|0, 1, 2, 3, 4|rbf|36.96 %|
|Nominal|0, 1, 2, 3, 4|rbf|42.03 %|
|Feature Scaled|0, 1, 2, 3, 4|rbf|43.84 %|
|___Original___|___0, 1___|___linear___|___79.53 %___|
|Nominal|0, 1|linear|72.46 %|
|Feature Scaled|0, 1|linear|79.35 %|
|___Original___|___0, 1, 2, 3, 4___|___linear___|___47.83 %___|
|Nominal|0, 1, 2, 3, 4|linear|42.93 %|
|Feature Scaled|0, 1, 2, 3, 4|linear|44.75 %|


#### 2.3.3 Decision Tree

- All Data 0, 1 (Training: 50%, Test: 50%)

|Data Type|Scale|# of Samples at Leaf Node|Max Depth|Accuracy|
|---|:---:|:---:|:---:|:---:|
|Original|0, 1|2 |-|62.39 %|
|Original|0, 1|5 |-|64.35 %|
|Original|0, 1|10|-|60.65 %|
|Nominal |0, 1|2 |-|64.35 %|
|Nominal |0, 1|5 |-|61.74 %|
|Nominal |0, 1|10|-|60.00 %|
|Original|0, 1|-|2 |62.83 %|
|___Original___|___0, 1___|-|___3___ |___76.96 %___|
|Original|0, 1|-|4 |73.04 %|
|Nominal |0, 1|-|2 |63.04 %|
|Nominal |0, 1|-|3 |68.26 %|
|Nominal |0, 1|-|4 |63.04 %|

- All Data 0, 1, 2, 3, 4 (Training: 50%, Test: 50%)

|Data Type|Scale|# of Samples at Leaf Node|Max Depth|Accuracy|
|---|:---:|:---:|:---:|:---:|
|___Original___|___0, 1, 2, 3, 4___|___2___ |-|___38.26 %___|
|Original|0, 1, 2, 3, 4|5 |-|36.96 %|
|Original|0, 1, 2, 3, 4|10|-|36.30 %|
|Nominal |0, 1, 2, 3, 4|2 |-|35.65 %|
|Nominal |0, 1, 2, 3, 4|5 |-|36.74 %|
|Nominal |0, 1, 2, 3, 4|10|-|36.96 %|
|Original|0, 1, 2, 3, 4|-|2 |37.83 %|
|Original|0, 1, 2, 3, 4|-|3 |37.61 %|
|Original|0, 1, 2, 3, 4|-|4 |38.04 %|
|Nominal |0, 1, 2, 3, 4|-|2 |38.04 %|
|Nominal |0, 1, 2, 3, 4|-|3 |38.04 %|
|Nominal |0, 1, 2, 3, 4|-|4 |38.04 %|

#### 2.3.4 Algorithms Comparison

|Algorithm|Data Type|Scale|Accuracy|
|---|:---:|:---:|:---:|
|___Naive Bayse___|___Original___|___0, 1___|___81.30 %___|
|SVM (kernel = linear)|Original|0, 1|79.53 %|
|Decision Tree (Max Depth = 3)|Original|0, 1|76.96 %|
|Naive Bayse|Nominal|0, 1, 2, 3, 4|40.87 %|
|___SVM (kernel = linear)___|___Original___|___0, 1, 2, 3, 4___|___47.83 %___|
|Decision Tree (# of samples at leaf node = 2)|Original|0, 1, 2, 3, 4|38.26 %|

## 3.Conclusion

### 3.1 Discovery

- Algorithms with best accuracy

|Algorithm|Data Type|Scale|Accuracy|
|---|:---:|:---:|:---:|
|___Naive Bayse___|___Original___|___0, 1___|___81.30 %___|
|___SVM (kernel = linear)___|___Original___|___0, 1, 2, 3, 4___|___47.83 %___|

### 3.2 Unexpected

- Naive Bayse Accuracy: Analysis using original data (chol not handled) got higher accuracy. Why?

- Visualizing Decision Tree

### 3.3 Expectation

- Predict heart disease using 13 features

- Apply similar logic to other disease

- If these algorithms are applied to all disease, computer can diagnose probability of each disease with given features.

- Doctors will make better diagnosis with help of these algorithms applied to medical data.

### 3.4 In the Future

- GitHub organization: `MedicalDataAnalysis`

- repository: `Heart_Disease`

- Plan to make repositories for other disease whenever we get the data

- Build medical platform using models we created
