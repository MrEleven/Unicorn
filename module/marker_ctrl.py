#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def get_marker_list_by_user_id(user_id, page=1, page_size=10, orderby=1):
    start = (page-1) * page_size
    sql = "select marker.id, title, nickname, avatar_url, marker, create_time, user_id from marker, user where marker.user_id = %s and user.id = marker.user_id order by marker.id " + "desc" if orderby else "asc" + " limit %s, %s;"
    return db.query(sql, user_id, start, page_size)

def check_user_marked(user_id, start_time):
    """检查用户是否已经签到过"""
    sql = "select create_time from marker where user_id = %s and create_time > %s;"
    return db.query(sql, user_id, start_time)

def get_marker_list(page=1, page_size=10):
    start = (page-1) * page_size
    sql = "select marker.id, title, nickname, avatar_url, marker, create_time, user_id, comment_count from marker, user where user.id = marker.user_id order by marker.id desc limit %s, %s;"
    return db.query(sql, start, page_size)

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
