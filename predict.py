import pickle
import numpy as np
from PIL import Image
IMG_SIZE = (64,64)

with open("model.pkl","rb") as file:
    model = pickle.load(file)



def predict_img(filepath):
    image = Image.open(filepath).convert("RGB")
    image = image.resize(IMG_SIZE)
    
    test = np.array(image).flatten().reshape(1, -1)
    return model.predict(test)[0]

if __name__ == "__main__":
    prediction = predict_img("testimage1.jpg")
    print(prediction)