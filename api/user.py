#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

import tornado.web
import module.user_ctrl as user_ctrl
from util import md5
import random

class LoginHandler(tornado.web.RequestHandler):
    """登陆"""
    def get(self):
        self.render("login.html", result={})

    def post(self):
        phone = self.get_argument("phone", "")
        password = self.get_argument("password", "")
        if phone == "" or password == "":
            return self.redirect("/user/login")
        password_md5 = md5(password)
        user_id = user_ctrl.checkout_login(phone, password_md5)
        if user_id:
            self.set_secure_cookie("session_id", str(user_id))
            return self.redirect("/marker/list")
        else:
            msg = "手机号或密码错误"
            return self.render("login.html", result={"password": password,
                                                 "phone": phone, "msg": msg})

class RegistHandler(tornado.web.RequestHandler):
    """注册"""
    def get(self):
        """注册，先这么简单弄一下，以后要加上短信和邮箱验证，和上传头像"""
        self.render("regist.html", result={})

    def post(self):
        phone = self.get_argument("phone", "")
        email = self.get_argument("email", "")
        nickname = self.get_argument("nickname", "")
        password = self.get_argument("password", "")
        if phone == "" or password == "" or nickname == "" or email == "":
            msg = "注册信息不对"
            return self.redirect("/user/register", result={"phone": phone, "password": password, \
                                                           "email": email, "nickname": nickname, "msg": msg})
        avatar_url = self.gen_avatar_url()
        user_ctrl.add_user(phone, email, nickname, avatar_url, md5(password))
        return self.redirect("/user/login")

    def gen_avatar_url(self):
        """随机选择一个头像"""
        fix_avatar_list = ["http://image.lanrenzhoumo.com/leo/img/20151011024819_18199bd27cd7a6ac8cebf4bdf45fb070.jpg",
                           "http://image.lanrenzhoumo.com/leo/img/20151011025414_a27de62e3ee2e3fdfd2b4e7d987f18da.jpg",
                           "http://image.lanrenzhoumo.com/leo/img/20151011025547_29c0c0f96f0db2cc28553c806e1efc0f.jpg",
                           "http://image.lanrenzhoumo.com/leo/img/20151011025708_8be0a8a0ea1e9a827b54bfed38fc94a8.jpg"
        ]
        return fix_avatar_list[random.randint(0, len(fix_avatar_list)-1)]
        

class LogoutHandler(tornado.web.RequestHandler):
    """登出"""
    def get(self):
        # todo: clear session for safety logout
        return self.redirect("/user/logout")


