#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-11
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """api的基类型"""
    def get_current_user(self):
        return self.get_secure_cookie("session_id")

    
