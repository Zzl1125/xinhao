# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt     #导入matplotlib库
import numpy as np                  #导入numpy包
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)   #0--3*pi等分为100份，共100个点
y = np.sin(x)                        #对x元素取正弦

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)       #一个FIGURE图形生成一行两列两个子图，subplot(1,2,1)后面一个1表示当前激活第二个子图
plt.title(r'$f(x)=sin(x)$')          #显示图片的标题
plt.plot(x, y)                       #x轴数据，y轴数据，format_string控制曲线的格式字串 
#plt.show()

x1 = [t*0.375*np.pi for t in x]      #x1的范围是t*0.375*pi--x
y1 = np.sin(x1)                      #对x元素取正弦
plt.subplot(1,2,2)      #一个FIGURE图形生成一行两列两个子图，subplot(1,2,2)后面一个2表示当前激活第二个子图
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #显示图片的标题
plt.plot(x, y1)                      #x轴数据，y轴数据，format_string控制曲线的格式字串
plt.show()                           #显示图片，不显示格式
