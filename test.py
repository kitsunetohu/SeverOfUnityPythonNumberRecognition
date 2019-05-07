from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

from keras import models
from keras import layers
import matplotlib.pyplot as plt
import json
import numpy as np
import cv2
import pickle
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])

img=test_images[0]
plt.imshow(img)
plt.show()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


#获取训练好的网络
with open('trainedData', 'rb') as f:
    network=pickle.load(f)


#network.fit(train_images, train_labels, epochs=5, batch_size=128)
#test_loss, test_acc = network.evaluate(test_images, test_labels)
#print('test_acc:', test_acc)


img=img.reshape((1,28*28))
y=network.predict(img)
print(y)