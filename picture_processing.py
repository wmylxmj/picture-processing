# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:56:15 2018

@author: wmy
"""

import numpy
import operator
from os import listdir
import PIL.Image
import matplotlib.pyplot as plt

'''将文本文档中储存的二进制图像转换成一维向量'''
def TxtImageToVector(filename,width,height):
    #创建返回的向量
    returnvector=numpy.zeros((1,(width*height)))
    fr=open(filename)
    for h in range(height):
        linestr=fr.readline()
        for w in range(width):
            returnvector[0,width*h+w]=int(linestr[w])
    return returnvector

'''将图片转换成RGB数组'''
def ImageRGBToVector(filename):
    image=PIL.Image.open(filename)
    returnvector=numpy.array(image)
    return returnvector

'''将图片转为灰度数组并进行二值化处理'''
def ImageBinaryzationToVector(filename):
    #转换成灰度图像
    image=PIL.Image.open(filename).convert('L')
    imagevector=numpy.array(image)
    height,width=imagevector.shape
    for h in range(height):
        for w in range(width):
            if imagevector[h,w]<=128:
                imagevector[h,w]=0
            else:
                imagevector[h,w]=1
    return imagevector

def ArrayToImageShow(dataarray):
    plt.imshow(dataarray)
    plt.axis('off')
    plt.show()
    return 0
                    
def GrayscaleImageShow(dataarray):
    plt.imshow(dataarray,cmap='gray')
    plt.axis('off')
    plt.show()
    return 0

'''把多维度矩阵并为一维向量'''
def MatrixToOneDimension(dataarray):
    returnvector=numpy.array(dataarray)
    returnvector=returnvector.flatten()
    return returnvector

ArrayToImageShow(ImageRGBToVector('17.jpg'))     
GrayscaleImageShow(ImageBinaryzationToVector('17.jpg'))    
print(ImageBinaryzationToVector('17.jpg'))
print(MatrixToOneDimension(ImageBinaryzationToVector('17.jpg')))

x=numpy.array([[1,2],[3,4],[5,6],[7,8]])
print(MatrixToOneDimension(x))
