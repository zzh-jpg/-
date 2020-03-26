# -*- coding: utf-8 -*-
#车辆的跟随距离问题
#following_distance.py

import numpy as np      #导入科学计算包numpy库
#数值计算库scipy中的子函数库optimize已经提供了实现最小二乘拟合算法的函数leastsq
from scipy.optimize import leastsq
import pylab as pl

#（1）定义待拟合的函数。x是变量，p是待求参数
def fun(x, p):
    return 0.75*x + p*x*x   #返回拟合函数

#（2）定义偏差函数：计算真实数据和拟合数据之间的误差。p是待拟合的参数，x和y分别是对应的真实数据
def residuals(p, x, y):
    return fun(x, p) - y

#（3）一组真实实验数据
#x1 = np.array([20, 30, 40, 50, 60, 70, 80], dtype=float)
x1 = np.array([29.3, 44, 58.7, 73.3, 88, 102.7, 117.3], dtype=float)   #车速
y1 = np.array([42, 73.5, 116, 173, 248, 343, 464], dtype=float)        #刹车距离

#（4）调用拟合函数。第一个参数是偏差函数，第二个是拟合初始值，第三个是需要拟合的实验数据
r = leastsq(residuals, [1], args=(x1, y1))

#（5）输出拟合参数。r[0]存储的是拟合参数，r[1]、r[2]代表其他信息
print ('拟合参数k为：',r[0])

#（6）根据模型计算刹车距离和以原车速v走过该刹车距离需要的时间
dis=[None]*7           #创建一个包含7个元素的空列表，存储根据模型计算出来的刹车距离
t=[None]*7             #创建一个包含7个元素的空列表，存储以原车速v走过计算刹车距离dis需要的时间
v = [29.3, 44, 58.7, 73.3, 88, 102.7, 117.3]#车速
print('车速v为：',v)
for i in range(0,7):
    dis[i]=0.75*v[i] + r[0]*v[i]*v[i]
    t[i]=dis[i]/v[i]
    print('v[',i,']=',v[i],'，dis[',i,']=',dis[i],'，t[',i,']=',t[i])   
    
#（7）绘制散点图和拟合曲线
pl.plot(x1, y1,  'o',label="data")          #绘制散点图
pl.plot(x1, fun(x1, r[0]), label="match")   #绘制拟合曲线
pl.legend()                                 #绘制图例
pl.show()



#print(v)
#for i in range(0,7):
    #print('v[i] is',v[i])
    #dis[i]=0.75*v[i] + r[0]*v[i]*v[i]
    #print('dis[i] is',dis[i])

