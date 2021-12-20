import numpy as np
import pandas as pd

import statsmodels.api as sm
from patsy import dmatrices

from sklearn.linear_model import LogisticRegression

import pickle


dta = sm.datasets.fair.load_pandas().data

# add "affair" column: 1 represents having affairs, 0 represents not

dta['affair'] = (dta.affairs > 0).astype(int)
dta = dta.drop('affairs', axis=1)

y, X = dmatrices('affair ~ rate_marriage + age + yrs_married + children + \
religious + educ + C(occupation) + C(occupation_husb)', dta, return_type="dataframe")
X = X.rename(columns = {'C(occupation)[T.2.0]':'occ_2',
'C(occupation)[T.3.0]':'occ_3',
'C(occupation)[T.4.0]':'occ_4',
'C(occupation)[T.5.0]':'occ_5',
'C(occupation)[T.6.0]':'occ_6',
'C(occupation_husb)[T.2.0]':'occ_husb_2',
'C(occupation_husb)[T.3.0]':'occ_husb_3',
'C(occupation_husb)[T.4.0]':'occ_husb_4',
'C(occupation_husb)[T.5.0]':'occ_husb_5',
'C(occupation_husb)[T.6.0]':'occ_husb_6'})
cols = X.columns

y = np.ravel(y)

#model = LogisticRegression(C=0.1, max_iter=500, solver='saga')
model = LogisticRegression(C=100)

model.fit(X, y)
print('Model Trained')

pickle.dump([cols, model], open('log_reg.sav', 'wb'))
print('Model Saved')
