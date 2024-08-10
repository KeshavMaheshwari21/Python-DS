from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import joblib
import sqlite3

# Load the model and scaler
model = tf.keras.models.load_model('models/ann_model.h5')
scaler = joblib.load('models/scaler.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/records')
def records():
    try:
        conn = sqlite3.connect('userdata.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM userecord")
        records = cur.fetchall()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
        records = []

    return render_template('records.html', records=records)

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from form and convert to appropriate types
    try:
        name = request.form.get('name')
        no_of_dependents = float(request.form.get('no_of_dependents', 0))
        income_annum = float(request.form.get('income_annum', 0))
        loan_amount = float(request.form.get('loanAmount', 0))
        loan_term = float(request.form.get('loan_term', 0))
        cibil_score = float(request.form.get('cibil_score', 0))
        residential_assets_value = float(request.form.get('residential_assets_value', 0))
        commercial_assets_value = float(request.form.get('commercial_assets_value', 0))
        luxury_assets_value = float(request.form.get('luxury_assets_value', 0))
        bank_asset_value = float(request.form.get('bank_asset_value', 0))
        
        education = 'Graduate' if request.form.get('education') == 0 else 'Not Graduate'
        self_employed = 'Yes' if request.form.get('self_employed') == 1 else 'No'
        
        education_numeric = 1 if education == 'Graduate' else 0
        self_employed_numeric = 1 if self_employed == 'Yes' else 0
        
        input_data = np.array([[no_of_dependents, income_annum, loan_amount, loan_term, cibil_score,
                                residential_assets_value, commercial_assets_value, luxury_assets_value,
                                bank_asset_value, education_numeric, self_employed_numeric]])

        input_transformed = scaler.transform(input_data)

        prediction = model.predict(input_transformed)

        pred = (prediction > 0.5).astype(int)

        value = int(pred[0][0])
                
    

        if value == 0:
            result = 'Approved'
        else:
            result = 'Rejected'

        # Insert data into database
        conn = sqlite3.connect('userdata.db')
        cur = conn.cursor()
        cur.execute('''
        INSERT INTO userecord (name, no_of_dependents, income_annum, loan_amount, loan_term, 
                               cibil_score, residential_assets_value, commercial_assets_value, 
                               luxury_assets_value, bank_asset_value, education, self_employed, prediction)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, no_of_dependents, income_annum, loan_amount, loan_term, cibil_score,
              residential_assets_value, commercial_assets_value, luxury_assets_value,
              bank_asset_value, education, self_employed, result))
        
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")
        result = 'Error processing your request'

    return render_template('output.html', output=result)

if __name__ == "__main__":
    app.run(debug=True)
