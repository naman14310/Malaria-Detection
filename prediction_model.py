import os
import random
import numpy as np
from keras.models import load_model
from keras.preprocessing import image


def get_results(img_name):
    imgPath = "./static/"+img_name
    imag = image.load_img(imgPath,target_size = (112,112))
    imag = image.img_to_array(imag)
    imag = np.expand_dims(imag,axis=0)
    imag = imag/255
    model = load_model('malaria_detection_model.h5')
    prob = model.predict(imag)

    if prob > 0.5:
        return "uninfected"
    else:
        return str((1-prob[0][0])*100)[:5]+"% prediction accuracy"
