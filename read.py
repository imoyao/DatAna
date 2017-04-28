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
cost_time = 0
def time_it(func):
    def wrapper(*args,**kwargs):
        global cost_time
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        cost_time = end_time-start_time
        return res,cost_time
    return wrapper


# @time_it
def read_excel():
    fname = settings.EXCEL_PATH
    workfile = xlrd.open_workbook(fname)    #type=list
    sheet_name = workfile.sheet_names()[0].encode("utf-8") #sheet name
    table = workfile.sheet_by_index(0)
    table_list = table.col_values(1)
    useful_data_list = table_list[5:-1]
    return useful_data_list

# @time_it
def unique(data_list):
    return dict(zip(*np.unique(data_list, return_counts=True)))

def sort_dict_by_keys(foo_dict):
    new_list = []
    for k in sorted(foo_dict.keys()):



        new_list.append((k,foo_dict[k]))
    return new_list

# itime_it
def mat_bar_chart(x_axis,y_axis):    #条形图
    show_font = mfm.FontProperties(fname=settings.FONT_PATH) #指定默认字体 
    x = np.arange(0,len(x_axis),1)
    fig = plt.figure(figsize=(10,8))
    print x_axis
    print y_axis
    rects = plt.bar(x,y_axis,0.8,facecolor = 'lightskyblue',edgecolor = 'white')
    plt.xlabel("乡镇名",fontproperties=show_font)  
    plt.ylabel("贫困户数量(户)",fontproperties=show_font)  
    plt.title("长武县贫困户信息图",fontproperties=show_font,fontsize=20)

    x_text = map(lambda i:i-0.3,x)
    y_text = map(lambda i:1.02*i,y_axis)
    s = map(lambda i:"  "+str(int(i))+"\n"+"("+str("{:.2f}".format((int(i)/9515.0)*100))+"%"+")",y_axis)
    for m,n,pstr in zip(x_text, y_text, s):
        plt.text(m,n,pstr)

    plt.xticks(x,x_axis,fontproperties=show_font, fontsize=8)
    plt.savefig("bar_out_put.png")
    # plt.show()


def mat_pie_chart(x_axis,y_axis):    #饼图
    '''
    http://matplotlib.org/api/pyplot_api.html?highlight=pie#matplotlib.pyplot.pie

    x:name
    y:num

    '''
    plt.figure(figsize=(8,4))
    show_font = mfm.FontProperties(fname=settings.FONT_PATH)

    colors = ['r','y','lightskyblue','g','c','#3a9bff','m','pink']
    #将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0.05,0,0,0,0,0,0,0)
    #patches,town_text,p_text
    town_text = plt.pie(y_axis,explode=explode,labels=x_axis,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.2f%%',shadow = False,
                                    startangle = 90,pctdistance = 0.6)

    for town in town_text[1]:

        town.set_fontproperties(show_font)
        town.set_size(8)

    plt.axis('equal')
    plt.legend(prop  = show_font,fontsize = 4,loc = 0)
    plt.title('各乡镇贫困户占比',fontproperties=show_font,fontsize=20)
    plt.savefig("pie_out_put.png")
    # plt.show()

'''
# https://www.zhihu.com/question/27800240
@time_it
def set_count(table_list):
    for item in set(table_list):
        print "the count {} in data is:{}".format(item,table_list.count(item))
'''

if __name__ == '__main__':

    data_list = read_excel()    #TODO if @time_it,should get a list,not tuple

    print "获取数据正常"
    #返回去重字典
    info_dict = unique(data_list)
    # print ana_info  #type:dict
    # ana_info = sort_dict_by_keys(info_dict)
    x_axis = info_dict.keys()
    y_axis = info_dict.values()
    print "开始绘图……"
    try:
        mat_bar_chart(x_axis,y_axis)
    except Exception as e:
        raise e

    try:
        mat_pie_chart(x_axis,y_axis)
    except Exception as e:
        raise e
