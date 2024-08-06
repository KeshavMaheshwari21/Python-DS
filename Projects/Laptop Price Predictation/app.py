from flask import Flask, render_template, request
import sqlite3
import joblib
import pandas as pd  # pandas is imported but not used; consider removing if unnecessary

# Load the model once at the start
model = joblib.load('laptop_model.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/output')
def satisfy():
    return render_template('output.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        try:
            # Input values
            ram = int(request.form['ram'])
            weight = float(request.form['weight'])  # Convert weight to float if it's a decimal
            screen_type = request.form['screen_type']
            touchscreen = 1 if screen_type == 'touchscreen' else 0
            ips = 1 if screen_type == 'ips' else 0
            
            company = request.form['company']
            companies = ['acer', 'apple', 'asus', 'dell', 'hp', 'lenovo', 'msi', 'toshiba', 'other']
            company_flags = [1 if company == c else 0 for c in companies]

            laptop_type = request.form['laptop_type']
            laptop_types = ['in21', 'gaming', 'netbook', 'notebook', 'ultrabook', 'workstation']
            laptop_flags = [1 if laptop_type == lt else 0 for lt in laptop_types]

            opsys = request.form['opsys']
            os_systems = ['linux', 'mac', 'windows', 'other']
            os_flags = [1 if opsys == os else 0 for os in os_systems]

            cpu = request.form['cpu']
            cpus = ['amd', 'i3', 'i5', 'i7', 'other']
            cpu_flags = [1 if cpu == c else 0 for c in cpus]

            gpu = request.form['gpu']
            gpus = ['amd', 'intel', 'nvidia']
            gpu_flags = [1 if gpu == g else 0 for g in gpus]

            unseen_data = [ram, weight, touchscreen, ips] + company_flags + laptop_flags + os_flags + cpu_flags + gpu_flags

            prediction = model.predict([unseen_data])[0]
            prediction = prediction*91.55
            
            return render_template('output.html', prediction=prediction)  # Pass the prediction to the template

        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
