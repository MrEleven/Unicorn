#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

import tornado.web
import module.member_ctrl as member_ctrl
import utils.utils as utils

class LoginHandler(tornado.web.RequestHandler):
    """登陆"""
    def get(self):
        self.render("login.html")

    def post(self):
        login_name = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if login_name == "" or password == "":
            return self.redirect("/member/login")
        user = member_ctrl.get_member_by_login_name(login_name)
        if len(user) == 0:
            return self.redirect("/member/login")

        if user[0].password != utils.md5(password):
            return self.redirect("/member/login")
            
        # todo: record session and update last login ip/time
        return self.redirect("/marker/list")

class RegisterHandler(tornado.web.RequestHandler):
    """注册"""
    def get(self):
        self.render("register.html")

    def post(self):
        login_name = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if login_name == "" or password == "":
            return self.redirect("/member/register")

        nick_name = self.get_argument("nickname", "")
        member_ctrl.add_member(login_name, nick_name, utils.md5(password))
        return self.redirect("/member/login")

class LogoutHandler(tornado.web.RequestHandler):
    """登出"""
    def get(self):
        # todo: clear session for safety logout
        return self.redirect("/member/logout")


