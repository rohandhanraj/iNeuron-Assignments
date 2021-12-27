<h1 style="color:#FF5733 ;font-size:38px;font-family:Lucida Handwriting;text-align:center;">⚓️<strong><u><b>XG Boost Assignment</b></u></strong>⚓️</h1>

<p style= "font-family:Georgia;color:#229A00;font-size:110%;text-align:center;"><br> In this assignment students need to predict whether a person makes over 50K per year or not from classic adult dataset using XGBoost.</p>

<h2 style="color:#FF5733 ;font-size:38px;font-family:Lucida Handwriting;text-align:center;">⚓️<strong><u><b>Data Set Information:</b></u></strong>⚓️</h2>

<p style= "font-family:Georgia;color:#229A00;font-size:110%;text-align:center;"><br>Extraction was done by Barry Becker from the 1994 Census database.  
A set of reasonably clean records was extracted using the following conditions:<br><strong><u><b>((AGE>16) && (AGI>100) && (FNLWGT>1) && (HRSWK>0))</b></u></strong></p>

<h3 style="color:#FF5733 ;font-size:38px;font-family:Lucida Handwriting;text-align:left;">⚓️<strong><u><b>Attribute Information:</b></u></strong>⚓️</h3>

* **Listing of attributes**: >50K, <=50K.
* **age**: continuous.
* **workclass**: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
* **fnlwgt**: continuous.
* **education**: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
* **education-num**: continuous.
* **marital-status**: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
* **occupation**: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
* **relationship**: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
* **race**: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
* **sex**: Female, Male.
* **capital-gain**: continuous.
* **capital-loss**: continuous.
* **hours-per-week**: continuous.
* **native-country**: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

## Following is the code to load required libraries and data:

```python
import numpy as np
import pandas as pd

train_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-
learning-databases/adult/adult.dat a', header = None)

test_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-
databases/adult/adult.test' , skiprows = 1, header = None)

col_labels = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
'marital_status', 'occupation','relationship', 'race', 'sex', capital_gain',
'capital_loss', 'hours_per_week', 'native_country', 'wage_class']

train_set.columns = col_labels
test_set.columns = col_labels
```

## Task
Deploy this assignment in any cloud platform.(Try to look for free cloud platform)

## Assignment
Submit assignment’s deployable link only.
