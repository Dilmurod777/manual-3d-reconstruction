import random

import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.models import Sequential
from keras.utils import image_utils
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import logging

tf.get_logger().setLevel(logging.ERROR)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

MODEL_CHECKPOINT_PATH = './checkpoints/cnn'
MODEL_PATH = './models/cnn'


def create_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
	model.add(MaxPool2D((2, 2)))
	model.add(Conv2D(128, (3, 3), activation='relu'))
	model.add(MaxPool2D((2, 2)))
	model.add(Conv2D(128, (3, 3), activation='relu'))
	model.add(Flatten())
	model.add(Dense(64, activation='relu'))
	model.add(Dense(4, activation='softmax'))
	
	model.compile(optimizer='adam', loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
	return model


def train_model():
	path = './data/mechanical_components_dataset/'
	ratio = 0.8
	images = {}
	labels = set()
	for fName in os.listdir(path):
		images[fName] = []
		labels.add(fName)
		for imagePath in os.listdir(path + fName):
			images[fName].append(path + fName + '/' + imagePath)
	labels = list(labels)
	
	train_images = []
	train_labels = []
	for label in labels:
		label_images = images[label]
		label_images = label_images[:int(len(label_images) * ratio)]
		for imagePath in label_images:
			image = cv2.imread(imagePath)
			image = cv2.resize(image, (224, 224))
			train_images.append(np.asarray(image) / 255.0)
			train_labels.append([labels.index(label)])
	
	train_images = np.asarray(train_images)
	train_labels = np.asarray(train_labels)
	
	test_images = []
	test_labels = []
	for label in labels:
		label_images = images[label]
		label_images = label_images[int(len(label_images) * ratio):]
		for imagePath in label_images:
			image = cv2.imread(imagePath)
			image = cv2.resize(image, (224, 224))
			test_images.append(np.asarray(image) / 255.0)
			test_labels.append([labels.index(label)])
	
	test_images = np.asarray(test_images)
	test_labels = np.asarray(test_labels)
	
	model = create_model()
	history = model.fit(train_images, train_labels, epochs=10,
						validation_data=(test_images, test_labels))
	
	model.save(MODEL_PATH)
	
	plt.plot(history.history['accuracy'], label='accuracy')
	plt.plot(history.history['val_accuracy'], label='val_accuracy')
	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.ylim([0.5, 1])
	plt.legend(loc='lower right')
	
	return model


def test_model(model):
	path = './data/mechanical_components_dataset/'
	images = {}
	ratio = 0
	labels = set()
	for fName in os.listdir(path):
		images[fName] = []
		labels.add(fName)
		for imagePath in os.listdir(path + fName):
			images[fName].append(path + fName + '/' + imagePath)
	labels = list(labels)
	
	test_images = []
	test_labels = []
	for label in labels:
		label_images = images[label]
		label_images = label_images[int(len(label_images) * ratio):]
		for imagePath in label_images:
			image = cv2.imread(imagePath)
			image = cv2.resize(image, (224, 224))
			test_images.append(np.asarray(image) / 255.0)
			test_labels.append([labels.index(label)])
	
	test_images = np.asarray(test_images)
	test_labels = np.asarray(test_labels)
	
	loss, acc = model.evaluate(test_images, test_labels, verbose=2)
	print(f'restored model, accuracy: {100 * acc:5.2f}')
