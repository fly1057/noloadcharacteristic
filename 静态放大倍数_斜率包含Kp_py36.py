# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:27:55 2018
@author: ll

目的：
本程序通过直接读取csv文件，然后进行静态放大倍数直线拟合画图，同时求取直线y=k*x+h，其中的k即为用于拟合KFD的斜率，
在实际推导过程中KFD=1.35*ULN/UFDB,广科一般使用KFD=1.35*ULN/UFD0，由于斜率肯定是包含了KFD之后的，除开KFD
之外的不确定因素还是通过现场拟合得出。
收获：
1、在已知数值求索引可以利用技巧：index.get_values().max()，就是先求索引然后求值，这时候还是个array，
我要求值的话用max就能得到单个的值。也就是 二维的array——一维的array——单个int，相当于抽丝剥茧。
UAB.head(UAB[(UAB>0.35)&(UAB<0.45)].index.get_values().max())
2、线性最小二乘和非线性最小二乘都要独自定义残差函数，这样就很清晰。
3、可以设定输出图像的大小及像素，可以保存图像。
4、可以对图像进行更进一步的操作，首先要定义plt.figure  
变量定义：
df    dataFrame结构数据，通过pandas直接读取CSV数据
Ug    对应CSV中的Ug，机端电压
Uref  对应CSV中的Uref，机端电压给定参考值
dU    对应CSV中的Uref-UAB
UFD   对应CSV中的UFD，励磁电压
IFD   对应CSV中的IFD，励磁电流
Uavr  对应CSV中的Uavr，对应控制电压Uk，也就是cosα的值
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
思路：
1、确保CSV表中的数据都是标幺化的
2、通过线性最小二乘拟合线性段的ΔU*KA*KFD*UL=UFD+IFD*Xc   (均为标幺值表示)，
即ΔU*KFD=( UFD+IFD*(3/π*Uk%*UTN^2/STN) )/UFDB/KA*UTN/UL
3、画图并保存
"""
from os import path
import numpy as np
import pandas as pd
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
###############################################################################
#读入CSV数据
#路径名处理
path_str=u"C:/Users/ll/Desktop/static_amplify.csv"
dir_filename,filetype=path.splitext(path_str)   
df=pd.read_csv(path_str,encoding="gb2312")
#df=pd.read_excel(path_str)
#将CSV数据的表头进行更换，便于编程处理
df=df.rename(columns={u'Ug(p.u.)':u'Ug',u'Uref(p.u.)':u'Uref',u'dU(p.u.)':u'dU',\
                      u'UFD(V)':u'UFD',u'IFD(A)':u'IFD',u'Uavr(p.u.)':u'Uavr',\
                      u'UFDB(V)':u'UFDB',u'UTN(kV)':u'UTN',u'STN(MW)':u'STN',u'Utk(%)':u'Utk',\
                      u'UFN(V)':u'UFN',u'IFN(A)':u'IFN',u'RFDB':u'RFDB',\
                      u'k':u'k',u'h':u'h',u'UL(kV)':u'UL',u'PID_P':u'PID_P' })
Uavr=df.Uavr.dropna()
UFDB=df.UFDB.dropna()
UTN=df.UTN.dropna()*10**3
STN=df.STN.dropna()*10**6
Utk=df.Utk.dropna()
UFN=df.UFN.dropna()
IFN=df.IFN.dropna()
RFDB=df.RFDB.dropna()
k=df.k.dropna() #对应KFD，就是要求的斜率
h=df.h.dropna()
UL=df.UL.dropna()*10**3
PID_P=df.PID_P.dropna()
#首先做一个判断，Ug是百分数还是标幺值，最终转换为标幺值
if df.Ug.max()>50:
   df.Ug=df.Ug/100  
if df.Uref.max()>50:
   df.Uref=df.Uref/100 
###############################################################################
dU=df.Uref-df.Ug
RFDB=UFN/IFN #在这里，RFDB是Series类型，如果要写值的话，需要取values
Xc=3.0/np.pi*Utk.values/100*UTN.values**2/STN.values   #这里Xc为实际值
###############################################################################
#自并励下，UL*随着Ug*变动
#Uavr=(df.UFD+df.IFD*Xc)/UFDB.values*df.Ug.values
###############################################################################
#他励下，UL*是定值
Uavr=(df.UFD+df.IFD*Xc)/UFDB.values*UTN.values/UL.values
###############################################################################
#拟合直线残差函数,求Uavr与dU的关系，dU为自变量
def  residuals_static_amplify_KA(p):
    k,h=p
    return Uavr-(k*dU+h)

res1=leastsq(residuals_static_amplify_KA,[1,0])
k,h=res1[0]
print ("k=",k,"h=",h,"\n")
###############################################################################
#回存到CSV里面
df.Uavr=Uavr
df.k.iloc[0]=np.round(k,3)
df.h.iloc[0]=np.round(h,3)
df.dU=dU
df.to_csv(path_str,index=None)#保存时去掉索引，否则csv会越来越大
#得到拟合直线
Uavr_sq=np.linspace(Uavr.min(),Uavr.max(),100)
dU_sq=(Uavr_sq-h)/k
#设定图像大小，像素，去除边框
plt.figure(figsize=(7,4),dpi=100)
ax = plt.gca()
ax.spines['top'].set_visible(False)  #去掉上边框
ax.spines['right'].set_visible(False) #去掉右边框
#画曲线
plt.plot(dU_sq,Uavr_sq)
plt.plot(dU,Uavr,"^")
#legend
plt.legend(['Fitting line','Data point'])
#text
plt.text(dU_sq.min()*1.2, Uavr_sq.max()*0.7,\
         'y='+str(round(k,3))+'x'+str(round(h,3)), \
         horizontalalignment='center',\
         verticalalignment='center')
#坐标图框架
#plt.title("")
plt.xlabel("(Uref-Ug)   (p.u.)")
plt.ylabel("Uavr        (p.u.)")
plt.xlim([dU_sq.min()*0.9,dU_sq.max()])
plt.ylim([Uavr_sq.min()*0.9,Uavr_sq.max()*1.1])
#plt.grid()
plt.savefig(dir_filename+'.jpg',format='jpg') 