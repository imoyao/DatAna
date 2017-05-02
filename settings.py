#!/usr/bin/env python
# -*- coding: utf-8 -*-


POVERTY_NUM = 9515  # 贫穷户数（2016）
# AREA_POVERTY_LINE = str("{:.2f}".format(POVERTY_NUM/float(CENSUS_NUM)*100))+"%"

TARGET_URL = 'http://www.snchangwu.gov.cn/zjzw/xzgk.htm'

INPUT_FILE_PATH = './statics/infiles/'

OUTPUT_FILE_PATH = './statics/outfiles/'

FONT_FILE_PATH = './statics/fonts/'

BAR_CHART_TITLE = "长武县各乡镇贫困信息概览图"
PIE_CHART_TITLE = '各乡镇贫困户占比'


DETAIL_INFO_FILE_NAME = "detail_info.json"
TARGET_JSON_FILE_NAME = "town_data.json"
PIE_CHART_FILE_NAME = "pie_out_put.png"
BAR_CHART_FILE_NAME = "bar_out_put.png"
EXCEL_FILE_NAME = 'foo_data.xlsx'

FONT_FILE_NAME = 'msyh.ttf'

DETAIL_FILE = OUTPUT_FILE_PATH + DETAIL_INFO_FILE_NAME
TARGET_JSON_FILE = OUTPUT_FILE_PATH + TARGET_JSON_FILE_NAME
PIE_CHART_FILE = OUTPUT_FILE_PATH + PIE_CHART_FILE_NAME
BAR_CHART_FILE = OUTPUT_FILE_PATH + BAR_CHART_FILE_NAME

EXCEL_PATH_FILE = INPUT_FILE_PATH + EXCEL_FILE_NAME

FONT_PATH_FILE = FONT_FILE_PATH + FONT_FILE_NAME


'''
判断文件是否存在

import os
r_file = settings.READ_FILE
def readFile():
	if not os.path.isfile(r_file):
		print "{} not exits.".format(r_file)
	else:
		try:
			with open(r_file,"r") as f:
				content = f.read()
				print content
		except Exception as e:
			raise e
def writeFile():
	mystr = "hello,world."
	w_file = settings.WRITE_FILE
	dir_name,file_name = os.path.split(w_file)[0],os.path.split(w_file)[1]
	if not os.path.exists(dir_name):
		os.makedirs(r"{}".format(dir_name))
		with open(w_file,"w") as f:
			f.write(mystr)
	else:
		with open(w_file,"w") as f:
			f.write(mystr)
	print "write file finished."

'''