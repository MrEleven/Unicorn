#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-17
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime

def get_comment_list(marker_id, page=1, page_size=10):
    """获取评论列表"""
    start = (page - 1) * page_size
    sql = "select user_id, content, create_time, nickname, avatar_url, reply, reply_user from comment, user where comment.user_id = user.id and marker_id = %s limit %s, %s;"
    return db.query(sql, marker_id, start, page_size)

def get_comment_info(comment_id):
    """获取评论列表"""
    sql = "select user_id, content, create_time, nickname, avatar_url, reply, reply_user from comment, user where comment.user_id = user.id and comment.id = %s;"
    result = db.query(sql, comment_id)
    if result:
        return result[0]
    return None

def add_comment(user_id, marker_id, content, reply=0, reply_user=0):
    """增加评论"""
    create_time = datetime.now()
    sql = "insert into comment (marker_id, user_id, content, create_time, reply, reply_user) values (%s, %s, %s, %s, %s, %s);"
    return db.execute(sql, marker_id, user_id, content, create_time, reply, reply_user)

def get_comment_user(comment_id):
    """获取某个评论的用户Id"""
    if not comment_id:
        return 0
    sql = "select user_id from comment where id = %s;"
    result = db.execute(sql, comment_id)
    if result:
        return result["user_id"]
    return 0
