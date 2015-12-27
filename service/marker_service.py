#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

import module.marker_ctrl as marker_ctrl

def check_user_marked(user_id, start_time):
    """检查用户是否已经签到过"""
    return marker_ctrl.check_user_marked(user_id, start_time)

def get_marker_list(last_id=0, page_size=10, user_id=0):
    return marker_ctrl.get_marker_list(last_id, page_size, user_id)

def add_marker(title, marker, user_id):
    """增加新的签到"""
    return marker_ctrl.add_marker(title, marker, user_id)

def inc_comment_count(marker_id):
    """增加评论信息"""
    return marker_ctrl.inc_comment_count(marker_id)

def min_comment_count(marker_id):
    """减少评论数量"""
    return marker_ctrl.min_comment_count(marker_id)

def get_marker_user(marker_id):
    """获取签到的用户Id"""
    return marker_ctrl.get_marker_user(marker_id)
