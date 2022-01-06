def transformer1(X):
    # copy the array
    df = X.copy()
    df['capital_gain'] = df['capital_gain'] - df['capital_loss']

    df['education'] = df['education_num']

    df['education'] = df['education'].astype('int')

    # Dropping Residual features after features generation
    df.drop(['education_num', 'capital_loss', 'relationship'], axis = 1, inplace = True)

    return df

def create_encoder(X, y):
    # copy the array
    df = X.copy()
    df['income'] = y

    # Encoding the categorical variables
    encoder = {}
    #iterate through the columns
    for col in [i for i in df.columns if df[i].dtypes=='O' and i != 'income']:
        if col != 'marital_status':
            encoder[col] = df[[col, 'income']].groupby([col]).mean().to_dict()['income']
        else:
            encoder[col] = {
                'Never-married': 0,
                'Divorced': 0,
                'Separated': 0,
                'Widowed': 0,
                'Married-civ-spouse': 1,
                'Married-spouse-absent': 1,
                'Married-AF-spouse': 1 
            }
    
    return encoder

def transformer2(X, encoder):
    # copy the array
    df = X.copy()
    
    df = df.replace(encoder)
    df[df.columns[df.dtypes=='O']] = df[df.columns[df.dtypes=='O']].astype('float')

    return df


    