#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-25
# Author: Master Yumi
# Email : yumi@meishixing.com

import module.goal_ctrl as goal_ctrl

def add_goal(user_id, name, image, description):
    """增加目标"""
    return goal_ctrl.add_goal(user_id, name, image, description)

def get_goal_list(user_id):
    """获取目标列表"""
    return goal_ctrl.get_goal_list(user_id)

def delete_goal(goal_id):
    """删除目标"""
    return goal_ctrl.delete_goal(goal_id)

def update_goal(goal_id, name="", image="", description=""):
    """更新目标"""
    return goal_ctrl.update_goal(goal_id, name, image, description)

def check_owner(user_id, goal_id):
    """验证目标Id和用户Id是否相匹配"""
    return goal_ctrl.check_owner(user_id, goal_id)

