# -*- coding: utf-8 -*-
#车辆的跟随距离问题中的刹车距离-车速散点图
#parking_scatter.py

import numpy as np                #导入科学计算包numpy库
import matplotlib.pyplot as plt   #导入matplotlib.pyplot模块

#一组真实实验数据
v = np.array([29.3,44,58.7,73.3,88,102.7,117.3], dtype=float)   #车速
d = np.array([42, 73.5, 116, 173, 248,343,464], dtype=float)    #刹车距离
plt.plot(v,d,'o')              #绘制散点图

plt.plot(v, d)                 #绘制曲线
plt.title('Figure of Braking Distance to Speed')    #设置图标题
plt.xlabel('Speed')            #设置x轴标签
plt.ylabel('Braking Distance') #设置y轴标签
plt.xlim(20, 120)              #设置x轴坐标限度
plt.ylim(40, 500)              #设置y轴坐标限度
plt.show()

