# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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

