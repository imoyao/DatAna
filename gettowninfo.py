#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import re

import settings

from dataspider import read_file

town_data_dict = {}
town_info_list = []
name_list = []


def read_json_info(r_json_file_name):
    with open(r_json_file_name, 'r') as f:
        info_str = json.load(f)
        # print type(info_str)
        # info_key_list = info_str.keys()   #TODO
        return info_str


def write_json_info(w_file_name, json_data):
    with open(w_file_name, 'w') as f:
        json.dump(json_data, f)


def get_json_data():
    '''
    正则匹配到数据：
    ('4980户', '2.1万人', '118.7平方公里')
    ………………
    ('2587户', '10543人', '32.9平方公里')
    :param town_name: str
    :param info_str: str
    :return: 拼接、组装，最后返回dict
    '''
    info_key_list = read_json_info(settings.DETAIL_FILE).keys()  # TODO

    for item in info_key_list:
        file_name = item + ".txt"
        town_name = item[:-2].encode("utf-8")  # key
        name_list.append(town_name)
        info_str = read_file(file_name)

        family_info = re.search(r'(\d+户)', info_str, re.M | re.I).group()
        people_info = re.search(
            r'(\d+人|\d+万人|\d+\.\d+万人)', info_str, re.M | re.I).group()
        part_info = re.search(r'(\d+平方公里|\d+\.\d+平方公里)',
                              info_str, re.M | re.I).group()
        family_num = int(family_info[:-3])  # note: 一个汉字占3个字符    #TODO
        people_raw = people_info[:-3]
        if people_raw.isdigit():  # 类型转换
            people_num = int(people_raw)
        else:
            people_num = int(float(people_raw[:-3])*10000)
        part_area = float(part_info[:-12])

        global town_data_dict
        town_data_dict["family_num"] = family_num
        town_data_dict["people_num"] = people_num
        town_data_dict["part_area"] = part_area
        town_info_list.append(town_data_dict)
        town_data_dict = {}  # NOTES:clear it is important!!!

    town_data_json = dict(zip(name_list, town_info_list))  # 组装json数据
    return town_data_json


def get_info_main():
    town_data_json = get_json_data()
    write_json_info(settings.TARGET_JSON_FILE, town_data_json)
    print "数据已正常写入{},打开看看吧.".format(settings.TARGET_JSON_FILE)

if __name__ == '__main__':
    get_info_main()
