from flask import Flask, redirect, url_for, render_template, request, jsonify
import math
from joblib import load
import numpy as np
import pandas as pd

app = Flask(__name__)


# Load Model Pipeline files
impute_knn_loaded = load('knn_imputer.joblib') 
xReg_model_loaded = load('xg_regressor.joblib') 

result = -1

def get_pred(crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat):
    """ Helper Function to get prediction """
    og_X_column = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
     'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    x_feature_list = [ crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]
    x_feature_list_np = np.asarray(x_feature_list)
    x_feature_list_np.reshape(1, -1)

    x_tester_feature = impute_knn_loaded.fit_transform([x_feature_list_np])
    x_tester_feature = pd.DataFrame(x_tester_feature,columns=og_X_column)


    predicted_val = xReg_model_loaded.predict(x_tester_feature)
    return predicted_val


@app.route("/", methods=["POST", "GET"])
def homepage():
    """Handles requests to get text inputs from webpage and
    calculates the prediction value and redirects user"""
    if request.method == "POST":
        crim = request.form["CRIM"]
        zn = request.form["ZN"]
        indus = request.form["CRIM"]
        chas =   1 if "CHAS" in request.form else 0
        indus = request.form["INDUS"]
        nox = request.form["NOX"]
        rm = request.form["RM"]
        age = request.form["AGE"]
        dis = request.form["DIS"]
        rad = request.form["RAD"]
        tax = request.form["TAX"]
        ptratio = request.form["PTRATIO"]
        b = request.form["B"]
        lstat = request.form["LSTAT"]

        x_feature_list = [ crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]

        result = get_pred(crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat)
        return render_template(
            "output.html", result=result)
    else:
        return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def prediction_api():
    """Provides an API endpoint to input features from a json body
    and returns the predicted median value for those input features in JSON format"""
    if request.method == "POST":
        data = request.get_json()

        try:
            crim = data["CRIM"]
            zn = data["ZN"]
            indus = data["INDUS"]
            chas = data["CHAS"]
            nox = data["NOX"]
            rm = data["RM"]
            age = data["AGE"]
            dis = data["DIS"]
            rad = data["RAD"]
            tax = data["TAX"]
            ptratio = data["PTRATIO"]
            b = data["B"]
            lstat = data["LSTAT"]
        except KeyError:
            return jsonify({"Error": "Invalid JSON Input!!"})


        try:
            predicted_val = get_pred(crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat)
            return jsonify({"Predicted Value": str(predicted_val[0])})
        except:
            return jsonify({"Error": "An error occurred during prediction. Please check inputs again!!"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)