#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-21
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def get_message_list(user_id, start_time=None, count=20):
    """获取消息列表"""
    sql = "select id, marker_id, comment_id, receiver_id, create_time from message where receiver_id = %s order by id desc"
    values = [user_id]
    if start_time:
        sql = sql + " and create_time < %s "
        values.append(start_time)
    sql = sql + " limit %s;"
    values.append(count)
    return db.query(sql, *values)

def add_message(markder_id, comment_id, receiver_id):
    """增加消息"""
    create_time = datetime.now()
    sql = "insert into message (marker_id, comment_id, receiver_id, create_time) values (%s, %s, %s, %s);"
    return db.execute(sql, markder_id, comment_id, receiver_id, create_time)

