#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time

import collections
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# foo_dict ={"c":1,"a":3,"b":5}

foo_dict = {u'\u5f6d\u516c\u9547': 1723, u'\u4ead\u53e3\u9547': 1324, u'\u76f8\u516c\u9547': 1309, u'\u5de8\u5bb6\u9547': 835, u'\u662d\u4ec1\u8857\u9053\u529e': 1543, u'\u67a3\u56ed\u9547': 778, u'\u4e01\u5bb6\u9547': 584, u'\u6d2a\u5bb6\u9547': 1419}
# foo_dict = {'彭公镇': 1723, '亭口镇': 1324, '相公镇': 1309, '巨家镇': 835, '昭仁街道办': 1543, '枣园镇': 778, '丁家镇': 584, '洪家镇': 1419}
x_axis = foo_dict.keys()
y_axis = foo_dict.values()
# print x_axis
# print y_axis
# def sort_dict_by_keys(foo_dict):
#     new_list = []
#     for k in sorted(foo_dict.keys()):



#         new_list.append((k,foo_dict[k]))
#     print new_list

# sort_dict_by_keys(foo_dict)
# '''
# [(u'\u4e01\u5bb6\u9547', 584), (u'\u4ead\u53e3\u9547', 1324), (u'\u5de8\u5bb6\u9547', 835), (u'\u5f6d\u516c\u9547', 1723), (u'\u662d\u4ec1\u8857\u9053\u529e', 1543), (u'\u67a3\u56ed\u9547', 778), (u'\u6d2a\u5bb6\u9547', 1419), (u'\u76f8\u516c\u9547', 1309)]

# '''

# # [(k,foo_dict[k]) for k in sorted(foo_dict.keys())]
#     # return str(new_list).replace('u\'','\'').decode("unicode-escape")
# def get_axis_list():

#     x_axis, y_axis= [],[]

#     for item in sort_dict_by_keys(foo_dict):
#         x_axis.append(item[0])
#         y_axis.append(item[1])
#     return zip(x_axis,y_axis)

# a = get_axis_list()
# print a
'''
https://www.zhihu.com/question/53470998
http://blog.csdn.net/jemila/article/details/52808391
import json
j = json.dumps(ana_info)
decode_info  = j.decode("unicode-escape").decode("unicode-escape")

'''
















    
# print [(k,foo_dict[k]) for k in sorted(foo_dict.keys())]

# # https://zhidao.baidu.com/question/474181365.html
# funcall_cost = 0
# def time_it(func):
# 	def wrapfunc(*args):
# 		global funcall_cost
# 		now = time()
# 		result = func(*args)
# 		funcall_cost = time() - now
# 		return result,funcall_cost
# 	return wrapfunc

# @time_it 
# def counter(foo_list):
#     rets = collections.Counter(foo_list)
#     # foo_dict = dict(rets)
#     # print foo_dict
#     return dict(rets)

# if __name__ == '__main__':
#     foo_list = ["a","b","c","a","b","a","b","c","a","b"]
#     a = counter(foo_list)
#     print a
#     # print funcall_cost