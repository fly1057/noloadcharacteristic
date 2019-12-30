# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:56:22 2017

@author: ll
"""
import numpy as np
from scipy.optimize import least_squares,leastsq
import matplotlib.pyplot as plt

A=np.array([   3.016,   34.798,   67.742,   99.856,  135.215])
B=np.array([ 0.01308,  0.10371,  0.2012 ,  0.30525,  0.41353])

def  residuals(p):
    k,b=p
    return B-(k*A+b)

r=leastsq(residuals,[1,0])
k,b=r[0]
print "k=",k,"b=",b

B_sq=np.linspace(0,1.3,131)
A_sq=(B_sq-b)/k
     
     
plt.plot(A_sq,B_sq,A,B)

##%原始的A，对应IFD，有名值, A减去零漂
#A_temp=A-np.linspace(1,1,np.size(A))*min(A)
#
##%原始的B，对应UAB，标幺值
#if B[-1]>2:
#    B=B/100
#
#B_temp=B-np.linspace(1,1,np.size(B))*min(B)
#
##%Kair即为直线的斜率
#[Kair,cost,] = lsq_linear(A_temp, B_temp, bounds=(-np.inf, np.inf),method='trf', lsmr_tol='auto', verbose=1)
#
#
#
#B_sq=np.linspace(0,1.3,131)
#A_sq=(B_sq-np.linspace(1,1,np.size(B))*min(B))/Kair+np.linspace(1,1,np.size(B))*min(A)
#
#A10=np.linspace(1,1,np.size(A))*(  (1-min(B))/Kair+min(A)   )
#A12=np.linspace(1,1,np.size(A))*(  (1.2-min(B))/Kair+min(A)   )





