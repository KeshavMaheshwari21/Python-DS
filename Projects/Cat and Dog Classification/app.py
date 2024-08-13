from flask import Flask, request, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = Flask(__name__)

model = tf.keras.models.load_model('models/cnn_model.h5')

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit():
    file = request.files['file']
    
    image = Image.open(file.stream)
    
    image = image.resize((224, 224))
    
    image_array = np.array(image) / 255.0
    
    if len(image_array.shape) == 3:
        image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)
    out = (prediction > 0.5).astype(int).ravel()

    class_names = ['DOG', 'CAT']
    result = class_names[out[0]]

    return render_template('upload.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
