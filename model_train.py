from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.metrics import accuracy_score
from joblib import dump, load
import numpy as np

# Train Support Vector Machine model
def train_svm():
    clf = svm.SVC()
    data = load_iris()
    # Unpack data
    X = data.data
    y = data.target_names[data.target]
    # Fit model
    clf.fit(X, y)
    # Check Accurary
    y_predict = clf.predict(X)
    # Export Model
    print('Accurary Score Is: {}' .format(accuracy_score(y, y_predict)))
    dump(clf, 'iris_model.joblib')

# Get average value for each predictor
def get_avg():
    data = load_iris()
    X = data.data
    means = {}
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    for i, feature in enumerate(features):
        means[feature] = np.mean(X[0:, i])
    return means
