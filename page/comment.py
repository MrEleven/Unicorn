#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-17
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from page.pagebase import PageHandler
import service.marker_service as marker_service
import service.comment_service as comment_service

class ListHandler(PageHandler):
    """评论列表"""
    def get(self):
        marker_id = self.get_argument("marker_id", 0)
        page = self.get_argument("page", 1)
        page_size = self.get_argument("page_size", 200) # 数据量小，先不做分页
        comment_list = comment_service.get_comment_list(int(marker_id), int(page), int(page_size))
        self.render_json(comment_list)


class AddHandler(PageHandler):
    """增加评论"""
    @tornado.web.authenticated
    def post(self):
        marker_id = self.get_argument("marker_id", 0)
        content = self.get_argument("content", "")
        if not(content and marker_id):
            return self.write("系统异常")
        user_id = self.get_current_user()
        comment_service.add_comment(user_id, marker_id, content)
        marker_service.inc_comment_count(marker_id)
        # return self.write("评论成功")
        
