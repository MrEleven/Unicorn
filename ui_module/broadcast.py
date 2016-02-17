#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2016-02-17
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from util import check_mobile
import service.todo_service as todo_service

class BroadcastUIModule(tornado.web.UIModule):
    """广播"""
    def render(self):
        todo_list = todo_service.broadcast()
        return self.render_string("ui_module/broadcast.html", result={"todo_list": todo_list})
