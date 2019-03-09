import os
import keras
import tensorflow as tf
import cv2
import numpy as np

train_data = []
train_labels = []
test_data = []
test_labels = []
i = 0

civ_labels = ["Australia", "Aztec", "Cherokee", "Chinese", "Egypt", "Indian", "Seminole", "Zulu"]

def pullImages(civ):
    j = 0
    for filename in os.listdir("/Users/ashwinr/Downloads/ProjectArtifact/images/" + civ + "/"):
        if filename.endswith(".jpg"):
            file_name = os.path.join(
                "/Users/ashwinr/Downloads/ProjectArtifact/images/" + civ + "/", filename)
            img = cv2.imread(file_name, 10)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            arr = np.array(gray)
            arr = arr / 255.0
            arr = arr.reshape(500, 500)
            if j < 40:
                train_labels.append(i)
                train_data.append(arr)
            else:
                test_labels.append(i)
                test_data.append(arr)
            global j
            j += 1
    global i
    i += 1


pullImages("Australia")
pullImages("Aztec")
pullImages("Cherokee")
pullImages("Chinese")
pullImages("Egypt")
pullImages("Indian")
pullImages("Seminole")
pullImages("Zulu")

train_data = np.array(train_data)
train_labels = np.array(train_labels)
test_data = np.array(test_data)
test_labels = np.array(test_labels)


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(500, 500)),
    keras.layers.Dense(500, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.softmax)
])

model.compile(keras.optimizers.Adam(lr=1e-5),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_data, train_labels, epochs=50)

test_loss, test_acc = model.evaluate(test_data, test_labels)

print('Test accuracy:', test_acc)