#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2016-02-21
# Author: Master Yumi
# Email : yumi@meishixing.com

from page.pagebase import PageHandler
import service.bg_service as bg_service

class BgHandler(PageHandler):
    """背景图片管理"""
    def get(self):
        pc_bg_list = bg_service.get_bg_list(image_type=1)
        mobile_bg_list = bg_service.get_bg_list(image_type=2)
        return self.render("eleven/bg.html", result={"pc_bg_list": pc_bg_list, "mobile_bg_list": mobile_bg_list})

    def post(self):
        image = self.request.files.get("image", [])
        if image:
            bg_service.upload_bg(image)
        return self.redirect(self.request.uri)

