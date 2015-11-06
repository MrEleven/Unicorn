#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

from page.pagebase import PageHandler
import module.user_ctrl as user_ctrl
import random
import re

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
    if ismobile:
        background_list = mobile_bg_list
    index = random.randint(0, len(background_list) - 1)
    return background_list[index]
    

class LoginHandler(PageHandler):
    """登陆"""
    def get(self):
        if self.get_current_user():
            return self.redirect("/marker/list")
        background = gen_background(self.check_mobile())
        self.render("login.html", result={"background": background})

    def check_mobile(self):
        user_agent = self.request.headers.get("User-Agent", "").lower()
        if user_agent.find("android") > 0:
            return True
        if user_agent.find("iphone") > 0:
            return True
        return False
        
    def post(self):
        phone = self.get_argument("phone", "")
        password = self.get_argument("password", "")
        if phone == "" or password == "":
            return self.redirect("/user/login")
        user_id = user_ctrl.checkout_login(phone, password)
        if user_id:
            self.set_user_id(str(user_id))
            return self.redirect("/marker/list")
        else:
            msg = "手机号或密码错误"
            background = gen_background()
            return self.render("login.html", result={"phone": phone, "msg": msg, "background": background})

class RegistHandler(PageHandler):
    """注册"""
    def get(self):
        """注册，先这么简单弄一下，以后要加上短信和邮箱验证，和上传头像"""
        background = gen_background()
        self.render("regist.html", result={"background": background})

    def post(self):
        background = gen_background()
        phone = self.get_argument("phone", "")
        email = self.get_argument("email", "")
        nickname = self.get_argument("nickname", "")
        password = self.get_argument("password", "")
        validate_result, msg = self._validate_params(phone, email, nickname, password)
        if not validate_result:
            result={"phone": phone, "email": email, "nickname": nickname, "msg": msg, "background": background}
            return self.render("regist.html", result=result)
        avatar_url = self.gen_avatar_url()
        user_id, msg = user_ctrl.add_user(phone, email, nickname, avatar_url, password)
        if not user_id:
            result={"phone": phone, "email": email, "nickname": nickname, "msg": msg, "background": background}
            return self.render("regist.html", result=result)
        return self.redirect("/user/login")

    def _validate_params(self, phone, email, nickname, password):
        """验证参数的有效性"""
        # check phone
        pattern = re.compile("^[1][358][0-9]{9}$", re.IGNORECASE)
        if not pattern.match(phone):
            return False, "手机号填写错误"
        # check email
        pattern = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
        if not pattern.match(email):
            return False, "Email格式错误"
        # check password
        if len(password) < 6:
            return False, "密码必须大于6位"
        return True, "验证成功"

    def gen_avatar_url(self):
        """随机选择一个头像"""
        fix_avatar_list = [
            "http://image.lanrenzhoumo.com/leo/img/20151011024819_18199bd27cd7a6ac8cebf4bdf45fb070.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151011025414_a27de62e3ee2e3fdfd2b4e7d987f18da.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151011025547_29c0c0f96f0db2cc28553c806e1efc0f.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151011025708_8be0a8a0ea1e9a827b54bfed38fc94a8.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151017231014_cf7d11a4fe95062cf4dcd09332c44bc1.jpeg",
            "http://image.lanrenzhoumo.com/leo/img/20151017231546_24f8086859e20bfacab7b082a3959329.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151017231621_74990d5e6fee8d9e2a8d4ab2a4f7a150.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151017231626_af3ea4549c1984d00a088e958e85cddc.png",
            "http://image.lanrenzhoumo.com/leo/img/20151017231655_cc3aed24a302a18a9cf869a9186f0831.jpg",
            "http://image.lanrenzhoumo.com/leo/img/20151017231814_8f94e8dbe27c467f18ca44225377a971.jpeg",
            "http://image.lanrenzhoumo.com/leo/img/20151011163317_07b20ebf75bf2e730f79621d5afd8afd.jpg",
        ]
        return fix_avatar_list[random.randint(0, len(fix_avatar_list)-1)]
        

class LogoutHandler(PageHandler):
    """登出"""
    def get(self):
        self.clear_cookie("session_id")
        return self.redirect("/user/login")


