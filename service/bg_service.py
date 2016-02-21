#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2016-02-21
# Author: Master Yumi
# Email : yumi@meishixing.com

import module.bg_ctrl as bg_ctrl
import module.image_ctrl as image_ctrl

def upload_bg(image):
    """增加背景"""
    width, height = image_ctrl.get_image_size(image)
    image_type = 1
    if width < height:
        image_type = 2
    url = image_ctrl.upload_pic(image, dir_name="bg")
    if url:
        bg_ctrl.add_bg(url, image_type=image_type)
    return url

def get_bg_list(image_type=1):
    """获取背景列表"""
    return bg_ctrl.get_bg_list(image_type=image_type)

def get_random_bg(image_type=1):
    """获取一张随机背景图片"""
    return bg_ctrl.get_random_bg(image_type)
