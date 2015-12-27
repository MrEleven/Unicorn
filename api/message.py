#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-21
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from api.apibase import APIHandler
import service.message_service as message_service
import service.comment_service as comment_service

class ListHandler(APIHandler):
    """消息列表"""
    @tornado.web.authenticated
    def get(self):
        user_id = self.get_current_user()
        message_list = message_service.get_message_list(user_id)
        for message in message_list:
            comment_id = message["comment_id"]
            comment_info = comment_service.get_comment_info(comment_id)
            message["content"] = comment_info["content"]
            message["comment_user_id"] = comment_info["user_id"]
            message["comment_nickname"] = comment_info["nickname"]
        return self.render_json(message_list)
