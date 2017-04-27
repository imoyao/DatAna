#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import xlrd
import collections
import sys
import settings
'''
不显示图片，以便进行批处理或调试：

import matplotlib
matplotlib.use('Agg')
需加在 import matplotlib.pyplot as plt 之前，同时删掉plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
import matplotlib.font_manager as mfm


reload(sys)
sys.setdefaultencoding("utf-8")

'''
http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
http://www.cnblogs.com/jiangzhaowei/p/5856617.html
http://blog.csdn.net/seetheworld518/article/details/49536599
http://old.sebug.net/paper/books/scipydoc/index.html
http://blog.csdn.net/jenyzhang/article/details/52047557
http://matplotlib.org/index.html
'''


def time_it(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        cost_time = end_time-start_time
        print "the func {} takes {}".format(func.__name__,cost_time)
    return wrapper

@time_it
def col_count(data):    #better
    mydict = {}
    for k in data:
        mydict[k] = data[k]

        print "the count {} in data is:{}".format(k,data[k])  

# @time_it
def read_excel():
    fname = settings.EXCEL_PATH
    workfile = xlrd.open_workbook(fname)    #type=list
    sheet_name = workfile.sheet_names()[0].encode("utf-8") #sheet name
    table = workfile.sheet_by_index(0)
    table_list = table.col_values(1)
    useful_data_list = table_list[5:-1]
    data = collections.Counter(useful_data_list)
    return data

@time_it
def mat_figure_out(x_axis,y):
    '''
    Simple demo of a horizontal bar chart.

    matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
    参数说明：

    left: 每一个柱形左侧的X坐标

    height:每一个柱形的高度

    width: 柱形之间的宽度

    bottom: 柱形的Y坐标

    color: 柱形的颜色
    '''
    show_font = mfm.FontProperties(fname=settings.FONT_PATH) #指定默认字体 
    x = np.arange(0,len(x_axis),1)
    fig = plt.figure(figsize=(10,8))
    rects = plt.bar(x,y,0.8,facecolor = 'lightskyblue',edgecolor = 'white')
    plt.xlabel("乡镇名",fontproperties=show_font)  
    plt.ylabel("贫困户数量(户)",fontproperties=show_font)  
    plt.title("长武县贫困户信息图",fontproperties=show_font,fontsize=20)

    x_text = map(lambda i:i-0.3,x)
    y_text = map(lambda i:1.02*i,y)

    s = map(lambda i:"  "+str(int(i))+"\n"+"("+str("{:.2f}".format((int(i)/9515.0)*100))+"%"+")",y)
    for m,n,pstr in zip(x_text, y_text, s):
        plt.text(m,n,pstr)

    plt.xticks(x,x_axis,fontproperties=show_font, fontsize=8)
    plt.savefig("out_put.png")
    # plt.show()
'''
# https://www.zhihu.com/question/27800240
@time_it
def set_count(table_list):
    for item in set(table_list):
        print "the count {} in data is:{}".format(item,table_list.count(item))
'''

if __name__ == '__main__':

    ana_info = read_excel()
    # print ana_info
    print "获取数据正常"

    x_axis,y = [],[]
    for i,j in ana_info.items():
        x_axis.append(i)
        y.append(j)
    print "开始绘图……"

    try:
        mat_figure_out(x_axis,y)
    except Exception as e:
        raise e
