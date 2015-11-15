#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-25
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db
from datetime import datetime
import goal_status

def add_goal(user_id, name, image, description):
    """增加目标"""
    create_time = datetime.now()
    sql = "insert into goal (user_id, name, image, create_time, status, description) values (%s, %s, %s, %s, %s);"
    return db.execute(sql, user_id, name, image, create_time, goal_status.UNFINISH, description)

def get_goal_list(user_id):
    """获取目标列表"""
    sql = "select id, name, image, description from goal where user_id = %s and status != %s;"
    return db.query(sql, user_id, goal_status.DELETE)

def delete_goal(goal_id):
    """删除目标"""
    sql = "update goal set status = %s where id = %s;"
    return db.execute(sql, goal_status.DELETE, goal_id)

def update_goal(goal_id, name="", image="", description=""):
    """更新目标"""
    update_key_list = []
    update_value_list = []
    if name:
        update_key_list.append("name")
        update_value_list.append(name)
    if image:
        update_key_list.append("image")
        update_value_list.append(image)
    if description:
        update_key_list.append("description")
        update_value_list.append(description)
    if not len(update_key_list):
        return
    update_cond_tmp = [key + " = %s" for key in update_key_list]
    update_prefix = ", ".join(update_cond_tmp)
    sql = "update goal set " + update_prefix + " where id = %s;"
    update_value_list.append(goal_id)
    return db.execute(sql, *update_value_list)

def check_owner(user_id, goal_id):
    """验证目标Id和用户Id是否相匹配"""
    sql = "select id from goal where id = %s and user_id = %s;"
    return db.query(sql, goal_id, user_id)

