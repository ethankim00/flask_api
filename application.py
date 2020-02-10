# using flask_restful
import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from model_train import train_svm, get_avg
from joblib import dump, load
import numpy as np

# If model does not exist, train model
if not os.path.isfile('iris_model.joblib'):
    train_svm()

# Load Model
svm_model = load('iris_model.joblib')

def get_prediction(measurements):
    return clf.predict(measurements)[0]

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        # Get mean value for each predictor
        means = get_avg()
        features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        values = {}
        # If a predictor is not in the request replace it with its mean in the training data
        counter = 0
        for feature in features:
            if not feature in data:
                values[feature] = means[feature]
                counter += 1
            else:
                values[feature]= data[feature]

        # Raise Error if All values are missing
        if counter == len(features):
            return jsonify({
                'Error': 'Input should be 4 numeric values for sepal_length, sepal_width, petal_length and petal_width'
            })
        # Make prediction using imported model
        prediction = svm_model.predict([[values['sepal_length'], values['sepal_width'], values['petal_length'], values['petal_width']]])[0]

        return jsonify({
            'Prediction': prediction
        })

api.add_resource(Prediction, '/predict')

if __name__ == '__main__':

    app.run(debug = True)
