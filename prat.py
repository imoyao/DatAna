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
# y = [1723,1324,1309,835,1543,778,584,1419]
# # s = map(lambda i:"  "+str(int(i))+"\n"+"("+str("%.2f"%((int(i)/9515.0)*100))+"%"+")",y)
# # print s
# s = map(lambda i:"  "+str(int(i))+"\n"+"("+str("{:.2f}".format((int(i)/9515.0)*100))+"%"+")",y)
# print s
# cost_time = 0
# def time_it(func):
#     def wrapper(*args,**kwargs):
#         global cost_time
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         end_time = time.time()
#         cost_time = end_time-start_time
#         return res,"the func {} takes {}".format(func.__name__,cost_time)
#     return wrapper
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
    # print useful_data_list
    # print len(useful_data_list)

    # rets = collections.Counter(useful_data_list)
    # '''data = {}
    # for k in rets:
    #     data[k] = rets[k]
    #     result = data
    # print result
    # print type(result)
    # # return result'''
    # data = dict(rets)
    # print data
@time_it 
def set_count(table_list):
    # foo_list = ["a","b","c","a","b","a","b","c","a","b"]
    foo_dict = {}
    for item in set(foo_list):
        foo_dict[item] = foo_list.count(item)
    # print "%s"%set_count.__name__
    # print foo_dict
    # print "%s"%set_count.__name__
    return foo_dict

@time_it 
def list_count(table_list):
    # foo_list = ["a","b","c","a","b","a","b","c","a","b"]
    foo_dict = {}
    for item in foo_list:
        foo_dict[item] = foo_list.count(item)
    # print "%s"%set_count.__name__
    # print foo_dict
    # print "%s"%set_count.__name__
    return foo_dict

@time_it 
def counter(foo_list):
    rets = dict(collections.Counter(foo_list))

    return rets

def generate_data(num=1000000):
    return np.random.randint(num / 10, size=num)

@time_it
def unique(lst):
    return dict(zip(*np.unique(lst, return_counts=True)))

if __name__ == '__main__':
    # foo = generate_data(100)
    # print foo
 # https://www.oschina.net/question/2400361_2151742
 # https://www.zhihu.com/question/27800240
    # foo_list = read_excel()
    foo_list = list(generate_data(10))

    n = unique(foo_list)
    n_t = n[1]

    a = set_count(foo_list)
    # print a
    set_t = a[1]

    c = counter(foo_list)
    # print c

    count_t = c[1]

    b = list_count(foo_list)
    # print b
    list_t = b[1]
    print n
    print a
    print b
    print c
    time_list = [set_t,count_t,n_t,list_t]
    print time_list
    time_list.sort()
    print time_list
    # num > 1000时:u,c,s,l
    # num = 100时:s,c,n,l

    # print t1 > t2
    # a = foo(range(3),["a","b","c"])
    # print a