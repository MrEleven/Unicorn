#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-10
# Author: July
# Email : julycw@gmail.com

from page.pagebase import PageHandler
import service.user_service as user_service
import service.marker_service as marker_service
import service.todo_service as todo_service
import random
import re
    

class LoginHandler(PageHandler):
    """登陆"""
    def get(self):
        next_url = self.get_argument("next", "")
        if not next_url:
            next_url = "/marker/list"
        if self.get_current_user():
            return self.redirect(next_url)
        self.render("login.html", result={"next_url": next_url})
        
    def post(self):
        phone = self.get_argument("phone", "")
        password = self.get_argument("password", "")
        next_url = self.get_argument("next_url", "")
        if not next_url:
            next_url = "/marker/list"
        if phone == "" or password == "":
            return self.redirect("/user/login")
        user_id = user_service.checkout_login(phone, password)
        if user_id:
            self.set_user_id(str(user_id))
            return self.redirect(next_url)
        else:
            msg = "手机号或密码错误"
            return self.render("login.html", result={"phone": phone, "msg": msg})

class RegistHandler(PageHandler):
    """注册"""
    def get(self):
        """注册，先这么简单弄一下，以后要加上短信和邮箱验证，和上传头像"""
        self.render("regist.html")

    def post(self):
        phone = self.get_argument("phone", "")
        email = self.get_argument("email", "")
        nickname = self.get_argument("nickname", "")
        password = self.get_argument("password", "")
        validate_result, msg = self._validate_params(phone, email, nickname, password)
        if not validate_result:
            result={"phone": phone, "email": email, "nickname": nickname, "msg": msg}
            return self.render("regist.html", result=result)
        avatar_url = self.gen_avatar_url()
        user_id, msg = user_service.add_user(phone, email, nickname, avatar_url, password)
        if not user_id:
            result={"phone": phone, "email": email, "nickname": nickname, "msg": msg}
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

class UserHandler(PageHandler):
    """用户页面"""
    def get(self):
        user_id = self.get_argument("user_id", 0)
        if not user_id:
            self.finish()
        user_info = user_service.get_user(user_id)
        # 签到列表
        marker_list = marker_service.get_marker_list(last_id=0, page_size=30, user_id=user_id)
        current_user_id = self.get_current_user()
        current_user_info = user_service.get_user(current_user_id)
        return self.render("user.html", result={"user_id": user_id, "user_info": user_info, "marker_list": marker_list, "current_user_id": current_user_id, "current_user_info": current_user_info})

class RecentHandler(PageHandler):
    """最近在干什么页面"""
    def get(self):
        user_id = self.get_argument("user_id", 0)
        if not user_id:
            self.finish()
        user_info = user_service.get_user(user_id)
        timeline_info = todo_service.recent_finish_todo(user_id)
        return self.render("recent.html", result={"user_id": user_id, "user_info": user_info, "timeline_info": timeline_info})
        
