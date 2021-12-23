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

cols, model = pickle.load(open('dcsn_tree_clf.sav', 'rb'))

app = Flask(__name__)
#CORS(app)


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_dict = request.form.to_dict()
            print(input_dict)
            input_features = {k.strip(): [float(v)] for k, v in input_dict.items()}
            print(input_features)
            data = pd.DataFrame(input_features)

            data = reqd_preprocess(data)
            data = transform_generate(data)
            data = drop_features(data)

            pred = model.predict(data)[0]
            result = 'Survived' if pred == 1 else 'Died'
            print(f'Result is: {result}')

            return render_template('result.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('index.html')

#port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #host = '0.0.0.0'
    # port = 5000
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()