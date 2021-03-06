#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-17
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from api.apibase import APIHandler
import service.marker_service as marker_service
import service.comment_service as comment_service
import service.user_service as user_service
import service.message_service as message_service

class ListHandler(APIHandler):
    """评论列表"""
    def get(self):
        marker_id = self.get_argument("marker_id", 0)
        page = self.get_argument("page", 1)
        page_size = self.get_argument("page_size", 200) # 数据量小，先不做分页
        comment_list = comment_service.get_comment_list(int(marker_id), int(page), int(page_size))
        for comment in comment_list:
            if comment["reply"]:
                comment["reply_user_info"] = user_service.get_user(comment["reply_user"])
        return self.render_json(comment_list)


class AddHandler(APIHandler):
    """增加评论"""
    @tornado.web.authenticated
    def post(self):
        marker_id = self.get_argument("marker_id", 0) or 0
        content = self.get_argument("content", "") or ""
        if not(content and marker_id):
            return self.write("系统异常")
        user_id = self.get_current_user()
        if content.startswith("@"):
            content = content.split(" ", 1)[-1]
            reply = self.get_argument("reply", 0) or 0
        else:
            reply = 0
        reply_user = comment_service.get_comment_user(reply)
        comment_id = comment_service.add_comment(user_id, marker_id, content, reply, reply_user)
        marker_service.inc_comment_count(marker_id)
        marker_user_id = marker_service.get_marker_user(marker_id)
        if int(marker_user_id) != user_id:
            message_service.add_message(marker_id, comment_id, marker_user_id)
        if reply and reply_user != user_id:
            message_service.add_message(marker_id, comment_id, reply_user)
        
