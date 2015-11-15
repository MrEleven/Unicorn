#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-24
# Author: Master Yumi
# Email : yumi@meishixing.com

from api.apibase import APIHandler
import tornado.web
import module.goal_ctrl as goal_ctrl


class AddHandler(APIHandler):
    """增加目标"""
    @tornado.web.authenticated
    def post(self):
        user_id = self.get_current_user()
        name = self.get_argument("name", "")
        image = self.get_argument("image", "")
        description = self.get_argument("description", "")
        goal_id = goal_ctrl.add_goal(user_id, name, image, description)
        return self.render_json(goal_id)


class ListHandler(APIHandler):
    """获取目标列表"""
    def get(self):
        user_id = self.get_argument("user_id", 0)
        if not user_id:
            user_id = self.get_current_user()
        if not user_id:
            goal_list = []
        else:
            user_id = int(user_id)
            goal_list = goal_ctrl.get_goal_list(user_id)
        return self.render_json(goal_list)


class UpdateHandler(APIHandler):
    """更新目标"""
    @tornado.web.authenticated
    def post(self):
        goal_id = self.get_argument("goal_id")
        if not goal_id:
            raise Exception("goal/update msg: goal_id cant be %s" % goal_id)
        user_id = self.get_current_user()
        if not goal_ctrl.check_owner(user_id, int(goal_id)):
            raise Exception("user_id: %s want to update goal(id: %s) raise no permission Exception")
        name = self.get_argument("name")
        image = self.get_argument("image")
        description = self.get_argument("description")
        rst = goal_ctrl.update_goal(int(goal_id), name, image, description)
        return self.render_json(str(rst))


class DeleteHandler(APIHandler):
    """删除目标"""
    @tornado.web.authenticated
    def post(self):
        goal_id = self.get_argument("goal_id")
        if not goal_id:
            raise Exception("goal/delete msg: goal_id cant be %s" % goal_id)
        user_id = self.get_current_user()
        if not goal_ctrl.check_owner(user_id, int(goal_id)):
            raise Exception("user_id: %s want to delete goal(id: %s) raise no permission Exception")
        rst = goal_ctrl.delete_goal(goal_id)
        return self.render_json(rst)
