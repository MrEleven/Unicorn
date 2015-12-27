#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © meishixing.com
# Date  : 2014-03-25
# Author: Master Yumi
# Email : <yumi@meishixing.com>
#
# Distributed under terms of the MIT license.


import time
from datetime import datetime
from random import randint
from oss.oss_api import *
from cStringIO import StringIO
from config import ID, KEY, BUCKET, BASE_URL, UNICORN_PATH

oss = OssAPI("oss.aliyuncs.com", ID, KEY)

def upload_pic(image):
    """上传图片到阿里云
    localname: 本地图片名称
    file_name: 上传后的地址
    """
    def gen_image_name():
        """生成图片文件名"""
        back_fix = ".jpg"
        today = datetime.now().strftime("%Y/%m/%d/%H%M%S")
        random_str = str(randint(100000, 999999))
        return UNICORN_PATH +  today + random_str + back_fix
    file_name = gen_image_name()
    content_type = image[0]["content_type"]
    image = image[0]["body"]
    content = image

    if not _upload_pic(content, file_name, content_type):
        if not _upload_pic(content, file_name, content_type):
            return ''
    return BASE_URL + file_name

def _upload_pic(pic, file_name, content_type):
    """上传图片
    """
    res = oss.put_object_from_string(BUCKET, file_name, pic, content_type=content_type)
    if res.status != 200:
        return ''
    return file_name
