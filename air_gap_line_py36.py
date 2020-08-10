# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:37:09 2017
修改
1、首先通过曲线拟合方法求出abn，然后求出SG1.0  SG1.2 ，然后通过1167的公式反过来计算abn，
为了和excel表一致。20180414
2、对气隙线进行了消除残压的处理，空载特性曲线应该是不包含残压的曲线，气隙线上应减去h，饱和曲线的UAB应减去h
@author: ll

目的：
本程序通过直接读取csv文件，然后进行空载特性曲线、气隙线画图，同时求取a，b，n，SG1.0，SG1.2

收获：
1、在已知数值求索引可以利用技巧：index.get_values().max()，就是先求索引然后求值，这时候还是个array，
我要求值的话用max就能得到单个的值。也就是 二维的array——一维的array——单个int，相当于抽丝剥茧。
UAB.head(UAB[(UAB>0.35)&(UAB<0.45)].index.get_values().max())
2、线性最小二乘和非线性最小二乘都要独自定义残差函数，这样就很清晰。
3、可以设定输出图像的大小及像素，可以保存图像。
4、可以对图像进行更进一步的操作，首先要定义plt.figure  

变量定义：
df   dataFrame结构数据，通过pandas直接读取CSV数据
UAB  对应CSV中的UAB
IFD  对应CSV中的IFD
UAB_40_sq  对应UAB中前0.4UN及之前的点组成的array
IFD_40_sq  对应IFD中前0.4IFD及之前的点组成的array
residuals_airgap_line  线性最小二乘函数的残差函数
UAB_air_sq  气隙线上的UAB数组
IFD_air_sq  气隙线上的IFD数组
IFD_air_100_value  1.0UN对应的励磁电流
IFD_air_120_value  1.2UN对应的励磁电流
UAB_air_100_vertical_sq  气隙线上1.0UN对应的垂线的UAB纵坐标数组
IFD_air_100_vertical_sq  气隙线上1.0UN对应的垂线的IFD横坐标数组
UAB_air_120_vertical_sq  气隙线上1.2UN对应的垂线的UAB纵坐标数组
IFD_air_120_vertical_sq  气隙线上1.2UN对应的垂线的IFD横坐标数组
residuals_saturation_curve  非线性最小二乘函数的残差函数
a,b,n,SG1.0,SG1.2  
UAB_saturation_sq  空载特性曲线上的UAB数组
IFD_saturation_sq  空载特性曲线上的IFD数组
UAB_sat_100_vertical_sq  空载特性曲线上1.0UN对应的垂线的UAB纵坐标数组
IFD_sat_100_vertical_sq  空载特性曲线上1.0UN对应的垂线的IFD横坐标数组
UAB_sat_120_vertical_sq  空载特性曲线上1.2UN对应的垂线的UAB纵坐标数组
IFD_sat_120_vertical_sq  空载特性曲线上1.2UN对应的垂线的IFD横坐标数组

思路：
1、把UAB标幺化
2、取0.4UN之前的点，通过线性最小二乘拟合线性段的UAB=k*IFD+h
3、将拟合直线延伸到1.2UN处
4、记录拟合直线UN=1和UN=1.2时的IFD，将UN=1时的IFD作为IFDB
5、用IFDB把IFD标幺化
6、使用全部标幺化的IFD和UAB，通过非线性最小二乘拟合IFD=a*UAB+b*UAB^n求出abn
7、将拟合曲线延伸至1.2UN处
7、计算拟合曲线UN=1和UN=1.2时的IFD，对拟合曲线的IFD有名值化，用于画图
8、画标记点的下垂线

"""

from os import path
import numpy as np
import pandas as pd
from scipy.optimize import least_squares, leastsq
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

###############################################################################

# 读入CSV数据
# 路径名处理
# path_str=u"C:/Users/ll/Desktop/ddj4_voltage_ascend.csv"
# path_str=u"C:/Users/ll/Desktop/yiyang4_no_load_curve.csv"
# path_str=u"C:/Users/ll/Desktop/wqx2.csv"
# path_str=u"C:/Users/ll/Desktop/yongxin1_shengya.csv"
# path_str=u"C:/Users/ll/Desktop/yongxin2talikongzai.csv"
# path_str=u"C:/Users/ll/Desktop/hongjiang2shengya1.csv"
# path_str=u"C:/Users/ll/Desktop/youxian2shengya.csv"
# path_str=u"C:/Users/ll/Desktop/hmf1_kongzai2018.csv"
# path_str=u"C:/Users/ll/Desktop/hmf2_kongzai2018.csv"
# path_str=u"C:/Users/ll/Desktop/xiangtan3kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/wuqiangxi3kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/wuqiangxi4kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/xiangtan1kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/LCJ2_xiangtan1kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/xiaodongjiang1kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/yueyang1kongzai2019.csv"
# path_str=u"C:/Users/ll/Desktop/centianhe4.csv"
path_str = u"C:/Users/ll/Desktop/zaoshi1.csv"

# path_str=u"C:/Users/ll/Desktop/sjk7.csv"
# path_str=u"C:/Users/ll/Desktop/ddj1_voltage_ascend.csv"
# path_str=u"C:/Users/ll/Desktop/caijiazhou4.csv"

dir_filename, filetype = path.splitext(path_str)
df = pd.read_csv(path_str, encoding="gb2312")
# df=pd.read_excel(path_str)

# 将CSV数据的表头进行更换，便于编程处理
#df=df.rename(columns={ u'UAB(V)':u'UAB', u'IA(A)':u'IA', u'UFD(V)':u'UFD', u'IFD(A)': u'IFD'})
#df=df.rename(columns={ u'Time':u't',u'UAB(V)':u'UAB',u'UBC(V)':u'UBC',u'UCA(V)':u'UCA',  u'UFD(V)':u'UFD', u'IFD(A)': u'IFD'})
#df=df.rename(columns={ u'Time':u't',u'UAB(V)':u'UAB', u'IFD(A)': u'IFD'})
df = df.rename(columns={
    u'UAB(V)': u'UAB',
    u'UFD(V)': u'UFD',
    u'IFD(A)': u'IFD'
})

# 截取上升段的数据，注意需要找到最大值index后加1
UAB = df.UAB[0:(df.UAB.idxmax() + 1)]
IFD = df.IFD[0:(df.UAB.idxmax() + 1)]
UFD = df.UFD[0:(df.UAB.idxmax() + 1)]

# 首先做一个判断，UAB是百分数还是标幺值，最终转换为标幺值
if UAB.max() > 50:
    UAB = UAB / 100

# 取IFD和UAB前面0.4额定电压的段作为气隙线的拟合基本数据
# 通过UAB[(UAB>0.35)&(UAB<0.45)].index.get_values()得到index的array
# 由于head需要int型变量，那么array是不行的，取个巧，取这个array的最大
# 值的到index的int值
UAB_40_sq = UAB.head(UAB[(UAB > 0.45) & (UAB < 0.6)].index.to_numpy().max())
IFD_40_sq = IFD.head(UAB[(UAB > 0.45) & (UAB < 0.6)].index.to_numpy().max())
UFD_40_sq = UFD.head(UAB[(UAB > 0.45) & (UAB < 0.6)].index.to_numpy().max())
###############################################################################
# 气隙线残差函数


def residuals_airgap_line_IFD(p):
    k, h = p
    return UAB_40_sq - (k * IFD_40_sq + h)


def residuals_airgap_line_UFD(p):
    k, h = p
    return UAB_40_sq - (k * UFD_40_sq + h)


res_IFD = leastsq(residuals_airgap_line_IFD, [1, 0])
k_IFD, h_IFD = res_IFD[0]
print("k_IFD = ", k_IFD, "h_IFD = ", h_IFD, "\n")

res_UFD = leastsq(residuals_airgap_line_UFD, [1, 0])
k_UFD, h_UFD = res_UFD[0]
print("k_UFD = ", k_UFD, "h_UFD = ", h_UFD, "\n")

# 对UAB减去残压，然后对IFD也同样进行筛选
UAB_sq_IFD = UAB.head(UAB[(UAB > h_IFD)].index.to_numpy().max())
IFD_sq_IFD = IFD.head(UAB[(UAB > h_IFD)].index.to_numpy().max())

UAB_sq_UFD = UAB.head(UAB[(UAB > h_UFD)].index.to_numpy().max())
IFD_sq_UFD = IFD.head(UAB[(UAB > h_UFD)].index.to_numpy().max())

h_IFD = 0
h_UFD = 0
# 得到气隙线
UAB_air_sq = np.linspace(0, 1.3, 131)  # 得到消除残压后的实际发电机本体的气隙线
IFD_air_sq = (UAB_air_sq) / k_IFD
UFD_air_sq = (UAB_air_sq) / k_UFD

# 计算气隙线上的点
IFD_air_100_value = (1.0) / k_IFD  # 1.0UN对应的励磁电流
IFD_air_120_value = (1.2) / k_IFD  # 1.2UN对应的励磁电流

UFD_air_100_value = (1.0) / k_UFD  # 1.0UN对应的励磁电压
UFD_air_120_value = (1.2) / k_UFD  # 1.2UN对应的励磁电压

# 形成气隙线上1.0及1.2倍UN的下垂线
UAB_air_100_vertical_sq = np.linspace(0, 1.0, 141)  # 注意点数要都一致
IFD_air_100_vertical_sq = np.linspace(IFD_air_100_value, IFD_air_100_value,
                                      141)
UAB_air_120_vertical_sq = np.linspace(0, 1.2, 141)
IFD_air_120_vertical_sq = np.linspace(IFD_air_120_value, IFD_air_120_value,
                                      141)

###############################################################################

# 计算空载特性曲线上的点
# 根据PSASP说明书中空载曲线的形式为 IFD=a*UAB+b*UAB^n，a取为1，则实际未知参数只有b、n。

# 空载特性曲线残差函数


def residuals_saturation_curve(p):
    b, n = p
    # 标幺化后进行的计算，否则误差会很大,UAB为实际上的电压，需要减去h
    return IFD / IFD_air_100_value - (UAB + b * (UAB)**n)


# 进行计算前的初始化条件
lb = np.array([0.01, 0.01])
ub = np.array([10.0, 15.0])
x0 = [0.1, 7]
res2 = least_squares(residuals_saturation_curve,
                     x0,
                     ftol=0.001,
                     bounds=(lb, ub),
                     method='trf')
b, n = res2.x
a = 1

#print ("a=",1," b=",b," n=",n,"\n")
#print ("cost=",res2.cost)

# 得到空载特性曲线
UAB_saturation_sq = np.linspace(0, 1.22, 141)
IFD_saturation_sq = (UAB_saturation_sq +
                     b * UAB_saturation_sq**n) * IFD_air_100_value
UFD_saturation_sq = (UAB_saturation_sq +
                     b * UAB_saturation_sq**n) * UFD_air_100_value

# 计算空载特性曲线上的点
IFD_sat_100_value = (1 + b * 1**n) * IFD_air_100_value  # 1.0UN对应的励磁电流
IFD_sat_120_value = (1.2 + b * 1.2**n) * IFD_air_100_value  # 1.2UN对应的励磁电流

# 形成空载特性曲线上1.0及1.2倍UN的下垂线
UAB_sat_100_vertical_sq = np.linspace(0, 1.0, 141)  # 注意点数要都一致
IFD_sat_100_vertical_sq = np.linspace(IFD_sat_100_value, IFD_sat_100_value,
                                      141)
UAB_sat_120_vertical_sq = np.linspace(0, 1.2, 141)
IFD_sat_120_vertical_sq = np.linspace(IFD_sat_120_value, IFD_sat_120_value,
                                      141)

SG100 = (IFD_sat_100_value - IFD_air_100_value) / IFD_air_100_value
SG120 = (IFD_sat_120_value - IFD_air_120_value) / IFD_air_120_value

# 按照公式再算一遍a b n，在这里使用IFD0的实际值，而在excel中使用的约等值，因此有误差
a = 1
b = SG100
n = 1 + np.log(SG120 / SG100) / np.log(1.2)


###############################################################################
#静态放大倍数计算
#通过abn先计算SG
def SG_function(UAB, a, b, n):
    SG =  b / a * UAB**(n - 1)
    return SG

SG = SG_function(UAB_saturation_sq, a, b, n)
print("SG = ", SG)

IFDB = []
UFDB = []
KFD = []
ULN = 450  # V
STN = 10**6  # W
Uk = 0.06

for i in np.arange(IFD_saturation_sq.__len__()):
    if i == 0:
        pass
    else:
        IFDB.append((IFD_saturation_sq[i] / (1+SG[i])) / UAB_saturation_sq[i])
        UFDB.append((UFD_saturation_sq[i] / (1+SG[i])) / UAB_saturation_sq[i])
        KFD.append(
            1.35 * ULN * UAB_saturation_sq[i] /
            ((UFD_saturation_sq[i] + IFD_saturation_sq[i] * ULN**2/STN*Uk ) / (1+SG[i])))

print("IFDB = ", IFDB)
print("UFDB = ", UFDB)
print("KFD = ", KFD)
###############################################################################

# 设定图像大小，像素，去除边框
plt.figure(figsize=(7, 4), dpi=100)
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去掉上边框
ax.spines['right'].set_visible(False)  # 去掉右边框

# 所画曲线
plt.plot(IFD_saturation_sq, UAB_saturation_sq, color='k', marker='*')
plt.plot(IFD_air_sq, UAB_air_sq, color='k', marker='')
plt.plot(IFD_air_100_vertical_sq, UAB_air_100_vertical_sq, ':', color='k')
plt.plot(IFD_air_120_vertical_sq, UAB_air_120_vertical_sq, ':', color='k')
plt.plot(IFD_sat_100_vertical_sq, UAB_sat_100_vertical_sq, ':', color='k')
plt.plot(IFD_sat_120_vertical_sq, UAB_sat_120_vertical_sq, ':', color='k')

# legend
#plt.legend(['Saturation curve','Air-gap line'])
plt.legend(['空载特性曲线', '气隙线'])

# 标注IFDB、a、b、n、SG1.0、SG1.2
plt.text(IFD_air_100_value,
         1.05,
         'IFDB1.0=' + str(round(float(IFD_air_100_value),1)) + 'A',
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_120_value,
         1.25,
         'IFDB1.2=' + str(round(float(IFD_air_120_value),1)) + 'A',
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_sat_100_value,
         0.5,
         'IFD01.0=' + str(round(float(IFD_sat_100_value),1)) + 'A',
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_sat_120_value,
         0.5,
         'IFD01.2=' + str(round(float(IFD_sat_120_value),1)) + 'A',
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 5.0,
         1,
         'a=' + str(round(a, 3)),
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 5,
         0.9,
         'b=' + str(round(b, 3)),
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 5,
         0.8,
         'n=' + str(round(n, 3)),
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 5,
         0.7,
         'SG1.0=' + str(round(SG100, 3)),
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 5,
         0.6,
         'SG1.2=' + str(round(SG120, 3)),
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 2,
         1 ,
         'IFDB=' + str(round(IFDB[0], 1))+"A",
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 2,
         0.9,
         'UFDB=' + str(round(UFDB[0], 1))+"V",
         horizontalalignment='center',
         verticalalignment='center')

plt.text(IFD_air_100_value / 2,
         0.8,
         'KFD=' + str(round(KFD[0], 2)),
         horizontalalignment='center',
         verticalalignment='center')

# 坐标图框架
# plt.title("")
plt.xlabel("Ifd /A")
plt.ylabel("Ug /p.u.")
plt.xlim([0, IFD_saturation_sq.max()])
plt.ylim([0, 1.3])
# plt.grid()
plt.savefig(dir_filename + '2.jpg', format='jpg')
plt.show()
