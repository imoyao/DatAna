#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time

import collections

# how to???
# def foo():
# 	listmylist.append()
# 	return mylist

# a = foo()
# type(a) = list

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:01:29 2016

@author: toby
"""
#知识点：原函数有返回值，加上装饰器如何拿到返回值？

# #装饰器函数
# def outer(fun): 
#     def wrapper(strs): 
#         # print '哈哈'
#         res = fun(strs)
#         return res #返回原函数的返回值
#         # print 'hello world!'
#     return wrapper

# @outer
# def func1(arg):
#     print 'this is func1',arg
#     return '100' #这是原函数的返回值

# #调用函数时，传入一个字符串作为参数
# aa = func1("my name is tantianran")
# print aa


# https://zhidao.baidu.com/question/474181365.html
funcall_cost = 0
def time_it(func):
	def wrapfunc(*args):
		global funcall_cost
		now = time()
		result = func(*args)
		funcall_cost = time() - now
		return result,funcall_cost
	return wrapfunc

@time_it 
def counter(foo_list):
    rets = collections.Counter(foo_list)
    # foo_dict = dict(rets)
    # print foo_dict
    return dict(rets)

if __name__ == '__main__':
    foo_list = ["a","b","c","a","b","a","b","c","a","b"]
    a = counter(foo_list)
    print a
    # print funcall_cost