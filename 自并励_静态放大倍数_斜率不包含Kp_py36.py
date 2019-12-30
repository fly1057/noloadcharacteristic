# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:37:09 2017
@author: ll
变量定义：
df    dataFrame结构数据，通过pandas直接读取CSV数据
Ug    对应CSV中的Ug，机端电压
Uref  对应CSV中的Uref，机端电压给定参考值
dU    对应CSV中的Uref-UAB
UFD   对应CSV中的UFD，励磁电压
IFD   对应CSV中的IFD，励磁电流
Uavr  对应CSV中的Uavr，对应控制电压Uk，也就是cosα的值
IFDB  对应CSV中的IFDB，从气隙线上得到的基准励磁电流
UFDB  对应CSV中的UFDB，从气隙线上得到的基准励磁电压
UTN   对应CSV中的UTN，励磁变额定低压侧电压（这里取了低压侧值）
STN   对应CSV中的STN，励磁变额定容量
Utk   对应CSV中的Utk，励磁变短路阻抗
UFN   对应CSV中的UFN，额定励磁电压
IFN   对应CSV中的IFN，额定励磁电流
RFDB  对应CSV中的RFDB，额定励磁基准阻抗
k     对应CSV中的k，即直线斜率
h     对应CSV中的h，即直线截距
UL    对应CSV中的h，即当前的励磁变低压侧阳极电压（在他励方式下是定值）
PID_P 对应CSV中的PID_P，即PID的比例系数
原理

思路：
1、确保CSV表中的数据都是标幺化的
2、通过线性最小二乘拟合线性段的ΔU*KA*KFD*UL=UFD+IFD*Xc   (均为标幺值表示)，
即ΔU*KFD=( UFD+IFD*(3/π*Uk%*UTN^2/STN) )/UFDB/KA*UTN/UL
3、画图并保存
"""
from os import path
import numpy as np
import pandas as pd
###############################################################################
#读入CSV数据
#路径名处理
#path_str=u"C:/Users/ll/Desktop/niaoerchao1_static_amplify_kp_10.csv"
path_str=u"C:/Users/ll/Desktop/wqx2_static_amplify.csv"
#path_str=u"C:/Users/ll/Desktop/qingshuitang4_static_amplify_kp_11.csv"


dir_filename,filetype=path.splitext(path_str)   
df=pd.read_csv(path_str,encoding="gb2312")

#将CSV数据的表头进行更换，便于编程处理
df=df.rename(columns={u'Ug(p.u.)':u'Ug',u'Uref(p.u.)':u'Uref',u'dU(p.u.)':u'dU',\
                      u'UFD(V)':u'UFD',u'IFD(A)':u'IFD',u'Uavr(p.u.)':u'Uavr',\
                      u'IFDB(V)':u'IFDB',u'UFDB(V)':u'UFDB',\
                      u'UTN(kV)':u'UTN',u'STN(MW)':u'STN',u'Utk(%)':u'Utk',\
                      u'UFN(V)':u'UFN',u'IFN(A)':u'IFN',u'RFDB':u'RFDB',\
                      u'k':u'k',u'h':u'h',u'UL(kV)':u'UL',u'PID_P':u'PID_P' })

Uref=df.Uref.dropna()
Ug=df.Ug.dropna()
UFD=df.UFD.dropna()
IFD=df.IFD.dropna()
Uavr=df.Uavr.dropna()
IFDB=df.IFDB.dropna()
UFDB=df.UFDB.dropna()
UTN=df.UTN.dropna()
STN=df.STN.dropna()
Utk=df.Utk.dropna()
UFN=df.UFN.dropna()
IFN=df.IFN.dropna()
RFDB=df.RFDB.dropna()
k=df.k.dropna() #对应KFD，就是要求的斜率
h=df.h.dropna()
UL=df.UL.dropna()
PID_P=df.PID_P.dropna()
#首先做一个判断，Ug是百分数还是标幺值，最终转换为标幺值
if Ug.max()>50:
   Ug=Ug/100  
if Uref.max()>50:
   Uref=Uref/100 
dU=Uref-Ug
RFDB=UFN/IFN #在这里，RFDB是Series类型，如果要写值的话，需要取values
UFDB=IFDB*RFDB
Xc=3.0/np.pi*Utk.values/100*UTN.values**2/STN.values   #这里Xc为实际值
###############################################################################
##自并励下，UL*随着Ug*变动
Uavr=(UFD+IFD*Xc)/(UFDB.values*Ug.values*PID_P.values)
KFD=Uavr/dU
KFD=np.average(KFD)
print ("KFD=",KFD)
###############################################################################
#回存到CSV里面
df.Uavr=Uavr
df.k.iloc[0]=0
df.h.iloc[0]=0
df.dU=dU
df.UFDB=UFDB
df.to_csv(path_str,index=None)#保存时去掉索引，否则csv会越来越大

