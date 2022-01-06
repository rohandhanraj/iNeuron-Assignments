import numpy as np
import pandas as pd
from utils import * # preprocessing and transforming data....

from wsgiref import simple_server
from flask import Flask, render_template, request, Response
from flask_cors import CORS,cross_origin

import os
import pickle


#os.putenv('LANG', 'en_US.UTF-8')
#os.putenv('LC_ALL', 'en_US.UTF-8')

model = pickle.load(open('lr.sav', 'rb'))

app = Flask(__name__)
#CORS(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/lr', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def lin_reg():
    return render_template('boston.html')

@app.route('/log-reg', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('affairs.html')

@app.route('/dt', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('titanic.html')

@app.route('/rf', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('boston_rf.html')

@app.route('/xgb', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('adult_income.html')


@app.route('/xgb-res', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_dict = request.form.to_dict()
            print(input_dict)
            input_features = {k.strip(): [v] for k, v in input_dict.items()}
            print(input_features)
            for f in ['age', 'fnlwgt', 'capital_gain', 'capital_loss', 'hours_per_week']:
                input_features[f] = list(map(float, input_features[f])) # Convert to float
            print(input_features)
            
            data = pd.DataFrame(input_features)

            model = pickle.load(open('models/xgb_clf.sav', 'rb'))

            pred = model.predict(data)[0]
            result = 'LESS THAN $50K' if pred == 0 else 'MORE THAN $50K'
            print(f'Result:\n{"-"*10} \nIncome: {result}')

            return render_template('xgb_res.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('adult.html')


@app.route('/rf-res', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_dict = request.form.to_dict()
            print(input_dict)
            input_features = {k.strip(): [float(v)] for k, v in input_dict.items()}
            print(input_features)
            
            data = pd.DataFrame(input_features)

            model = pickle.load(open('models/rf.sav', 'rb'))

            pred = model.predict(data)[0]
            result = pred * 1000
            print(f'Result is: {result}')

            return render_template('rf_res.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('boston_rf.html')


@app.route('/dt-res', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_dict = request.form.to_dict()
            print(input_dict)
            input_features = {k.strip(): [v] for k, v in input_dict.items()}
            print(input_features)
            data = pd.DataFrame(input_features)
            print('DataFrame Created:\n', data)

            model = pickle.load(open('models/dcsn_tree_clf.sav', 'rb'))

            data = reqd_preprocess(data)
            print('Preprocessed Data:\n', data)
            data = transform_generate(data)
            print('Transformed Data:\n', data)
            data = drop_features(data)
            print('After drop:\n', data)

            pred = model.predict(data)[0]
            print('Prediction:', pred)
            result = 'Survived' if pred == 1 else 'Died'
            print(f'Result is: {result}')

            return render_template('dt_res.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('titanic.html')


@app.route('/log-res', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_dict = request.form.to_dict()
            print(input_dict)
            input_features = {k.strip(): [float(v)] for k, v in input_dict.items()}
            print(input_features)
            data = pd.DataFrame(input_features)

            cols, model = pickle.load(open('models/log_reg.sav', 'rb'))

            #data = pd.DataFrame({'rate_marriage': [3.0], 'age': [27.0], 'yrs_married': [3.0], 'children': [2.0], 'religious': [3.0], 'educ': [16.0], 'occupation': [3.0], 'occupation_husb': [5.0]})
            data[cols[0]] = 1.0
            data[cols[1:11]] = 0

            for i, j in zip(cols[1:6], cols[6:11]) :
                if float(i[-1]) == data['occupation'].values[0]:
                    data[i] = 1
                elif float(j[-1]) == data['occupation_husb'] .values[0]:
                    data[j] = 1
            else:
                x = data[cols]

            pred = model.predict(x)[0]
            result = 'Yes' if pred == 1 else 'No'
            print(f'Result is: {result}')

            return render_template('log_res.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('affairs.html')


@app.route('/lr-res', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_dict = request.form.to_dict()
            print(input_dict)
            input_features = {k.strip(): [float(v)] for k, v in input_dict.items() if k != 'CHAS'}
            print(input_features)
            data = pd.DataFrame(input_features)

            model = pickle.load(open('models/lr.sav', 'rb'))

            pred = model.predict(data)[0]
            result = pred * 1000
            print(f'Result is: {result}')

            return render_template('lr_res.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('boston.html')

#port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #host = '0.0.0.0'
    # port = 5000
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()