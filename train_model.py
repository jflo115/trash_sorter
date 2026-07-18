import os
import numpy as np
from PIL import Image
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

items = []  #x axis
output = []     # y axis

IMG_SIZE = (64,64)

data_path = "train" 
labels = ["trash", "recycling"]

for label in labels:
    folder = os.path.join(data_path,label)
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        try:
                image = Image.open(filepath).convert("RGB")
                image = image.resize(IMG_SIZE)

                image_array = np.array(image).flatten()

                items.append(image_array)
                output.append(label)

        except Exception as e:
                print("file not found")
                print(e)


#Train Model
model = svm.SVC(kernel = "linear")
model.fit(items, output)

# Save Model
with open("model.pkl","wb") as file:
    pickle.dump(model,file)
print("Model Saved")
