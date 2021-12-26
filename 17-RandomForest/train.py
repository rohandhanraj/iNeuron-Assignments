import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

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
                                    ('scale_data', MinMaxScaler(), x.columns)
                                ])
model = RandomForestRegressor(
    ccp_alpha=0.001,
    criterion='mae',
    max_depth=834,
    min_samples_split=9,
    n_estimators=61,
    random_state=137
    )

model_pipeline = Pipeline(steps=[('pre_processing',pre_process),
                                 ('model', model)
                                 ]) 

model_pipeline.fit(x, y)
print('Model Trained')

pickle.dump(model_pipeline, open('rf.sav', 'wb'))
print('Model Saved')

