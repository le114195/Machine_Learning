import numpy
import math

def openfile():
    dataMat = []; labelMat = []
    fr = open('testSet3.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1.0/(1 + math.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = numpy.mat(dataMatIn)
    labelMat = numpy.mat(classLabels).transpose() #convert to NumPy matrix
    m,n = numpy.shape(dataMatrix)
    alpha = 0.01
    maxCycles = 50
    weights = numpy.ones((n,1))
    h = numpy.ones((m, 1))
    for k in range(maxCycles):              #heavy on matrix operations
        xx = dataMatrix*weights
        for hk in range(m):
            h[hk, 0] = sigmoid(xx[hk, 0])

        error = (labelMat - h)              #vector subtraction
        weights = weights + alpha * dataMatrix.transpose()* error #matrix mult
    return weights

dataMatIn, classLabels = openfile()

hhh = gradAscent(dataMatIn, classLabels)

print('hhh = ', hhh)
