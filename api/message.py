#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-21
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from api.apibase import APIHandler
import module.message_ctrl as message_ctrl
import module.comment_ctrl as comment_ctrl

class ListHandler(APIHandler):
    """消息列表"""
    @tornado.web.authenticated
    def get(self):
        user_id = self.get_current_user()
        message_list = message_ctrl.get_message_list(user_id)
        for message in message_list:
            comment_id = message["comment_id"]
            comment_info = comment_ctrl.get_comment_info(comment_id)
            message["content"] = comment_info["content"]
            message["comment_user_id"] = comment_info["user_id"]
            message["comment_nickname"] = comment_info["nickname"]
        return self.render_json(message_list)
