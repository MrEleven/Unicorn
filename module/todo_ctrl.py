#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-13
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime
import todo_status

def add_todo(user_id, goal_id, name="", note=""):
    """增加TODO"""
    create_time = datetime.now()
    sql = "insert into todo(user_id, goal_id, status, name, create_time, note) values (%s, %s, %s, %s, %s, %s);"
    return db.execute(sql, user_id, goal_id, todo_status.UNFINISH, name, create_time, note)


def get_todo_list(goal_id):
    """获取某个目标得所有待办事项"""
    sql = "select id, name, goal_id, status, create_time, note from todo where goal_id = %s;"
    return db.query(sql, goal_id)

def delete_todo(todo_id):
    """删除TODO"""
    sql = "delete from todo where id = %s;"
    return db.execute(sql, todo_id)

def update_todo(todo_id, goal_id=0, status=None, name=None, note=None):
    """更新todo内容"""
    update_key_list = []
    update_value_list = []
    if goal_id:
        update_key_list.append("id")
        update_value_list.append(goal_id)
    if name:
        update_key_list.append("name")
        update_value_list.append(name)
    if status is not None:
        update_key_list.append("status")
        update_value_list.append(status)
    if note is not None:
        update_key_list.append("note")    
        update_value_list.append(note)
    update_cond_tmp = [key + " = %s" for key in update_key_list]
    update_prefix = ", ".join(update_cond_tmp)
    sql = "update todo set " + update_prefix + " where id = %s;"
    update_value_list.append(todo_id)
    return db.query(sql, *update_value_list)
