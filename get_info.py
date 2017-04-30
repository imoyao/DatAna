#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import re

from dataspider import read_file

town_data_json = {}
town_data_dict = {}

def read_json_info():
	with open('info.json', 'r') as f:
		info_str = json.load(f)  
		# print type(info_str)
		info_key_list = info_str.keys()
		return info_key_list
	
def re_file(town_name,info_str):
	'''一个汉字占3个字符'''
	family_info = re.search( r'(\d+户)', info_str, re.M|re.I).group()
	people_info = re.search( r'(\d+人|\d+万人|\d+\.\d+万人)', info_str, re.M|re.I).group()
	part_info = re.search( r'(\d+平方公里|\d+\.\d+平方公里)', info_str, re.M|re.I).group()
	faminly_num = int(family_info[:-3])	#
	# people_info = "2.1万人"
	people_raw = people_info[:-3]
	if people_raw.isdigit():
		people_num = int(people_raw)
	else:
		people_num = int(float(people_raw[:-3])*10000)
	part_area = float(part_info[:-12])
	global town_data_dict
	town_data_dict["faminly_num"] = faminly_num
	town_data_dict["people_num"] = people_num
	town_data_dict["part_area"] = part_area
	
	# print town_data_dict
	town_data_json[town_name] = town_data_dict

	# print town_data_json
	# return town_data_json
	# print part_area
	# print people_num

def get_json_data():
	info_key_list = read_json_info()
	for item in info_key_list:	#TODO
		town_name_temp = item.encode("utf-8")	#str key
		file_name = town_name_temp + ".txt"	#TODO
		info_str = read_file(file_name)
		town_name = town_name_temp[:-6]
		print town_name
		print type(town_name)
		re_file(town_name,info_str)
		print "********"
	with open('hello.json', 'w') as f:
		json.dump(town_data_json, f)
	print type(town_data_json)
	print "数据已正常写入,打开看看吧"
	
if __name__ == '__main__':
	get_json_data()
# print town_data_json