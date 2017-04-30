#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import urllib2
from lxml import etree
# from dataspider import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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