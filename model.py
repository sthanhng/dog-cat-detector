import json

import tensorflow as tf
import numpy as np
import requests

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

SIZE=128
MODEL_URI='http://localhost:8501/v1/models/pets:predict'
CLASSES = ['cat', 'dog']


def get_prediction(image_path):
    image = load_img(image_path, target_size=(SIZE, SIZE))
    image = img_to_array(image)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    data = json.dumps({
        'instances': image.tolist()
    })

    response = requests.post(MODEL_URI, data=data.encode('utf-8'))
    result = json.loads(response.text)

    prediction = np.squeeze(result['predictions'][0])
    class_name = CLASSES[int(prediction > 0.5)]

    return class_name
