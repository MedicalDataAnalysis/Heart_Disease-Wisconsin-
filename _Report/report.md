# Bigdata Analysis Final Project
## Diagnostic Aid for Heart Disease Using Data
### Seed Project for Medical Platform
--------------------------------------------------------------------------   ___Hankyu Jang, Jihoon Lee___

## Index
- 1.Introduction
  - 1.1 Project Plan
  - 1.2 Data Outline
    - 1.2.1 Data Description
    - 1.2.2 Sample Data Outline
    - 1.2.3 Data Assessment
      - 1.2.3.1 Descriptive Statistics
- 2.Body
  - 2.1 Methodology
    - 2.1.1 Goal: Predict Heart Disease with Given Features
    - 2.1.2 Naive Bayse
    - 2.1.3 Support Vector Machines
    - 2.1.4 Tree
  - 2.2 Working Environment
    - 2.2.1 Language
    - 2.2.2 Library
    - 2.2.3 Analysis Time
  - 2.3 Finding
    - 2.3.1 Naive Bayse
    - 2.3.2 Support Vector Machines
    - 2.3.3 Decision Tree
    - 2.3.4 Algorithms Comparison
- 3.Conclusion
  - 3.1 Discovery
  - 3.2 Unexpected
  - 3.3 Expectation
  - 3.4 In the Future
- 4.Reference

## 1.Introduction

The topic of this report is the diagnosing of heart disease. More specifically the possibility of diagnosing a patient without having to interact with other assistant.

First of all, we had to consider what kind of topic to analyze. Both of us have interest in medical industry to provide diagnosing platform. The platform could help doctors to diagnose with high confidence because doctor often diagnose with their own instinct depending on their experience and career. But there is always human error in everywhere. Hankyu almost lost his mother due to several misdiagnoses. She sprained her ankle. Her ankle was infected by germs after getting an intramuscular shot. She suffered chronic gastritis due to overuse of antibiotics. When she was hospitalized, she even had a hypoglycemic shock which almost took her life away. Fortunately, a doctor finally found that she was suffering from a thyroid disease and she finally recovered her health with appropriate treatment.

<img src = "/img/thyroid.png" width = 600 />

In reality like this situation, some doctor doesn’t have enough time to listen to patients for they rush their visit by limiting the meeting time to strictly less than five minutes. We believe that more data should be used when diagnosing a patient. The data from individual devices which include the personal medical history stored in the medical personal platform. The platform will observe the data and give notice to patients if it detects something unusual. It will recommend a proper hospital to the patents and send their data to the hospital. This will help doctors make better diagnosis and eventually prevent disease from getting worse.

Our project goal is to take data from users which contains symptoms of disease and analyzed symptoms to find out whether users get disease or not. First of all, we want diagnosis data which contains symptoms and diagnosing result. In gathering dataset, we separate the disease with rules that categorize with part of body section like heart disease, bronchial pneumonia. We find the 'Heart Disease Databases' consist of 'cleveland.data, hungarian.data, long-beach-va.data, switzerland.data' with 76 attributes and 920 examples.

### 1.1 Project Plan
1. Find data

2. Data cleaning

3. Data description

4. Create data set

5. Select methodology

6. Find model

7. Improve model accuracy

8. Conclusion

## 1.2 Data Outline

### 1.2.1 Data Description

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

  2. 4  (sex) (1 = male; 0 = female)

  3. 9  (cp) chest pain type

  4. 10 (trestbps) resting blood pressure

  5. 12 (chol) serum cholestoral in mg/dl

  6. 16 (fbs) fasting blood sugar > 120mg/dl (1 = true; 0 = false)

  7. 19 (restecg) resting electrocardiographic results

  8. 32 (thalach) maximum heart rate achieved

  9. 38 (exang) exercise induced angina (1 = yes; 0 = no)

  10.  40 (oldpeak) ST depression induced by exercise relative to rest

  11.  41 (slope) the slope of the peak exercise ST segment

  12.  44 (ca) number of major vessals (0-3) colored by flourosopy

  13.  51 (thal) 3 = normal; 6 = fixed defect; 7 = reversable defect

  14.  58 (num) diagnosis of heart disease (the predicted attribute)

7. Missing Attribute Values: Several.  Distinguished with value -9.0.

### 1.2.2 Sample Data Outline

<img src='/img/sampledata.jpg' width=800/>

### 1.2.3 Data Assessment

  1. Missing values

    <img src='/img/missingV.jpg' width=550/>

  Missing value is '-9' or '0'. But we figure out that actual missing value is '?' or '-9'. When we eliminated patients with missing values, 67.5% of data were deleted. This was a huge loss, so we decided to preserve data by filling in the missing values with the average value of its feature computed from other patients. For example feature 'col' has -9 which is missing value we replaced as below.

  ```
  'col'== '-9' or '?' to 'col'= avg value of (feature 'col')
  ```

  We used Pandas library for replacing. And also used round function to insert integer value to examples. Figure below is the missing value insert in each datasets.

  <img src = "/img/missing_value.jpg" width = 600/>

  2. Outliers

  <img src="/img/outliers.jpg" width=300/>

    Fortunately in 14 features of dataset has two outliers which are 'trestbps' and 'ca' feature. 'trestbps'is maximum heart rate but in Long Beach data one example has value ='0'. And 'ca' range (0~3) but the hungarian data has the 'ca' value is '9'. so we deleted both examples.

  3. Combine datasets
    - Cleveland
    <img src = "/img/data_cleveland.jpg" width = 800/>

    - Hungarian
    <img src = "/img/data_hungarian.jpg" width = 800/>

    - Switzerland
    <img src = "/img/data_switzerland.jpg" width = 800/>

    - Long Beach
    <img src = "/img/data_long_beach.jpg" width = 800/>

    Except for `ca` and `chol` features, others have similarity in each data set. Every `[mean, min, 25%, 50%, 75%, max]` values’ errors are within 10% range. It is considered that each data sets bear resemblance to other data sets. We drew scatter plot graphs of each data sets below to help you visualize the state of data sets.

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

#### 2.1.1 Goal: Predict Heart Disease with Given Features

1. __Make several datasets__

  Before diving into analysis, we reorganized the data into a proper format for use in analysis. We created presence to absence data by changing the labels (0 -> 0 and 1, 2, 3, 4 -> 1). Then we created another two data sets using the original data. First, we applied feature scaling method to make a new data by standardizing the features for use in SVM. Second, we calculated quantiles of continuous features to categorize entries into four groups because we wanted to check whether or not this grouping would provide better prediction.

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
    The feature characteristics of four regions are similar

    - Cleveland

    - Hungarian

    - Switzerland

    - VA

2. __Make training set, test set, and verification set__

  To make models and verify them, we randomly divided each data set into three parts: 60% for training, 20% for test and 20% for verification. Then, we created hundreds of models using training data and tested them with test features to find the one with the highest performance.

  -	Training set: 60%
  -	Test set: 20%
  -	Verification set: 20%

3. __Made Accuracy Function to adequately give accuracy on 0, 1, 2, 3, 4 Prediction__
At first, we used an accuracy function that calculates accuracy only if the two given values have the same value. Let’s assume that a patient’s heart disease rate was 4. Also, assume that there are two cases of prediction: case 1 predicts the label with value 3 and case2 predicts the label with value 0. The accuracy function returns 0% accuracy on both cases. However, this behavior needed to be changed because case 1 is much more accurate than case 2.

Therefore, we gave an accuracy of 0.8 on the value in which the difference between real label and prediction label is equal to 1. For example, accuracy function will return 80% accuracy on case 1 above. However, if the model predicts label 1 with 0, we didn’t give accuracy because this may predict a person having no heart disease even if he doesn’t have heart disease and vice versa.

4. __Algorithms__

  - Naive Bayse

  - Support Vector Machines

  - Decision Tree

#### 2.1.2 Naive Bayse
__Naive Bayes__ methods are a set of supervised learning algorithms based on applying Bayes’ theorem with the “naive” assumption of independence between every pair of features.

#### 2.1.3 Support Vector Machines
__Support vector machines (SVMs)__ are a set of supervised learning methods used for classification, regression and outliers detection.

##### Parameter which makes huge difference in decision boundaries
- Kernel

<img src = "/img/2_SVM_kernel_diagram.PNG" width = 700/>

####  2.1.4 Tree
##### Parameter which makes huge difference in decision boundaries

- Number of samples at leaf node

- Max depth

<img src = "/img/3_Decision_tree_max_depth.PNG" width = 600/>

### 2.2 Working Environment

#### 2.2.1 Language

-	Python3 (Anaconda): Data Cleaning & Analysis
-	Python2 (IPythonNotebook): Plotting
-	SPSS: Plotting

#### 2.2.2 Library
- Numpy

- Pandas

- Matplotlib

- Sklearn

#### 2.2.3 Analysis Time

|Week|Activity  |
|----|:--------:|
|4~11|Data Mining (Request data)|
|12|Data Cleaning|
|13~15|Data Analysis|
|16|Prepare Report|

#### 2.2.4 Team Role

|Name|Role  |
|----|:--------:|
|Hankyu Jang|Data Request, Cleaning, Analysis, Plotting using SPSS|
|Jihoon Lee|Data Request, Research Article Analysis, Plotting using Matplotlib, Organize Report|

### 2.3 Finding

#### 2.3.1 Naive Bayse

-	Simulation 10 times (Training: 60%, Test: 20%, Verification: 20%)

- 0, 1 Prediction
  -	Best training set prediction percentage: 85%

  -	Corresponding verification set prediction percentage: 76%

- 0, 1, 2, 3, 4 Prediction
  -	Best training set prediction percentage: 73%

  -	Corresponding verification set prediction percentage: 74%

<img src = "/img/test_verification_Naive_Bayse_01.jpg" width = 400 />
<img src = "/img/test_verification_Naive_Bayse_01234.jpg" width = 400 />

#### 2.3.2 Support Vector Machines

-	Simulation 10 times (Training: 60%, Test: 20%, Verification: 20%)

- 0, 1 Prediction
  -	Best training set prediction percentage: 87% (rbf kernel)

  -	Corresponding verification set prediction percentage: 82%

- 0, 1, 2, 3, 4 Prediction
  -	Best training set prediction percentage: 76% (linear kernel)

  -	Corresponding verification set prediction percentage: 77%

<img src = "/img/test_verification_SVM_linear_01.jpg" width = 400 />
<img src = "/img/test_verification_SVM_linear_01234.jpg" width = 400 />
<img src = "/img/test_verification_SVM_rbf_01.jpg" width = 400 />
<img src = "/img/test_verification_SVM_rbf_01234.jpg" width = 400 />

#### 2.3.3 Decision Tree

-	Simulation 10 times (Training: 60%, Test: 20%, Verification: 20%)
-	Controlling max depth is better than controlling min split in leaf node.

- 0, 1 Prediction>
  -	Best training set prediction percentage: 83% (max depth = 4)

  -	Corresponding verification set prediction percentage: 72%

- 0, 1, 2, 3, 4 Prediction
  -	Best training set prediction percentage: 73% (max depth = 2)

  -	Corresponding verification set prediction percentage: 72%

<img src = "/img/test_verification_Decision_Tree_Depth_01.jpg" width = 400 />
<img src = "/img/test_verification_Decision_Tree_Depth_01234.jpg" width = 400 />
<img src ="/img/test_verification_Decision_Tree_Split_01.jpg" width = 400 />
<img src = "/img/test_verification_Decision_Tree_Split_01234.jpg" width = 400 />

#### 2.3.4 Algorithms Comparison

-	Best algorithm to predict hearth disease: SVM

<img src = "/img/algorithms_compare_01.jpg" width = 400 />
<img src = "/img/algorithms_compare_01234.jpg" width = 400 />

## 3.Conclusion

### 3.1 Discovery

- Algorithms with best accuracy

|Algorithm|Data Type|Scale|Accuracy|
|---|:---:|:---:|:---:|
|___SVM (kernel = rbf)___|___Feature Scaled Data___|___0, 1___|___82 %___|
|___SVM (kernel = linear)___|___Nominal Data___|___0, 1, 2, 3, 4___|___77 %___|

Best Working Data Sets for Each Algorithm

-	Naïve Bayse: Original Data
-	SVM: Feature Scaled Data, Nominal Data
-	Decision Tree: Nominal Data


### 3.2 Unexpected

- Difficulty in Visualizing Decision Tree

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

## 4.Reference

- Hyebong Choi(2015), "PRESENTATION IN DATA SCIENCE", CCE40001: BIG DATA ANALYTICS

- Jyoti Soni, Uzma Ansari, Dipesh Sharma, Sunita Soni(2011), "Intelligent and Effective Heart Disease Prediction System using Weighted Associative Classifiers, IJCSE

- Mai Shouman, Tim Turner, Rob Stocker(2011), "Using Decision Tree for Diagnosing Heart Disease Patients", CRPIT Volume 121 - Data Mining and Analytics 2011

- Ms. Shinde Swati B, March-April, 2015, "Decision Support System on Prediction of Heart Disease Using Data Mining Techniques", International Journal of Engineering Research and General Science Volume 3, Issue 2

- Pawel Herman, Orjan Ekeberg(2015), "Early Screening Diagnostic Aid for Heart Disease using Data Mining", KTH Computer Science and Communication

- Prof.K.Rajewari, Dr.V. Vaithiyanathan, Shailaja V.Pede(2013), "Feature Selection for Classification in Medical Data Mining", IJETTCS

- Swati Shilaskar, Ashok Ghatol(2013), "Dimensionality Reduction Techniques for Improved Diagnosis of Heart Disease", IJCA

- Decision Tree, scikit-learn documentation version 0.17, http://scikit-learn.org/stable/modules/tree.html

- Naive Bayse, scikit-learn documentation version 0.17, http://scikit-learn.org/stable/modules/naive_bayes.html

- Support Vector Machines, scikit-learn documentation version 0.17, http://scikit-learn.org/stable/modules/svm.html

- cleveland.data, Cleveland Clinic Foundation

- hungarian.data, Hungarian Institute of Cardiology, Budapest

- long-beach-va.data, V.A. Medical Center, Long Beach, CA

- switzerland.data, University Hospital, Zurich, Switzerland

- Udacity, “Intro to Machine Learning”, https://www.udacity.com/course/intro-to-machine-learning--ud120
