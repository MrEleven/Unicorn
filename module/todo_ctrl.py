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
    sql = "select id, name, goal_id, status, create_time, note from todo where goal_id = %s and status != %s order by status asc;"
    return db.query(sql, goal_id, todo_status.DELETE)

def delete_todo(todo_id):
    """删除TODO"""
    sql = "update todo set status = %s where id = %s;"
    return db.execute(sql, todo_id, todo_status.DELETE)

def update_todo(todo_id, goal_id=0, name=None, note=None):
    """更新todo内容"""
    update_key_list = []
    update_value_list = []
    if goal_id:
        update_key_list.append("goal_id")
        update_value_list.append(goal_id)
    if name:
        update_key_list.append("name")
        update_value_list.append(name)
    if note is not None:
        update_key_list.append("note")    
        update_value_list.append(note)
    update_cond_tmp = [key + " = %s" for key in update_key_list]
    update_prefix = ", ".join(update_cond_tmp)
    sql = "update todo set " + update_prefix + " where id = %s;"
    update_value_list.append(todo_id)
    return db.execute(sql, *update_value_list)

def check_owner(user_id, todo_id):
    """验证TODOId和用户ID是否相匹配"""
    sql = "select id from todo where id = %s and user_id = %s;"
    return db.query(sql, todo_id, user_id)

def finish_todo(todo_id):
    close_time = datetime.now()
    sql = "update todo set status = %s, close_time = %s where id = %s;"
    return db.execute(sql, todo_status.FINISHED, close_time, int(todo_id))

def unfinish_todo(todo_id):
    sql = "update todo set status = %s where id = %s;"
    return db.execute(sql, todo_status.UNFINISH, int(todo_id))

def recent_finish_todo(user_id, last_finish_time):
    """最近完成的todo列表"""
    if not last_finish_time:
        last_finish_time = "9999-11-11 11:11:11"
    sql = "select id, name, goal_id, status, create_time, note, close_time from todo where user_id = %s and status = %s and close_time < %s order by close_time desc;"
    return db.query(sql, user_id, todo_status.FINISHED, last_finish_time)

def postcard():
    """获取前10条当广播"""
    sql = "select todo.id, name, goal_id, status, create_time, user_id, nickname from todo, user where user.id = todo.user_id and todo.status = %s order by close_time desc limit 20;"
    return db.query(sql, todo_status.FINISHED)
