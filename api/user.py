#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2016-09-02
# Author: Master Yumi
# Email : yumi@meishixing.com

from api.apibase import APIHandler
import tornado.web
import service.user_service as user_service

class IsRegistedHandler(APIHandler):
    """检查是否已经注册"""
    def post(self):
        phone = self.get_argument("phone", None)
        if phone:
            user_id = user_service.is_phone_exist(phone)
            json_obj = {"user_id": user_id}
            return self.render_json(json_obj)
        nickname = self.get_argument("nickname", None)
        if nickname:
            user_id = user_service.is_name_exist(nickname)
            json_obj = {"user_id": user_id}
            return self.render_json(json_obj)

