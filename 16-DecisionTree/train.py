#IMPORT THE LIBRARIES....
import numpy as np # linear algebra....
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)....

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

# Preprocessing the Age feature
titanic.loc[ titanic['Age'] <= 16, 'Age'] = 0
titanic.loc[(titanic['Age'] > 16) & (titanic['Age'] <= 26), 'Age'] = 1
titanic.loc[(titanic['Age'] > 26) & (titanic['Age'] <= 36), 'Age'] = 2
titanic.loc[(titanic['Age'] > 36) & (titanic['Age'] <= 62), 'Age'] = 3
titanic.loc[ titanic['Age'] > 62, 'Age'] = 4
titanic['Age'] = titanic['Age'].astype(int)

# Preprocessing the Fare feature
titanic.loc[ titanic['Fare'] <= 7.91, 'Fare'] = 0
titanic.loc[(titanic['Fare'] > 7.91) & (titanic['Fare'] <= 14.454), 'Fare'] = 1
titanic.loc[(titanic['Fare'] > 14.454) & (titanic['Fare'] <= 31), 'Fare']   = 2
titanic.loc[(titanic['Fare'] > 31) & (titanic['Fare'] <= 99), 'Fare']   = 3
titanic.loc[(titanic['Fare'] > 99) & (titanic['Fare'] <= 250), 'Fare']   = 4
titanic.loc[ titanic['Fare'] > 250, 'Fare'] = 5
titanic['Fare'] = titanic['Fare'].astype(int)

# Preprocessing the Name feature
titanic['Name'] = titanic.Name.str.extract(' ([A-Za-z]+)\.', expand = False)
titanic['Name'].unique().tolist()
titanic.rename(columns={'Name' : 'Title'}, inplace=True)
# titanic['Title'] = titanic['Title'].replace(['Mme', 'Mlle', 'Ms', 'Miss'], 'Miss')
titanic['Title'] = titanic['Title'].replace(['Rev', 'Dr', 'Col', 'Ms', 'Mlle', 'Major', 'Countess', 'Capt', 'Dona', 'Jonkheer', 'Lady', 'Sir', 'Mme', 'Don'], 'Other')

# Creating Relatives feature by combining the SibSp and Parch features
titanic['Relatives'] = titanic['SibSp'] + titanic['Parch']

#Feature Transformation.....
titanic['Sex'].replace({'male':0, 'female':1}, inplace=True)
titanic['Embarked'].replace({'S':0, 'C':1,'Q':2}, inplace=True)
titanic['Title'].replace({'Mr':0, 'Mrs':1,'Miss':2,'Master':3,'Other':4}, inplace=True)

#Feature Generation...
titanic.loc[titanic['Relatives'] > 0, 'Not_alone'] = 0
titanic.loc[titanic['Relatives'] == 0, 'Not_alone'] = 1
titanic['Not_alone'] = titanic['Not_alone'].astype(int)

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