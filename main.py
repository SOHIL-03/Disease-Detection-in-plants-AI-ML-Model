# Download Data set and model from -> https://drive.google.com/drive/folders/1mmQ8qVRLhxxgIG1qCWIAsDNwyb6xa4fQ?usp=share_link


from flask import *
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.preprocessing import image
import traceback

import tensorflow as tf
import cv2
import os
import numpy as np



model = tf.keras.models.load_model("Trained_final.h5")
ref = {0: 'Apple scab',
       1: 'Apple Black Rot',
       2: 'Apple Cedar(Apple rust)',
       3: 'Healthy Apple',
       4: 'Not a leaf',
       5: 'Healthy Blueberry',
       6: 'Cherry Powdery Mildew',
       7: 'Healthy Cherry',
       8: 'Corn Cercospora Leaf spot (Gray Leaf Spot)',
       9: 'Corn Common Rust',
       10: 'Corn Northern Leaf Blight',
       11: 'Healthy Corn',
       12: 'Grape Black Rot',
       13: 'Grape Esca (Black_Measles)',
       14: 'Grape Leaf Blight (Isariopsis_Leaf_Spot)',
       15: 'Healthy Grape',
       16: 'Orange Haunglongbing (Citrus_greening)',
       17: 'Peach Bacterial Spot',
       18: 'Healthy Peach',
       19: 'Bell Pepper (Bacterial spot)',
       20: 'Healthy Bell Pepper',
       21: 'Potato Early Blight',
       22: 'Potato Late Blight',
       23: 'Healthy Potato',
       24: 'Healthy Raspberry',
       25: 'Healthy Soybean',
       26: 'Squash Powdery Mildew',
       27: 'Strawberry Leaf Scorch',
       28: 'Healthy Strawberry',
       29: 'Tomato Bacterial Spot',
       30: 'Tomato Early Blight',
       31: 'Tomato Late Blight',
       32: 'Tomato Leaf Mold',
       33: 'Tomato Septoria Leaf Spot',
       34: 'Tomato Spider Mites (Two-spotted Spider Mite)',
       35: 'Tomato Target Spot',
       36: 'Tomato Yellow Leaf Curl-Virus',
       37: 'Tomato Mosaic Virus',
       38: 'Healthy Tomato'}



def prediction(path):
    img = load_img(path,target_size=(256,256))
    i=image.img_to_array(img)
    im = preprocess_input(i)
    img = np.expand_dims(im,axis=0)
    pred = np.argmax(model.predict(img))
    # main(ref[pred])
    return render_template('/uploadimage.html',result=(ref[pred]))




app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/uploadimage')
def main():
    return render_template('/uploadimage.html')

@app.route('/Image')
def Image():
    return render_template("/image.html")

@app.route('/apple')
def apple():
    return render_template("/apple.html")


@app.route('/BlueBerry')
def BlueBerry():
    return render_template("/BlueBerry.html")

@app.route('/Cherry')
def Cherry():
    return render_template("/Cherry.html")

@app.route('/Corn')
def Corn():
    return render_template("/Corn.html")


@app.route('/Grapes')
def Grapes():
    return render_template("/Grapes.html")


@app.route('/Orange')
def Orange():
    return render_template("/Orange.html")


@app.route('/Peach')
def Peach():
    return render_template("/Peach.html")


@app.route('/Pepper')
def Pepper():
    return render_template("/Pepper.html")


@app.route('/Rasberry')
def Rasberry():
    return render_template("/Rasberry.html")


@app.route('/Potato')
def Potato():
    return render_template("/Potato.html")


@app.route('/Soyabean')
def Soyabean():
    return render_template("/Soyabean.html")


@app.route('/Squash')
def Squash():
    return render_template("/Squash.html")


@app.route('/', methods=['POST'])
def third():
    try:
        if 'file' in request.files and request.files['file'] and request.files['file'].filename != '':
            s=""
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(filename)
            result = prediction(filename)
            os.remove(filename)
            # flash("you are successfuly logged in")  
            
            return result
        else:
            return "File Not found"
    except Exception:
        print(traceback.format_exc())
        return "Error 404"


if __name__ == "__main__":
    app.run(port=8080, debug=True, host="0.0.0.0", threaded=True,
            use_reloader=True, passthrough_errors=True)
