#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-13
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime
import todo_status
import module.todo_ctrl as todo_ctrl

def add_todo(user_id, goal_id, name="", note=""):
    """增加TODO"""
    return todo_ctrl.add_todo(user_id, goal_id, name, note)

def get_todo_list(goal_id):
    """获取某个目标得所有待办事项"""
    return todo_ctrl.get_todo_list(goal_id)

def delete_todo(todo_id):
    """删除TODO"""
    return todo_ctrl.delete_todo(todo_id)

def update_todo(todo_id, goal_id=0, name=None, note=None):
    """更新todo内容"""
    return todo_ctrl.update_todo(todo_id, goal_id, name, note)
    
def check_owner(user_id, todo_id):
    """验证TODOId和用户ID是否相匹配"""
    return todo_ctrl.check_owner(user_id, todo_id)

def finish_todo(todo_id):
    return todo_ctrl.finish_todo(todo_id)

def unfinish_todo(todo_id):
    return todo_ctrl.unfinish_todo(todo_id)

def recent_finish_todo(user_id, last_finish_time=""):
    """最近完成的todo列表"""
    tododata = todo_ctrl.recent_finish_todo(user_id, last_finish_time)
    result = []
    todo_map = {"date": None}
    for todo in tododata:
        close_date = str(todo["close_time"])[0:10]
        if not todo_map["date"] == close_date:
            date_str = todo["close_time"].strftime("%m月%d日")
            todo_map = {"date": close_date, "todolist": [], "date_str": date_str}
            result.append(todo_map)
        todo_map["todolist"].append(todo)
    return result

    
def postcard():
    """获取前10条当广播"""
    return todo_ctrl.postcard()
