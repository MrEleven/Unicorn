#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-27
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from api.apibase import APIHandler
import module.image_ctrl as image_ctrl


class UploadHandler(APIHandler):
    """上传图片"""
    def post(self):
        """上传图片"""
        file = self.request.files.get("file", [])
        if not file:
            return self.render_json("")
        image_url = image_ctrl.upload_pic(file)
        return self.render_json(image_url)
        
