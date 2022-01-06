import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from sklearn.datasets import load_boston

import pickle

boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos['MDEV'] = boston.target

x = bos.drop('MDEV', axis=1)
y = bos['MDEV']

pre_process = ColumnTransformer(transformers=[
                                    ('drop_columns', 'drop', ['B']),
                                    ('scale_data', StandardScaler(), x.columns)
                                ])

model_pipeline = Pipeline(steps=[('pre_processing',pre_process),
                                 ('model', LinearRegression())
                                 ]) 

model_pipeline.fit(x, y)
print('Model Trained')

pickle.dump(model_pipeline, open('models/lr.sav', 'wb'))
print('Model Saved')