def reqd_preprocess(df):
    def _preprocess_age(df):
        df.loc[ df['Age'] <= 16, 'Age'] = 0
        df.loc[(df['Age'] > 16) & (df['Age'] <= 26), 'Age'] = 1
        df.loc[(df['Age'] > 26) & (df['Age'] <= 36), 'Age'] = 2
        df.loc[(df['Age'] > 36) & (df['Age'] <= 62), 'Age'] = 3
        df.loc[ df['Age'] > 62, 'Age'] = 4
        df['Age'] = df['Age'].astype(int)
        return df
    def _preprocess_fare(df):
        df.loc[ df['Fare'] <= 7.91, 'Fare'] = 0
        df.loc[(df['Fare'] > 7.91) & (df['Fare'] <= 14.454), 'Fare'] = 1
        df.loc[(df['Fare'] > 14.454) & (df['Fare'] <= 31), 'Fare']   = 2
        df.loc[(df['Fare'] > 31) & (df['Fare'] <= 99), 'Fare']   = 3
        df.loc[(df['Fare'] > 99) & (df['Fare'] <= 250), 'Fare']   = 4
        df.loc[ df['Fare'] > 250, 'Fare'] = 5
        df['Fare'] = df['Fare'].astype(int)
        return df
    def _preprocess_name(df):
        df['Name'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand = False)
        df['Name'].unique().tolist()
        df.rename(columns={'Name' : 'Title'}, inplace=True)
        # df['Title'] = df['Title'].replace(['Mme', 'Mlle', 'Ms', 'Miss'], 'Miss')
        df['Title'] = df['Title'].replace(['Rev', 'Dr', 'Col', 'Ms', 'Mlle', 'Major', 'Countess', 'Capt', 'Dona', 'Jonkheer', 'Lady', 'Sir', 'Mme', 'Don'], 'Other')
        return df
    
    # Preprocessing the Age feature
    df = _preprocess_age(df)

    # Preprocessing the Fare feature
    df = _preprocess_fare(df)

    # Preprocessing the Name feature
    df = _preprocess_name(df)
    return df

def transform_generate(df):
    #Feature Transformation.....
    df['Sex'].replace({'male':0, 'female':1}, inplace=True)
    df['Embarked'].replace({'S':0, 'C':1,'Q':2}, inplace=True)
    df['Title'].replace({'Mr':0, 'Mrs':1,'Miss':2,'Master':3,'Other':4}, inplace=True)

    # Creating Relatives feature by combining the SibSp and Parch features
    df['Relatives'] = df['SibSp'] + df['Parch']

    #Feature Generation...
    df.loc[df['Relatives'] > 0, 'Not_alone'] = 0
    df.loc[df['Relatives'] == 0, 'Not_alone'] = 1
    df['Not_alone'] = df['Not_alone'].astype(int)

    return df

def drop_feature(df):
    pass

