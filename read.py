#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import xlrd
import collections
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def time_func(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        cost_time = end_time-start_time
        print "the func {} takes {}".format(func.__name__,cost_time)
        # return func(*args,**kwargs)
    return wrapper

@time_func
def col_count(data):    #better
    for k in data:
        print "the count {} in data is:{}".format(k,data[k])
'''
# https://www.zhihu.com/question/27800240
@time_func
def set_count(table_list):
    for item in set(table_list):
        print "the count {} in data is:{}".format(item,table_list.count(item))
'''

if __name__ == '__main__':
    fname = "cw.xlsx"
    fname1 = "china.xls"
    workfile = xlrd.open_workbook(fname)    #type=list
    sheet_name = workfile.sheet_names()[0].encode("utf-8") #sheet name
    # print sheet_name
    table = workfile.sheet_by_index(0)
    table_list = table.col_values(1)
    useful_data_list = table_list[5:-1][-1]
    data = collections.Counter(useful_data_list)
    print "*"*20
    col_count(data)
    # print "*"*20
    # set_count(table_list)
