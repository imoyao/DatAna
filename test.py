#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
http://www.cnblogs.com/jiangzhaowei/p/5856617.html
http://blog.csdn.net/seetheworld518/article/details/49536599
'''

import time
import xlrd
import collections
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


fname = "cw.xlsx"
fname1 = "china.xls"
work_book = xlrd.open_workbook(fname)    #type=list
sheet_name = work_book.sheet_names()[0].encode("utf-8") #sheet name
# print sheet_name
table = work_book.sheet_by_index(0)  #读取第一个sheet   
table_list = table.col_values(1)    #读取第二列（index=1）

useful_data_list = table_list[5:-1][-1]
print useful_data_list

# countyname = table.cell_value(5,1).encode('utf-8')
# county = table.cell(3,1).value.encode('utf-8')
# countype = table.cell(3,1).ctype
# #ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# print countyname
# print county
# print countype
# data = collections.Counter(table_list)
# for k in data:
#     print "the count {} in data is:{}".format(k,data[k])
