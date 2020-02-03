# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:46:13 2019

@author: Munire
"""

#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#load dataset
#dataset overview
#Now  we have 2 numpy files X.npy and Y.npy. So we need to load them.

dataset1=np.load('X.npy')
print(dataset1)

dataset2=np.load('Y.npy')
print(dataset2)
#Determine to variables
imageSize=64
#We can shown as in the figure.For example we want to see what is in the 12. data. 
#If you run it, you can see "3" digit data with the fingers of hand in the 12. data.
plt.imshow(dataset1[12].reshape(imageSize,imageSize))
plt.title("12. image")
#Now, we do not want to see the with axises.(Optional)
plt.axis("off")
#Now if we see the X.npy and Y.npy dataset. X.npy dataset (2062,64,64), Y.npy dataset is (2062,10).
#For 0: [0:204]
#For 1: [204:409]
#For 2:[409:615]
#♣For 3:[615:822]
#◘For 4:[822:1028]
#For 5: [1028:1236]
#For 6:[1236:1443]
#For 7:[1443:1649]
#For 8:[1649:1855]
#For 9[1855:2062]
#dataset2=dataset2.reshape(2062,1)
print("Dimension of Dataset1:" + str(dataset1.ndim))
print("Dataset1 shape:" +str( dataset1.shape))
print("Dataset2 shape:"+ str(dataset2.shape))
#training and testing data
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest=train_test_split(dataset1,dataset2, test_size=0.15, random_state=42)
trainNumber=Xtrain.shape[0]
testNumber=Ytest.shape[0]
trainNumber2=Ytrain.shape[0]
testNumber2=Xtest.shape[0]
print("Xtrain Number: " + str(trainNumber) + "Xtrain shape: " + str(Xtrain.shape))
print("Ytest Number:" + str(testNumber) + "Ytest shape: " + str(Ytest.shape))
print("Ytrain Number:" + str(trainNumber2) + "Ytrain shape: " + str(Ytrain.shape))
print("Xtest Number:" + str(testNumber2) + "Xtest shape: " + str(Xtest.shape))

#Normalizationing Data; convert to gray scale: between 0 and 1
print("Normalization")
Xtrain=Xtrain/255.0
Xtest=Xtest/255.0
Ytrain=Ytrain/255.0
Ytest=Ytest/255.0
#Reshape Data because of the Keras rules
#-1?
Xtrain=Xtrain.reshape(-1,64,64,3)
Xtest=Xtest.reshape(-1,64,64,1)
Ytrain=Ytrain.reshape(-1,10,1)
print("Xtrain shape: " , Xtrain.shape)
print("Xtest shape: ",Xtest.shape)
print("Ytrain shape: ",Ytrain.shape)
print("Ytest shape: ",Ytest.shape)
#Label Encoding
from keras.utils.np_utils import to_categorical
Ytrain=to_categorical(Ytrain,num_classes=10)

#Train and Test Split
#CNN-Same Padding
#CNN-Max Pooling
#Flattening
#Full Connection
#Create Model
#Define Optimizer
#Compile Model
#Epochs and Batch Size
#Data Augmentation
#Fit the Model
#Evaluate the Model