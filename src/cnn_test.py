# -*- coding: utf-8 -*-
"""cnn_test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14UbQkCeOPjeUlM_DPV8sb6YR9ngdAu5B
"""

from google.colab import drive
drive.mount('/content/drive')

import argparse
import cv2,time
import numpy as np
import sys
from scipy import misc
import matplotlib.pyplot as plt

def test(path):
  	
  imge=cv2.imread(path,1)		
  imge = cv2.resize(imge, (28,28)) #to fit the image to the model

  lower_reso = cv2.resize(imge, (28,28))
  gray_scale = cv2.cvtColor(lower_reso,cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray_scale,(3,3),0)
  retval, threshold = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)

  plt.subplot(121),plt.imshow(imge),plt.title('Original')
  plt.xticks([]), plt.yticks([])
  plt.subplot(122),plt.imshow(threshold),plt.title('Preprocessed Image')
  plt.xticks([]), plt.yticks([])
  plt.show()

  
  from keras.models import load_model
  model = load_model('/content/drive/My Drive/apps/cnn.h5')
  
  threshold=np.reshape(threshold,(-1,28,28,1))
  predictions=model.predict_classes(threshold)
  print(predictions[0])
  label = ''
  label = "even" if predictions[0] %2 == 0 else "odd"
  print("The label is: ", label)
 

while True:
  path = input("\nPlease enter file path or press esc or q for exit: ")
  #print(keyboard.is_pressed('q'))
  if path == 'q':
       print("\n\nProgram Terminated")
       break
  else:
       test(path)