#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-17
# Author: Master Yumi
# Email : yumi@meishixing.com

import module.comment_ctrl as comment_ctrl

def get_comment_list(marker_id, page=1, page_size=100):
    """获取评论列表"""
    return comment_ctrl.get_comment_list(marker_id, page, page_size)

def get_comment_info(comment_id):
    """获取评论列表"""
    return comment_ctrl.get_comment_info(comment_id)

def add_comment(user_id, marker_id, content, reply=0, reply_user=0):
    """增加评论"""
    return comment_ctrl.add_comment(user_id, marker_id, content, reply, reply_user)

def get_comment_user(comment_id):
    """获取某个评论的用户Id"""
    return comment_ctrl.get_comment_user(comment_id)
