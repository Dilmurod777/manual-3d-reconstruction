import cv2
# import keras.models
import numpy as np

# from model import create_model, MODEL_CHECKPOINT_PATH, test_model, train_model, MODEL_PATH
# import tensorflow as tf
# import os
# import logging

# tf.get_logger().setLevel(logging.ERROR)
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

filename = 'cube.png'

image = cv2.imread('./data/' + filename)
w, h, c = image.shape
# resize to have width = WIDTH
WIDTH = 224
image = cv2.resize(image, (WIDTH, WIDTH * w // h))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

color = np.uint8([[[0, 0, 0]]])  # white
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# identify blue color region
lower = np.array([60, 35, 140])
upper = np.array([180, 255, 255])

# identify white color
# lower = hsv_color[0][0][0] - 10, 100, 100
# upper = hsv_color[0][0][0] + 10, 255, 255
# lower = np.array(lower)
# upper = np.array(upper)

mask = cv2.inRange(hsv_image, lower, upper)

result = cv2.bitwise_and(image, image, mask=mask)

# apply gaussian blur
kernel = np.ones((3, 3), np.float32) / 9
result = cv2.filter2D(result, -1, kernel)

# save masked image
output_filename = filename.split('.')[0] + '_output.' + filename.split('.')[1]
cv2.imwrite("./data/" + output_filename, result)

# detect edges
edges = cv2.Canny(image=result, threshold1=100, threshold2=200)

# model
# model = train_model()

result = cv2.resize(result, (224, 224))

# test = cv2.imread('./data/mechanical_components_dataset/bolt/00_09_0101_0100_0400_4.png')
# print(test.shape)
# model = keras.models.load_model(MODEL_PATH)
# model.summary()
#
# labels = os.listdir('./data/mechanical_components_dataset/')
#
# predictions = model.predict(np.asarray([result]), verbose=2)
# print(labels[predictions.argmax()])

# show output
cv2.imshow('hsv', hsv_image)
cv2.imshow('gray', gray)
cv2.imshow('canny', edges)
cv2.imshow('result', result)
cv2.waitKey(0)

# cv2.destroyAllWindows()
