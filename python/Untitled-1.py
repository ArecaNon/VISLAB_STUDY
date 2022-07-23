import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()

def Default_AND(x1,x2):
    w1, w2, theta = 0.5,0.5,0.7
    temp = x1*w1+x2*w2
    if temp <= theta:
        return 0
    else: 
        return 1


def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-.5,-.5])
    b = .7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else: 
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([.5,.5])
    b = -.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else: 
        return 1


def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([.5,.5])
    b = -.2
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else: 
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)

    return y
