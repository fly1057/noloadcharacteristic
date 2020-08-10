# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:35:44 2018

@author: ll
"""

from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

###############################################################################
#提取Ks2T7数据
#path_str=u"C:/Users/ll/Desktop/KFD791.csv"
path_str=u"C:/Users/ll/Desktop/KFD65.csv"
dir_filename,filetype=path.splitext(path_str) 

df=pd.read_csv(path_str,encoding="gb2312")
t_shice = df.t_shice
t_fangzhen = df.t_fangzhen
shice = df.shice
fangzhen = df.fangzhen

#设定图像大小，像素，去除边框
plt.figure(figsize=(7,4), dpi=100)
ax = plt.gca()
ax.spines['top'].set_visible(False)  #去掉上边框
ax.spines['right'].set_visible(False) #去掉右边框

plt.plot(t_shice,shice,"-",color='k' )
plt.plot(t_fangzhen,fangzhen,":",color='k' )
plt.legend(['实测曲线','KFD=6.5 仿真曲线'])
#plt.legend(['实测曲线','KFD=7.91 仿真曲线'])

plt.xlabel("t /s")
plt.ylabel("Ug /p.u.")

plt.show()