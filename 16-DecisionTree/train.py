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

# Drop the columns that we don't need
titanic.drop(columns = ['Cabin','PassengerId'],axis = 1,inplace = True)





#Dropping the redundant columns...
#Since the Ticket attribute has 681 unique tickets, it will be a bit lengthy to convert them into useful categories. So we will drop it from the dataset.
titanic.drop(columns = ['Pclass','Age','SibSp','Not_alone','Ticket'],axis = 1,inplace = True)

#Feature Variables
x = titanic.drop('Survived',axis=1)
cols = x.columns
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

pickle.dump([cols, dtc], open('dcsn_tree_clf.sav', 'wb'))
print('Model Saved')