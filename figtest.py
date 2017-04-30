# -*- coding: utf-8 -*-
<<<<<<< HEAD
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import mlab
# from matplotlib import rcParams
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
  
import settings
=======
>>>>>>> 42006db8009ea794ed9017268117f9f4765f0c43
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
<<<<<<< HEAD
import matplotlib.font_manager as mfm
import sys
 
reload(sys)
sys.setdefaultencoding("utf-8")


n_groups = 5  
  
means_men = (20, 35, 30, 35, 27)  
means_women = (25, 32, 34, 20, 25)   
fig, ax = plt.subplots()  
index = np.arange(n_groups)  
bar_width = 0.35   
opacity = 0.4  
rects1 = plt.bar(index, means_men, bar_width,alpha=opacity, color='b',label=    'Men')  
rects2 = plt.bar(index + bar_width, means_women, bar_width,alpha=opacity,color='r',label='Women')  
plt.xlabel('Group')  
plt.ylabel('Scores')  
plt.title('Scores by group and gender')  
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))  
plt.ylim(0,40)  
plt.legend()  
  
plt.tight_layout()  
plt.show()  

=======
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''
http://old.sebug.net/paper/books/scipydoc/index.html
http://blog.csdn.net/jenyzhang/article/details/52047557
http://matplotlib.org/index.html
不显示图片，以便进行批处理：

import matplotlib
matplotlib.use('Agg')
需加在 import matplotlib.pyplot as plt 之前，同时删掉plt.show()
'''

"""
Simple demo of a horizontal bar chart.

atplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
参数说明：

left: 每一个柱形左侧的X坐标

height:每一个柱形的高度

width: 柱形之间的宽度

bottom: 柱形的Y坐标

color: 柱形的颜色

the count 彭公镇 in data is:1723
the count 亭口镇 in data is:1324
the count 相公镇 in data is:1309
the count 巨家镇 in data is:835
the count 昭仁街道办 in data is:1543
the count 枣园镇 in data is:778
the count 丁家镇 in data is:584
the count 洪家镇 in data is:1419
"""

# X=[0,1,2,3,4,5]  
# Y=[222,42,455,664,454,334]    
# fig = plt.figure()  
# plt.bar(X,Y,0.4,color="green")  
# plt.xlabel("X-axis")  
# plt.ylabel("Y-axis")  
# plt.title("bar chart")  

import matplotlib.font_manager as mfm
show_font = mfm.FontProperties(fname='./fonts/msyh.ttf') #指定默认字体  
# x = [0,1,2,3,4,5,6,7]
x = np.arange(0,8,1)
# x = np.linspace(0, 1, 12)
x_axis= ('彭公镇','亭口镇','相公镇','巨家镇','昭仁街道办','枣园镇','丁家镇','洪家镇')
y = [1723,1324,1309,835,1543,778,584,1419]

fig = plt.figure(figsize=(10,8))
rects = plt.bar(x,y,0.8,facecolor = 'lightskyblue',edgecolor = 'white')
plt.xlabel(u"乡镇名",fontproperties=show_font)  
plt.ylabel(u"贫困户数量(户)",fontproperties=show_font)  
plt.title(u"长武县贫困户信息图",fontproperties=show_font,fontsize=20)

# for x_text,y_text in x,y:
# 	plt.text(x-0.02,y,str(int(x)))



def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        print height
        x = rect.get_x()+rect.get_width()/2.0
        y = 1.02*height

        # s = "wosho %.2f"%(0.98)
        percent = "%.2f"%((int(height)/9515.0)*100)

        # percent = "%.2f"%(height/9515.0)*100
        s = "  "+str(int(height))+"\n"+"("+str(percent)+"%"+")"
        plt.text(x-0.3, y, s)
        # print x-0.02,y,s
autolabel(rects)
plt.xticks(x,x_axis,fontproperties=show_font, fontsize=8)
plt.show()   
>>>>>>> 42006db8009ea794ed9017268117f9f4765f0c43

