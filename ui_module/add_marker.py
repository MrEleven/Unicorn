#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-18
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.web
from datetime import datetime, timedelta
import module.user_ctrl as user_ctrl
import module.marker_ctrl as marker_ctrl
from util import to_utf8, check_mobile

class AddMarkerUIModule(tornado.web.UIModule):
    """签到的输入框"""
    time_regular = {
        1 : {"hour": 4},   # 签到时间
        2 : {"hour": 12}   # 总结时间
    }

    def render(self):
        user_id = self.current_user
        has_marked = False
        has_marked_tips = ""
        if user_id:
            has_marked = self.check_marked(user_id)
            if has_marked:
                has_marked_tips = self.gen_marker_tips()
        template_path = "ui_module/add_marker.html"
        if check_mobile(self):
            template_path = "ui_module/mobile/add_marker.html"
        return self.render_string(template_path, result={"user_id": user_id, "has_marked": has_marked, "has_marked_tips": has_marked_tips})

    def get_current_time_block(self):
        """获取当前时间是签到时间还是总结时间"""
        hour = datetime.now().hour
        start_mark_time = self.time_regular[1]["hour"]
        end_mark_time = self.time_regular[2]["hour"]
        if hour < start_mark_time or hour >= end_mark_time:
            return 2    # 总结时间
        return 1

    def gen_marker_tips(self):
        """生成提醒信息"""
        current_block = self.get_current_time_block()
        if current_block == 1:
            return "您已经签到过了，不要忘记下午来做个总结。"
        else:
            return "您已经做过总结了，早点休息，记得明天继续努力。"

    def check_marked(self, user_id):
        """检查该用户是否已经签到 4:00 - 12:00 是签到时间, 4:00前或12:00后是总结时间"""
        now = datetime.now()
        # 获取当前是签到时间还是总结时间
        current_block = self.get_current_time_block()
        if current_block == 1:
            start_time = to_utf8(datetime.now())[:10] + " 04:00:00"
        elif now.hour < 4:
            start_time = to_utf8(now - timedelta(days=1))[:10] + " 12:00:00"
        else:
            start_time = to_utf8(now)[:10] + " 12:00:00"
        if marker_ctrl.check_user_marked(user_id, start_time):
            return True
        else:
            return False
