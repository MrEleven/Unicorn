#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

import sys
import os
from importlib import import_module
import torndb

if len(sys.argv) < 2:
    print "usage: python unicorn.py CONFIGFILE"
    sys.exit(0)

    
config_file = sys.argv[-1]
dir_name, base_name = os.path.split(config_file)
module_name = base_name.split(".")[0]
dir_name = dir_name.replace("/", ".").replace("..", ".")
if dir_name[0] == ".":
    dir_name = dir_name[1:]
config_module = import_module(dir_name + "." + module_name)

db = torndb.Connection(**config_module.mysql_config)


