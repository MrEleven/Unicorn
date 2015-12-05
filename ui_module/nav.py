#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-17
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from datetime import datetime
import module.user_ctrl as user_ctrl
from util import to_utf8

class NavUIModule(tornado.web.UIModule):
    """导航栏"""
    def render(self):
        user_id = self.current_user
        greeting = ""
        user_info = {}
        if user_id:
            user_info = user_ctrl.get_user(user_id)
            greeting = self.gen_greeting(to_utf8(user_info["nickname"]))
        return self.render_string("ui_module/nav.html", result={"user_id": user_id, "greeting": greeting, "user_info": user_info})

    def gen_greeting(self, nickname):
        """生成问候语"""
        hour = datetime.now().hour
        if hour < 5:
            message = "晚安"
        elif hour < 9:
            message = "早上好"
        elif hour < 11:
            message = "上午好"
        elif hour < 14:
            message = "中午好"
        elif hour < 18:
            message = "下午好"
        elif hour < 23:
            message = "晚上好"
        else:
            message = "晚安"
        return message + "，" + nickname

    def javascript_files(self):
        """js文件加载"""
        return "/static/js/message.js"
