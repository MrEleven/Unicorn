#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

import module.user_ctrl as user_ctrl

def add_user(phone, email, nickname, avatar_url, password):
    """增加新用户"""
    return user_ctrl.add_user(phone, email, nickname, avatar_url, password)

def checkout_login(phone, password):
    """先只支持手机号码登录吧"""
    return user_ctrl.checkout_login(phone, password)

def get_user(user_id):
    """根据id获取用户"""
    return user_ctrl.get_user(user_id)
