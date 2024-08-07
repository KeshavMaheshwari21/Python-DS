from flask import Flask, render_template, request
import joblib
import re

model = joblib.load('Models/Multinomial_Model.lb')
bow_obj = joblib.load('Models/countvectorizer.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        emailContent = request.form.get('emailContent', '')
        emailContent = emailContent.lower()
        emailContent = re.sub(r'[^a-zA-Z ]', '', emailContent)

        emailContent_transformed = bow_obj.transform([emailContent])
        prediction = model.predict(emailContent_transformed)[0]

        labels = {'1': "SPAM", '0': "HAM"}
        result = labels.get(str(prediction))

        return render_template('output.html', output=result)

if __name__ == "__main__":
    app.run(debug=True)
