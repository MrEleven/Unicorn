#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from page.pagebase import PageHandler
import service.user_service as user_service
import service.marker_service as marker_service

class TestHandler(PageHandler):
    def get(self):
        return self.render("test.html")

class ListHandler(PageHandler):
    """签到列表"""
    def get(self):
        page_size = self.get_argument("page_size", 30) # 先不做分页
        marker_list = marker_service.get_marker_list(last_id=0, page_size=int(page_size))
        current_user_id = self.get_current_user()
        current_user_info = user_service.get_user(current_user_id)
        self.render("marker_list.html", result={
            "marker_list": marker_list, 
            "current_user_id": current_user_id, 
            "current_user_info": current_user_info
        })

class AddHandler(PageHandler):
    """增加新签到"""
    @tornado.web.authenticated
    def get(self):
        return self.redirect("/marker/list")

    @tornado.web.authenticated
    def post(self):
        marker = self.get_argument("marker", "")
        if not marker:
            return self.render_string("内容不能为空")
        user_id = self.get_current_user()
        marker_service.add_marker("", marker, user_id)
        return self.redirect("/marker/list")
