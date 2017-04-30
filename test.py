#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
from time import time

import collections
=======
import json
import time
import urllib2
from lxml import etree
# from dataspider import *
>>>>>>> 42006db8009ea794ed9017268117f9f4765f0c43
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

<<<<<<< HEAD
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
=======
def get_html(url):  #
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers = {'User-Agent': user_agent} 
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    print type(html)
    write_file("target.html",html)
    return html

def write_file(w_file_name,content):
    with open(w_file_name,"w") as f:
        f.write(content)
    print "{} write finished.".format(w_file_name)

def get_target_url(pre_html):
    html = etree.HTML(pre_html)
    names = html.xpath('//div[@class = "newsrcon fr"]/ul/li/a/text()')
    urls = html.xpath('//div[@class = "newsrcon fr"]/ul/li/a/@href') 
    target_urls = ["http://www.snchangwu.gov.cn" + i[2:len(i)] for i in urls]
    print type(target_urls)
    target_info =dict(zip(names,target_urls))
    print target_info
    print type(target_info)
    dict3  = json.dumps(target_info).decode("unicode-escape").encode("utf-8")
    print dict3
    print type(dict3)

    write_file("info.json",dict3)


# '''
    # dict1 = {"data":["\u73bb\u7483", "\u5851\u6599", "\u91d1\u5c5e"]}
    # import json
    # j = json.dumps(dict1)
    # dict2  = j.decode("unicode-escape").decode("unicode-escape")
    # print dict2


        # target_info = json.dumps(target_urls,ensure_ascii=False)    #
    # '''

if __name__ == '__main__':
    # url = 'http://www.snchangwu.gov.cn/zjzw/xzgk.htm'
    with open ("target.html","r") as f:
        pre_html = f.read()
    get_target_url(pre_html)
>>>>>>> 42006db8009ea794ed9017268117f9f4765f0c43
