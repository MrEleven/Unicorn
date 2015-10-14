#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def get_user_marker_list(user_id, page=1, page_size=10):
    start = (page-1) * page_size
    sql = "select title, nickname, avatar_url, marker, create_time, user_id from marker, user where marker.user_id = %s and user.id = marker.user_id order by marker.id desc limit %s, %s;"
    return db.query(sql, user_id, start, page_size)

def get_marker_list(page=1, page_size=10):
    start = (page-1) * page_size
    sql = "select title, nickname, avatar_url, marker, create_time, user_id from marker, user where user.id = marker.user_id order by marker.id desc limit %s, %s;"
    return db.query(sql, start, page_size)

def add_marker(title, marker, user_id):
    """增加新的签到"""
    create_time = datetime.now()
    sql = "insert into marker (title, marker, user_id, create_time) values (%s, %s, %s, %s);"
    return db.execute(sql, title, marker, user_id, create_time)
    
