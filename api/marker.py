#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
import module.marker_ctrl as marker_ctrl

class ListHandler(tornado.web.RequestHandler):
    """签到列表"""
    def get(self):
        page = self.get_argument("page", 1)
        page_size = self.get_argument("page_size", 10)
        marker_list = marker_ctrl.get_marker_list(int(page), int(page_size))
        self.render("marker_list.html", marker_list=marker_list)

class AddHandler(tornado.web.RequestHandler):
    """增加新签到"""
    def post(self):
        print "hello world"


