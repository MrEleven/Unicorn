#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

from config import db
from datetime import datetime

def add_user(login_name, nick_name, password):
    """增加新用户"""
    create_time = datetime.now()
    sql = "insert into user (phone, nick_name, password, create_time) values (%s, %s, %s, %s);"
    return db.execute(sql, login_name, nick_name, password, create_time)

def get_member_by_login_name(login_name):
    """根据login_name获取用户"""
    sql = "select * from member where login_name = %s;"
    return db.query(sql,login_name)
