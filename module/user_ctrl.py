#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

from config import db
from datetime import datetime

def add_user(phone, email, nickname, avatar_url, password):
    """增加新用户"""
    regist_time = datetime.now()
    sql = "insert into user (phone, email, nickname, avatar_url, password, regist_time) values (%s, %s, %s, %s, %s, %s);"
    return db.execute(sql, phone, email, nickname, avatar_url, password, regist_time)

def checkout_login(phone, password):
    """先只支持手机号码登录吧"""
    sql = "select id from user where phone = %s and password = %s;"
    user_id = db.get(sql, phone, password)
    return user_id["id"] if user_id else 0

def get_user(user_id):
    """根据id获取用户"""
    sql = "select * from user where id = %s;"
    user = db.get(sql, user_id)
    return user
