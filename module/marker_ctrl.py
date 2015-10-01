#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def get_marker_list(page=1, page_size=10):
    start = (page-1) * page_size
    sql = "select * from marker order by id desc limit %s, %s;"
    return db.query(sql, start, page_size)

def add_marker(title, marker):
    """增加新的签到"""
    create_time = datetime.now()
    sql = "insert into marker (title, marker, create_time) values (%s, %s, %s);"
    return db.execute(sql, title, marker, create_time)
    
