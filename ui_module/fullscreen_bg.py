#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-07
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from util import check_mobile
import random
import service.bg_service as bg_service

def gen_background(ismobile=False):
    """随机生成背景图片"""
    background_list = [
        "http://image.lanrenzhoumo.com/leo/img/20151101104358_c3fe2c228b6710f7680c7b3a430a85b2.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151101105230_36ef607d73196da90b86bcc7dca58ee6.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151101105331_3e87ea432f1cc057416fb4341b5d720e.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151105100656_2cb55aa631eab011024215e3b11637db.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151105101014_030d7e8e966169ab4c7f67c291c333f4.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151105101104_5d88fa421e119f04cd5ce64e3cf7c3e4.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151105101150_8eed7b1e86c45cd880591743bd2195dd.jpg"
    ]
    mobile_bg_list = [
        "http://image.lanrenzhoumo.com/leo/img/20151106124713_f217091424054d7b761aa13c5da1bf0b.jpeg",
        "http://image.lanrenzhoumo.com/leo/img/20151106124842_413064d7fc717052d9a0f27e4b47ab2c.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151106125030_38e1553fc77a75f7a5fba3ca57588690.jpg",
        "http://image.lanrenzhoumo.com/leo/img/20151106125404_ac5d95d3e4c2874b132190e710c70d6a.jpg"
    ]
    # if ismobile:
    #     return ""
    # return "http://image.lanrenzhoumo.com/leo/img/20151223225125_3e87ea432f1cc057416fb4341b5d720e.jpg"
    if ismobile:
        background_list = mobile_bg_list
    index = random.randint(0, len(background_list) - 1)
    return background_list[index]

class FullScreenBGUIModule(tornado.web.UIModule):
    """背景图片"""
    def render(self):
        image_type = 1
        if check_mobile(self):
            image_type = 2
        background = bg_service.get_random_bg(image_type)
        return self.render_string("ui_module/fullscreen_bg.html", result={"background": background})
