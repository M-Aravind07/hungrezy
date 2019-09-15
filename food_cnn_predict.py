
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

#load model
img_width, img_height = 128, 128
model_path = './models/model3.h5'
model_weights_path = './models/weights3.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

#Prediction on a new picture
from keras.preprocessing import image as image_utils

from PIL import Image,ImageTk
import requests
from io import BytesIO
from tkinter import Tk,Label,Canvas,NW,Entry,Button
url = ''
window = Tk()
window.title("Hungrezy") 
window.geometry('800x600')
lbl = Label(window, text="Enter the URL of the image", font=("Helvetica", 16))
lbl.pack()

def clearinput():
    User_input.delete(0,'end')

def clicked(): 
    global url
    lbl.configure()
    url  = (User_input.get())
    #print(url)
    response = requests.get(url)
    test_image = Image.open(BytesIO(response.content))
    put_image = test_image.resize((400,400)) 
    test_image = test_image.resize((128,128))  
    img = ImageTk.PhotoImage(put_image)
    pic = Label(image=img)
    pic.pack()
    pic.image = img
    test_image = image_utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    
 
    result = model.predict_on_batch(test_image)
    #sprint (result)

    if result[0][1] == 1:
        ans = 'Naan'
    elif result[0][0] == 1:
        ans = 'Biriyani'
    elif result[0][2] == 1:
        ans = 'Dosa'
    elif result[0][3] == 1:
        ans = 'Idly'
    elif result[0][4] == 1:
        ans = 'Medhu Vada'
    
    print (ans)
    out = Label(window, text  = 'Predicted answer : ' +  ans, font=("Helvetica", 16))
    out.pack()

User_input = Entry(width = 100)
User_input.pack()
btn = Button(window, text="Detect Image", font=("Helvetica", 12), command=clicked)
btn.pack()

clearbutton = Button(window, text="Clear", font=("Helvetica",12),command=clearinput)
clearbutton.pack()
window.mainloop()

''' https://d3tfnts8u422oi.cloudfront.net/386x386/lakshmi-vasanth149254462958f66c75899dd.jpg- Medhu Vadai'''
''' https://www.vegrecipesofindia.com/wp-content/uploads/2013/09/vada-medu-vada-recipe-1.jpg - Medu Vadai'''
'''https://i.ytimg.com/vi/ClIZM5gBoMo/maxresdefault.jpg - Medhu Vadai''' 

'''https://www.archanaskitchen.com/images/archanaskitchen/0-Archanas-Kitchen-Recipes/2016/1-Archana/Homemade_Butter_Naan_Recipe_Soft_Yogurt_Bread-1.jpg - Butter Naan'''
'''https://media.chefdehome.com/650/0/0/naan-bread/yeast-naan-bread-chefdehome-10.jpg'''

'''https://c.ndtvimg.com/3jbsmmp_dosa_625x300_30_August_18.jpg- Dosa'''
'''https://www.vegrecipesofindia.com/wp-content/uploads/2018/10/dosa-recipe-1a-500x375.jpg - Dosa'''

'''https://i.ytimg.com/vi/d4Ca8wNwozM/maxresdefault.jpg -Idly'''
'''https://1.bp.blogspot.com/-HythLcEPEEU/USox8fIPrzI/AAAAAAAABso/OVh15nZyfwA/s1600/1-2013-02-23+21.07.14.jpg - Idly'''

'''https://vaya.in/recipes/wp-content/uploads/2018/03/Ambur-Chicken-Biriyani.jpg - Biriyani'''
'''https://b.zmtcdn.com/data/pictures/0/18782910/734fb3d548385a778657e79551f3b71a_featured_v2.jpg - Biriyani'''
