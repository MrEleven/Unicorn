#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def check_user_marked(user_id, start_time):
    """检查用户是否已经签到过"""
    sql = "select create_time from marker where user_id = %s and create_time > %s;"
    return db.query(sql, user_id, start_time)

def get_marker_list(last_id=0, page_size=10):
    if not last_id:
        last_id = 99999999
    sql = "select marker.id, title, nickname, avatar_url, marker, create_time, user_id, comment_count from marker, user where user.id = marker.user_id and marker.id < %s order by marker.id desc limit %s;"
    return db.query(sql, last_id, page_size)

def add_marker(title, marker, user_id):
    """增加新的签到"""
    create_time = datetime.now()
    sql = "insert into marker (title, marker, user_id, create_time) values (%s, %s, %s, %s);"
    return db.execute(sql, title, marker, user_id, create_time)

def inc_comment_count(marker_id):
    """增加评论信息"""
    sql = "update marker set comment_count = comment_count + 1 where id = %s;"
    return db.execute(sql, marker_id)

def min_comment_count(marker_id):
    """减少评论数量"""
    sql = "update marker set comment_count = comment_count - 1 where id = %s;"
    return db.execute(sql, marker_id)

def get_marker_user(marker_id):
    """获取签到的用户Id"""
    if not marker_id:
        return 0
    sql = "select user_id from marker where id = %s;"
    result = db.query(sql, marker_id)
    if result:
        return result[0]["user_id"]
    return 0
