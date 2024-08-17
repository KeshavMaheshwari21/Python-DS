from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

model = joblib.load('./Models/model.lb')
df = pd.read_csv('./x_train.csv')

# Ensure all columns are of the same type
df = df.astype(int)

# Drop any unnecessary columns (e.g., index columns) if present
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction", methods=['POST'])
def prediction():
    status = False
    price = None
    sqft = request.form.get('sqft')
    bath = request.form.get('bath')
    bhk = request.form.get('bhk')
    location = request.form.get('location')

    status = True

    loc_index = np.where(df.columns == location)[0]

    if loc_index.size == 0:
        raise ValueError("Location not found in the dataset.")

    # Ensure the input vector matches the number of features expected by the model
    x = np.zeros(len(df.columns))
    x[0] = float(sqft)
    x[1] = float(bath)
    x[2] = float(bhk)

    if loc_index.size > 0:
        x[loc_index[0]] = 1

    # Ensure the input vector is the correct shape
    x = x[:model.coef_.shape[0]]

    price = model.predict([x])[0] * 100000

    print(price)

    return render_template('project.html', price=int(price), status=status)

if __name__ == "__main__":
    app.run(debug=True)
