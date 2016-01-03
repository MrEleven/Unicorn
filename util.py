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
    mobile_agent = ['iphone', 'android', 'phone', 'mobile', 'wap', 'netfront', 'java', 'opera mobi', 'opera mini',
      'ucweb', 'windows ce', 'symbian', 'series', 'webos', 'sony', 'blackberry', 'dopod', 'nokia', 'samsung',   
      'palmsource', 'xda', 'pieplus', 'meizu', 'midp', 'cldc', 'motorola', 'foma', 'docomo', 'up.browser',   
      'up.link', 'blazer', 'helio', 'hosin', 'huawei', 'novarra', 'coolpad', 'webos', 'techfaith', 'palmsource',   
      'alcatel', 'amoi', 'ktouch', 'nexian', 'ericsson', 'philips', 'sagem', 'wellcom', 'bunjalloo', 'maui', 'smartphone',   
      'iemobile', 'spice', 'bird', 'zte-', 'longcos', 'pantech', 'gionee', 'portalmmm', 'jig browser', 'hiptop',   
      'benq', 'haier', '^lct', '320x320', '240x320', '176x220']
    for agent in mobile_agent:
        if user_agent.find(agent) > 0:
            return True
    return False

