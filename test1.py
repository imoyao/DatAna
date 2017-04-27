#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import xlrd
import collections
import sys
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
def time_it(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        cost_time = end_time-start_time
        print "the func {} takes {}".format(func.__name__,cost_time)
    return wrapper
@time_it   
def read_excel():
	fname = "cw.xlsx"
	workfile = xlrd.open_workbook(fname)    #type=list
	sheet_name = workfile.sheet_names()[0].encode("utf-8") #sheet name
	table = workfile.sheet_by_index(0)
	table_list = table.col_values(1)
	useful_data_list = table_list[5:-1]
	print len(useful_data_list)
	ret = collections.Counter(useful_data_list)
	data = dict(ret)
	print data
	
	"""
	import collections
	lst = []    # lst存放所谓的100万个元素
	d = collections.Counter(lst)
	# 瞬间出结果
	for k in d:
	    # k是lst中的每个元素
	    # d[k]是k在lst中出现的次数

	"""
	print type(data)
	# return data

@time_it
def col_count(data):    #better
    mydict = {}
    for k in data:
        mydict[k] = data[k]

        print "the count {} in data is:{}".format(k,data[k])  

if __name__ == '__main__':
	# a = read_excel()
	# print type(a)
	read_excel()
	print a