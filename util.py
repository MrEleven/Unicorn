#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-11
# Author: Master Yumi
# Email : yumi@meishixing.com

import hashlib
from datetime import datetime

def md5(text):
    """md5加密"""
    return hashlib.md5(text).hexdigest()

def to_utf8(text):
    """将对象转化成str"""
    if isinstance(text, unicode):
        return text.encode("utf8")
    if isinstance(text, datetime):
        return text.strftime("%Y-%m-%d %H:%M:%S")    
    return str(text)

def check_mobile(self):
    user_agent = self.request.headers.get("User-Agent", "").lower()
    if user_agent.find("android") > 0:
        return True
    if user_agent.find("iphone") > 0:
        return True
    return False
