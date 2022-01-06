#IMPORT THE LIBRARIES....
import numpy as np # linear algebra....
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)....
from utils import * # preprocessing and transforming data....

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.pipeline import Pipeline

from  xgboost import XGBClassifier # Model building and training....

import pickle


train_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', sep=', ', header = None, engine = 'python')

test_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test' , skiprows = 1, sep=', ', header = None, engine = 'python')

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
df['income']=df['wage_class'].map({'<=50K': 0, '>50K': 1, '<=50K.': 0, '>50K.': 1})
df = df.drop(['wage_class'], axis = 1)

# Dropping the irrelevant observations
df = df.iloc[np.where((df.age > 16) & ((df.capital_gain > 100) | (df.capital_loss > 100)) & (df.fnlwgt > 1) & (df.hours_per_week > 0))]

X = df.drop(['income'], axis = 1)
y = df['income']

# Creating encoder for Categorical variables
encoder = create_encoder(X, y)

# Function Transformers
trans1 = FunctionTransformer(transformer1)
trans2 = FunctionTransformer(transformer2, kw_args={'encoder': encoder})

# Scaling The features
# [listing the columns which won't be dropped by transformer1 & transformer2]
scale = ColumnTransformer(transformers=[
    (
        'scaler',
        StandardScaler(),
        [
            'age',
            'workclass',
            'fnlwgt',
            'education',
            'marital_status',
            'occupation',
            'race',
            'sex',
            'capital_gain',
            'hours_per_week',
            'native_country'
        ]
    )
])

# Building model with best parameters
params = {
    'alpha': 0.01,
    'booster': 'dart',
    'eta': 0.0008,
    'gamma': 0.0012,
    'lambda': 0.01,
    'learning_rate': 0.11,
    'max_depth': 50,
    'n_estimators': 670,
    'objective': 'binary:logistic',
    'random_state': 0,
    'tree_method': 'auto'
 }

model = XGBClassifier( **params)

# Defining the Pipeline and fitting it
pipeline = Pipeline(steps=[
    ('transformer1', trans1),
    ('transformer2', trans2),
    ('scaler', scale),
    ('model', model)
],
verbose=True)

pipeline.fit(X, y)

pickle.dump(pipeline, open('models/xgb_clf.sav', 'wb'))