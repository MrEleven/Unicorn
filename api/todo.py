#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-13
# Author: Master Yumi
# Email : yumi@meishixing.com

from api.apibase import APIHandler
import tornado.web
import module.todo_ctrl as todo_ctrl

class AddHandler(APIHandler):
    """增加TODO"""
    @tornado.web.authenticated
    def post(self):
        user_id = self.get_current_user()
        goal_id = self.get_argument("goal_id", 0)
        name = self.get_argument("name", "")
        note = self.get_argument("note", "")
        todo_id = todo_ctrl.add_todo(user_id, goal_id, name, note)
        return self.render_json(todo_id)


class ListHandler(APIHandler):
    """获取todo列表"""
    def get(self):
        goal_id = self.get_argument("goal_id", 0)
        if not goal_id:
            return self.render_json([])
        todo_list = todo_ctrl.get_todo_list(goal_id)
        return self.render_json(todo_list)
