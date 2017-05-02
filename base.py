#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import xlrd
import sys
'''
不显示图片，以便进行批处理或调试：

import matplotlib
matplotlib.use('Agg')
需加在 import matplotlib.pyplot as plt 之前，同时删掉plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm

import settings
from dataspider import detail_spider
from gettowninfo import read_json_info
from gettowninfo import get_info_main

reload(sys)
sys.setdefaultencoding("utf-8")


cost_time = 0


def time_it(func):
    def wrapper(*args, **kwargs):
        global cost_time
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        cost_time = end_time-start_time
        return res, cost_time
    return wrapper


# @time_it
def read_excel():
    '''
    read excel and get useful data list.
    :return: 
    '''
    fname = settings.EXCEL_PATH_FILE
    workfile = xlrd.open_workbook(fname)  # type=list
    # sheet_name = workfile.sheet_names()[0].encode("utf-8") #sheet name
    table = workfile.sheet_by_index(0)
    table_list = table.col_values(1)
    useful_data_list = table_list[5:-1]
    return useful_data_list


def unique(data_list):
    '''
    列表去重返回字典形式
    :param data_list: 
    :return: 
    '''
    return dict(zip(*np.unique(data_list, return_counts=True)))

family_num = []


def get_town_family_num(town_json_info):

    town_info = town_json_info.values()
    for item in town_info:

        each_family_num = item["family_num"]

        family_num.append(each_family_num)
    return family_num


def get_poverty_info():
    data_list = read_excel()  # TODO if @time_it,should get a list,not tuple

    print "获取excel数据正常"
    # 返回去重字典
    info_dict = unique(data_list)
    poverty_num_list = sort_dict_by_keys(info_dict)

    return poverty_num_list


def get_family_info():
    town_json_info = read_json_info(settings.TARGET_JSON_FILE)
    print "获取json数据正常"
    town_name = town_json_info.keys()
    family_num_list = get_town_family_num(town_json_info)
    family_dict = dict(zip(town_name, family_num_list))
    fam_info = sort_dict_by_keys(family_dict)
    return fam_info


def sort_dict_by_keys(old_dict):
    new_list = []
    for k in sorted(old_dict.keys()):
        new_list.append((k, old_dict[k]))
    return new_list


def mat_bar_chart(x_axis, y_axis, y_axis_total):  # 条形图
    show_font = mfm.FontProperties(fname=settings.FONT_PATH_FILE)  # 指定默认字体
    x = np.arange(0, len(x_axis), 1)
    fig = plt.figure(figsize=(10, 8))

    plt.bar(x, y_axis_total, 0.9, facecolor='lightskyblue',
            edgecolor='white', label='总户数')

    plt.bar(x, y_axis, 0.9, facecolor='red', bottom=0, label='贫困户')

    # 标注红色条形图文字
    x_text = map(lambda i: i-0.3, x)
    y_text = map(lambda i: 1.03*i, y_axis)
    s = map(lambda i, j: "   "+str(int(i))+"\n"+"(" +
            str("{:.2f}".format((int(i)/float(j)*100)))+"%"+")", y_axis, y_axis_total)

    for m, n, pstr in zip(x_text, y_text, s):
        plt.text(m, n, pstr)

    # 标注青色条形图文字
    y_text_total = map(lambda i: 1.02*i, y_axis_total)
    s = map(lambda i: "  "+str(int(i)), y_axis_total)

    for m, n, pstr in zip(x_text, y_text_total, s):
        plt.text(m, n, pstr)

    # 设置边框不可见
    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.ylim(0, max(y_axis_total)*1.1)  # 设定y轴范围
    plt.legend(prop=show_font)

    plt.xticks(x, x_axis, fontproperties=show_font, fontsize=8)  # 修改刻度
    plt.xlabel("乡镇", fontproperties=show_font)
    plt.ylabel("各乡镇住户量(户)", fontproperties=show_font)
    plt.title(settings.BAR_CHART_TITLE, fontproperties=show_font, fontsize=20)

    plt.savefig(settings.BAR_CHART_FILE)
    print("Draw bar chart finished.")
    # plt.show()


def mat_pie_chart(x_axis, y_axis):  # 饼图
    '''
    http://matplotlib.org/api/pyplot_api.html?highlight=pie#matplotlib.pyplot.pie

    x:name
    y:num

    '''
    plt.figure(figsize=(8, 4))
    show_font = mfm.FontProperties(fname=settings.FONT_PATH_FILE)

    colors = ['r', 'y', 'lightskyblue', 'g', 'c', '#3a9bff', 'm', 'pink']
    # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0, 0, 0, 0.05, 0, 0, 0, 0)
    # patches,town_text,p_text
    town_text = plt.pie(y_axis, explode=explode, labels=x_axis, colors=colors,
                        labeldistance=1.1, autopct='%3.2f%%', shadow=False,
                        startangle=90, pctdistance=0.6)

    for town in town_text[1]:
        town.set_fontproperties(show_font)
        town.set_size(8)

    plt.axis('equal')
    plt.legend(prop=show_font, fontsize=4, loc=0)
    plt.title(settings.PIE_CHART_TITLE, fontproperties=show_font, fontsize=16)
    plt.savefig(settings.PIE_CHART_FILE)
    print("Draw pie chart finished.")
    # plt.show()

if __name__ == '__main__':

    print "PHP is the best programming language."
    detail_spider()
    print "开始读取文件并获得详细信息."
    get_info_main()
    # 获取各乡镇户数信息
    fam_info = get_family_info()
    y_axis_total = []
    for item in fam_info:
        y_axis_total.append(item[1])

    # 获取各乡镇贫困户信息
    poverty_num_list = get_poverty_info()
    x_axis = []
    y_axis = []
    for item in poverty_num_list:
        x_axis.append(item[0])
        y_axis.append(item[1])

    print "开始绘图……"

    try:
        mat_bar_chart(x_axis, y_axis, y_axis_total)
    except Exception as e:
        raise e

    try:
        mat_pie_chart(x_axis, y_axis)
    except Exception as e:
        raise e
