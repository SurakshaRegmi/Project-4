
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

application = Flask(__name__)
app = application

# Load the pickled model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Define the list of feature names
feature_names = ['step', 'amount', 'oldbalanceOrg', 'oldbalanceDest', 'newbalanceDest',
       'hour', 'day', 'trans_weight', 'type_CASH_OUT', 'type_TRANSFER',
       'Destination']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form[feature_name]) for feature_name in feature_names]
    prediction = model.predict([features])[0]
    prediction_percentage = model.predict_proba([features])[0][1] * 100

    return render_template('index.html', prediction=f'Class: {prediction}, Confidence: {prediction_percentage:.2f}%')

if __name__ == '__main__':
    app.run(debug=True)
