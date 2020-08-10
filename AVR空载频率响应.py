# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:03:53 2018

@author: ll
"""

import control as ctrl
from matplotlib import pyplot as plt
import numpy as np
import sympy as sp


omega=np.arange(0.1,6,0.001)
sys1 = ctrl.tf([881.903, 5921.35, 12238.7, 7199.21, 0],\
               [1., 63.9469, 1045.37, 5749.19, 7164.41, 2651.41, 288.047]) 



s=sp.Symbol('s')

AVR_Open = 500*(1 + s)/(1 + 10*s)*7.3*1/(1 + 8.45*s)
AVR_Close = AVR_Open/(1 + AVR_Open)
PSS=(5*s)/(1+5*s)*5/(1+3*s)*(1+0.35*s)/(1+0.1*s)*(1+0.35*s)/(1+0.1*s)
AVR_PSS = PSS*AVR_Close

N=10
key=['s'+str(i) for i in np.arange(1,N,0.1)]
value=[i for i in np.arange(1,N,0.1)]
point=dict(zip(key,value))

print(AVR_PSS.evalf(subs=point, n=3))

# 波特图
ctrl.bode(sys1,omega,dB=1,Hz=1)
#plt.xlim(0.1,1)



