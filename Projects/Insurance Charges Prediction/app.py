from flask import Flask, render_template, request
import sqlite3
import joblib
import pandas as pd  # pandas is imported but not used; consider removing if unnecessary
from datetime import datetime

current_date = datetime.now()
date = current_date.strftime('%d/%m/20%y')

now = datetime.now()
time = now.strftime("%H:%M")

# Load the model once at the start
model = joblib.load('models/randomforest_model.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/records')
def records():
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM userecord")
    records = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('records.html', records=records)

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()
        
        # Input values
        age = int(request.form['age'])
        bmi = int(request.form['bmi'])
        child = int(request.form['child'])
        gender = int(request.form['gender'])
        smoker = int(request.form['smoker'])
        region = request.form['region']

        # region encoding
        northwest = 0
        southeast = 0
        southwest = 0

        if region == 'northwest':
            northwest = 1
        elif region == 'southeast':
            southeast = 1
        elif region == 'southwest':
            southwest = 1

        unseen_data = [[age, bmi, child, gender, smoker, northwest, southeast, southwest]]

        prediction = model.predict(unseen_data)[0]

        unseen_data_with_prediction = (age, bmi, child, gender, smoker, northwest, southeast, southwest, int(prediction), date, time)

        insert_data_query = """
        INSERT INTO userecord VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(insert_data_query, unseen_data_with_prediction)
        conn.commit()
        cur.close()
        conn.close()

        return render_template('output.html',output = str(int(prediction)))

if __name__ == "__main__":
    app.run(debug=True)