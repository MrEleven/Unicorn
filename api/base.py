#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-11
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from datetime import datetime
from util import to_utf8
import json

class BaseHandler(tornado.web.RequestHandler):
    """api的基类型"""
    def get_current_user(self):
        return self.get_secure_cookie("session_id")

    def render_json(self, json_obj):
        """渲染json"""
        def to_json(model):
            """将datetime类型转化成str"""
            if isinstance(model, list):
                return [to_json(submodel) for submodel in model]
            for key, value in model.iteritems():
                if isinstance(value, datetime):
                    model[key] = to_utf8(value)
            return model
        json_obj = to_json(json_obj)
        self.set_header("Content-Type", "text/json")
        return self.write(json.dumps(json_obj))
