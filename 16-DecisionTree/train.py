#IMPORT THE LIBRARIES....
import numpy as np # linear algebra....
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)....
from utils import * # preprocessing and transforming data....

from sklearn.tree import DecisionTreeClassifier # Model building and training....

import pickle # Saving and loading models....



url = 'https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv'

titanic = pd.read_csv(url)
titanic.columns = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']

#FILL THE MISSING VALUES WITH THE MEAN & MODE VALUES.. 
titanic['Embarked']=titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])
titanic['Age']=titanic['Age'].fillna(titanic['Age'].median())

titanic = reqd_preprocess(titanic)
titanic = transform_generate(titanic)
titanic = drop_features(titanic)

#Feature Variables
x = titanic.drop('Survived',axis=1)
#Target Variable
y = titanic['Survived']

#Model Training
dtc = DecisionTreeClassifier(
    criterion='entropy',
    ccp_alpha=0.0021, 
    max_depth=16,
    min_samples_leaf=1,
    min_samples_split=2,
    class_weight='balanced',
    splitter='random',
    max_features=4,
    random_state=42
)

dtc.fit(x, y)
print('Model Trained')

pickle.dump(dtc, open('dcsn_tree_clf.sav', 'wb'))
print('Model Saved')