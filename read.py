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
# @time_func
# def set_count(table_list):
#     for item in set(table_list):
#         # print set(table_list)
#         print "the count {} in data is:{}".format(item,table_list.count(item))
if __name__ == '__main__':
    fname = "cw.xlsx"
    fname1 = "china.xls"
    workfile = xlrd.open_workbook(fname)    #type=list
    sheet_name = workfile.sheet_names()[0].encode("utf-8") #sheet name
    # print sheet_name
    table = workfile.sheet_by_index(0)
    table_list = table.col_values(1)
    data = collections.Counter(table_list)
    print "*"*20
    col_count(data)
    # print "*"*20
    # set_count(table_list)
