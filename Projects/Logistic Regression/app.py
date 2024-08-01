from flask import Flask, render_template, request
import sqlite3
import joblib
import pandas as pd  # pandas is imported but not used; consider removing if unnecessary

# Load the model once at the start
model = joblib.load('logisticRegression.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/satisfy')
def satisfy():
    return render_template('satisfy.html')

@app.route('/dissatisfy')
def dissatisfy():
    return render_template('dissatisfy.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()
        
        # Input values
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])
        inflight_entertainment = int(request.form['inflight-entertainment'])
        baggage_handling = int(request.form['baggage-handling'])
        cleanliness = int(request.form['cleanliness'])
        departure_delay = int(request.form['departure_delay'])
        arrival_delay = int(request.form['arrival_delay'])
        gender = int(request.form['gender'])
        customer_type = int(request.form['customer-type'])
        travel_type = int(request.form['travel-type'])
        class_type = request.form['class-type']

        # Class type encoding
        class_eco = 1 if class_type == 'Economy' else 0
        class_eco_plus = 1 if class_type == 'Economy-Plus' else 0

        unseen_data = [[age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,
                        departure_delay, arrival_delay, gender, customer_type, travel_type, class_eco, class_eco_plus]]

        prediction = model.predict(unseen_data)[0]

        unseen_data_with_prediction = (age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,
                                       departure_delay, arrival_delay, gender, customer_type, travel_type, class_eco, class_eco_plus, int(prediction))

        insert_data_query = """
        INSERT INTO userecord VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(insert_data_query, unseen_data_with_prediction)
        conn.commit()
        cur.close()
        conn.close()

        labels = {1: "SATISFIED", 0: "DISATISFIED"}
    
        if int(prediction) == 0:
            return render_template('dissatisfy.html')
        
        else:
            return render_template('satisfy.html')

if __name__ == "__main__":
    app.run(debug=True)
