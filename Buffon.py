# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:23:04 2020

@author: ADIV
"""

import matplotlib.pyplot as plt
import numpy as np

rataX = []
rataY = []
def Buffon_Needle(l,d,n):
    
    intersection = 0
    for i in range(n):
        sudut = np.random.uniform(0,np.pi/2)
        x = np.random.uniform(0,d)
        if x <= l * np.cos(sudut):
            intersection += 1
        
    return intersection/n

def mean(n):
    l = 4
    d = 5
    rata_pi = 2*l /(Buffon_Needle(l,d,n)*d)
    return rata_pi

x = np.arange(100,10000,100)
y = np.zeros(len(x))
n = len(x)

for i in range(n):
    y[i] = mean(x[i])
    rataX.append(x[i])
    rataY.append(y[i])

rata_rata = sum(y)/n
    
plt.scatter(x,y)
plt.plot(rataX,rataY,'r')
plt.axhline(y = rata_rata, color = 'g', linestyle = '-')
plt.xlabel('N [Ukuran sampel]')
plt.ylabel('$\pi$')
plt.legend(['$\pi$ eksak','rata-rata seluruh sampel','Metode MC'],loc = 'best')
plt.show()

print('Nilai Phi : ',rata_rata)



    
    
        




