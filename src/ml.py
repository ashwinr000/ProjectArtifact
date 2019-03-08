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
    data = []
    labels = []
    for filename in os.listdir("/Users/erichu/Desktop/ProjectArtifact/images/" + civ + "/"):
        if filename.endswith(".jpg"):
            file_name = os.path.join(
                "/Users/erichu/Desktop/ProjectArtifact/images/" + civ + "/", filename)
            print(file_name)
            img = cv2.imread(file_name, 10)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            arr = np.array(gray)
            arr = arr / 255.0
            print(len(arr))
            arr = arr.reshape(500, 500, 1)
            data.append(arr)
            labels.append(i)
    train_data.append(data[:40])
    test_data.append(data[40:])
    train_labels.append(labels[:40])
    test_labels.append(labels[40:])
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
    keras.layers.Flatten(input_shape=(500, 500, 1)),
    keras.layers.Dense(500, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_data, train_labels, epochs=150)

test_loss, test_acc = model.evaluate(test_data, test_labels)

print('Test accuracy:', test_acc)
