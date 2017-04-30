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

import re

with open("亭口镇概况.txt","r") as f:

    line = f.read()

print type(line)
family_num = re.search( r'(\d+户)', line, re.M|re.I).group()
people_num = re.search( r'(\d+人|\d+万人|\d+\.\d+万人)', line, re.M|re.I).group()
total_area = re.search( r'(\d+平方公里|\d+\.\d+平方公里)', line, re.M|re.I).group()

print "familay num is {},perople num is {},total area is {}".format(family_num,people_num,total_area)