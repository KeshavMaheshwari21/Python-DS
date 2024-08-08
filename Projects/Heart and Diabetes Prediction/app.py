from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('Heart_model.lb')
modeldia = joblib.load('models/Diabetic_model.lb')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/heart_predict', methods=['POST'])
def heart_predict():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])
    
    features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    
    prediction = model.predict(features)[0]
    
    result = 'Unhealthy' if prediction == 1 else 'Healthy'
    
    return render_template('output.html', output = result)

@app.route('/diabetes_predict', methods=['GET', 'POST'])
def diabetes_predict():
    if request.method == 'POST':
    
        # Extract form data
        pregnancies = int(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = int(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        pedigree_function = float(request.form['pedigree_function'])
        age = int(request.form['age'])

        featuresdia = [[pregnancies, glucose, blood_pressure, skin_thickness,
                              insulin, bmi, pedigree_function, age]]
        
        prediction = modeldia.predict(featuresdia)[0]

        result = 'Unhealthy' if prediction == 1 else 'Healthy'

    return render_template('output.html', output=result)


if __name__ == '__main__':
    app.run(debug=True)
