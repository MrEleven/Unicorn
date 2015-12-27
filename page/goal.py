#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-24
# Author: Master Yumi
# Email : yumi@meishixing.com

from page.pagebase import PageHandler
import tornado.web
import service.goal_service as goal_service


class AddHandler(PageHandler):
    """增加目标"""
    @tornado.web.authenticated
    def post(self):
        user_id = self.get_current_user()
        name = self.get_argument("name", "")
        image = self.get_argument("image", "")
        description = self.get_argument("description", "")
        goal_id = goal_service.add_goal(user_id, name, image, description)
        return self.write(str(goal_id))

class ListHandler(PageHandler):
    """获取目标列表"""
    @tornado.web.authenticated
    def get(self):
        user_id = self.get_argument("user_id", 0)
        if not user_id:
            user_id = self.get_current_user()
        if not user_id:
            goal_list = []
        else:
            user_id = int(user_id)
            goal_list = goal_service.get_goal_list(user_id)
        return self.render("goal_list.html", result={"goal_list": goal_list})

class UpdateHandler(PageHandler):
    """更新目标"""
    @tornado.web.authenticated
    def post(self):
        goal_id = self.get_argument("goal_id")
        if not goal_id:
            raise Exception("goal/update msg: goal_id cant be %s" % goal_id)
        user_id = self.get_current_user()
        if not goal_service.check_owner(user_id, int(goal_id)):
            raise Exception("user_id: %s want to update goal(id: %s) raise no permission Exception")
        name = self.get_argument("name")
        image = self.get_argument("image")
        description = self.get_argument("description")
        rst = goal_service.update_goal(int(goal_id), name, image, description)
        return self.write(str(rst))
