# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:49:56 2018

@author: ll
"""

import  numpy  as np
import  matplotlib.pyplot  as plt

Uref=np.arange(0.1,1,0.01)
KA=15
Km=4
UFDB=68.66
IFDB=199.9
du=Uref/(1+KA*Km)
Ug=Uref*KA*Km/(1+KA*Km)
Uavr=du*KA
Ufd=Ug
Ufd=Ufd*UFDB
Ifd=Ug*IFDB
