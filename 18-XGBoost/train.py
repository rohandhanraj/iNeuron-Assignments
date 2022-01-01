#IMPORT THE LIBRARIES....
import numpy as np # linear algebra....
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)....
from utils import * # preprocessing and transforming data....

from  xgboost import XGBClassifier # Model building and training....

import pickle


train_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', header = None)

test_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test' , skiprows = 1, header = None)

col_labels = [
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education_num',
    'marital_status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital_gain',
    'capital_loss',
    'hours_per_week',
    'native_country',
    'wage_class'
    ]

train_set.columns = col_labels
test_set.columns = col_labels

# Merging the Train and Test Datasets
# 
df = pd.concat([train_set, test_set], axis = 0)
df['income']=df['wage_class'].map({' <=50K': 0, ' >50K': 1, ' <=50K.': 0, ' >50K.': 1})
df = df.drop(['wage_class'], axis = 1)
df[['education_num', 'income']] = df[['education_num', 'income']].astype('int')

# MISSING VALUES(' ?') in DataFrame..... 
missing = df.columns[np.where(df.eq(' ?').sum() > 0)]
# Fill the missing values with the mode of the column
for col in missing:
    df[col][df[col] == ' ?'] = df[col].value_counts().index[0]

df['capital_gain'] = df['capital_gain'] - df['capital_loss']
df = df.rename(columns={'capital_gain': 'capital_gross'})

df.drop(columns=['education_num'], axis = 1, inplace = True)
mean_encoder = {}
#iterate through the columns
for col in [i for i in df.columns if df[i].dtypes=='O' and i != 'split']:
    mean_encoder[col] = df[[col, 'income']].groupby([col]).mean().to_dict()['income']
df = df.replace(mean_encoder)
df[df.columns[df.dtypes=='O'][:-1]] = df[df.columns[df.dtypes=='O'][:-1]].astype('float')

df.drop('relationship', axis = 1, inplace = True)
df["marital_status"] = df["marital_status"].replace([' Married-civ-spouse',' Married-spouse-absent',' Married-AF-spouse'], 'Married')
df["marital_status"] = df["marital_status"].replace([' Never-married',' Divorced',' Separated',' Widowed'], 'Single')
df["marital_status"] = df["marital_status"].map({"Married":0, "Single":1})
df = df.rename(columns={'marital_status': 'couple'})