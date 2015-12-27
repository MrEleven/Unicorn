#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-21
# Author: Master Yumi
# Email : yumi@meishixing.com

import module.message_ctrl as message_ctrl

def get_message_list(user_id, start_time=None, count=20):
    """获取消息列表"""
    return message_ctrl.get_message_list(user_id, start_time, count)

def add_message(markder_id, comment_id, receiver_id):
    """增加消息"""
    return message_ctrl.add_message(markder_id, comment_id, receiver_id)
