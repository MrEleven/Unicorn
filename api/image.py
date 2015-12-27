#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-27
# Author: Master Yumi
# Email : yumi@meishixing.com

from api.apibase import APIHandler
import service.image_service as image_service


class UploadHandler(APIHandler):
    """上传图片"""
    def post(self):
        """上传图片"""
        file = self.request.files.get("file", [])
        if not file:
            return self.render_json("")
        image_url = image_service.upload_pic(file)
        return self.render_json(image_url)
        
