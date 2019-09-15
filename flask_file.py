from flask import *
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image as image_utils
from PIL import Image
import requests
from io import BytesIO

app=Flask(__name__)

app.config['UPLOAD_FOLDER']="/home/Desktop/VIT/'Aarush Hackathon'/SeeFood"
img_width, img_height = 128, 128
model_path = './models/model3.h5'
model_weights_path = './models/weights3.h5'
model = load_model(model_path)
model._make_predict_function()
model.load_weights(model_weights_path)

@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/render_blog')
def render_blog():
    return render_template("blog.html")

@app.route('/write_blog')
def write_blog():
    return render_template("writeblog.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/history')
def history():
    return render_template("history.html")

@app.route('/loginsignup')
def loginsignup():
    return render_template("loginsignup.html")

@app.route('/redeem')
def redeem():
    return render_template("redeem.html")

@app.route('/getcoupons')
def getcoupons():
    return render_template("getcoupons.html")

@app.route('/take', methods=['GET', 'POST'])
def take():
    if(request.method=='POST'):
        if request.files:
            print("Thank you for choosing a image!")
            f = request.files['photo']
            f.save(f.filename)

            test_image = Image.open(open(f.filename,'rb'))
            test_image = test_image.resize((128,128))  
            test_image = image_utils.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)

            result = model.predict_on_batch(test_image)
            print (result)

            if result[0][0] == 1:
                ans = 'Biriyani'
            elif result[0][1] == 1:
                ans = 'Naan'
            elif result[0][2] == 1:
                ans = 'Dosa'
            elif result[0][3] == 1:
                ans = 'Idly'
            elif result[0][4] == 1:
                ans = 'Medhu Vada'
            
            if ans=='Idly':
                return render_template("idly_page.html")
            elif ans=='Dosa':
                return render_template("dosa_page.html")
            elif ans=='Medhu Vada':
                return render_template("vada_page.html")
            elif ans=='Naan':
                return render_template("naan_page.html")
            elif ans=='Biriyani':
                return render_template("biriyani_page.html")
                
        else:
            return 'No File Uploaded'

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)