#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2016-02-21
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime
import random

def add_bg(url, image_type=1):
    """增加背景图片"""
    if not url.strip():
        return 0
    sql = "insert into bg (url, type, status, create_time) values (%s, %s, 1, %s);"
    return db.execute(sql, url, image_type, datetime.now())

def get_bg_list(image_type=1):
    """获取背景图片列表"""
    sql = "select * from bg where status = 1 and type = %s;"
    return db.query(sql, image_type)

def get_random_bg(image_type=1):
    """获取一张随机背景图片"""
    sql = "select count(*) as count from bg where status = 1 and type = %s;"
    count = db.query(sql, image_type)[0]["count"]
    start = random.randint(0, count-1)
    sql = "SELECT * FROM bg WHERE status =1 and type = %s LIMIT %s,1;"
    return db.query(sql, image_type, start)[0]["url"]
