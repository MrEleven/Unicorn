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

class UpdateHandler(APIHandler):
    """更新todo"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/update msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_ctrl.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to update todo(id: %s) raise no permission Exception")
        goal_id = self.get_argument("goal_id", 0)
        name = self.get_argument("name", "")
        note = self.get_argument("note", "")
        result = todo_ctrl.update_todo(todo_id, goal_id, name, note)
        return self.render_json(result)

class DeleteHandler(APIHandler):
    """删除TODO"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/delete msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_ctrl.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to delete todo(id: %s) raise no permission Exception")
        result = todo_ctrl.delete_todo(todo_id)
        return self.render_json(result)

class FinishHandler(APIHandler):
    """完成某个TODO"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/finish msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_ctrl.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to finish todo(id: %s) raise no permission Exception")
        result = todo_ctrl.finish_todo(todo_id)
        return self.render_json(result)

class UnfinishHandler(APIHandler):
    """将某个TODO设置成未完成"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/unfinish msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_ctrl.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to unfinish todo(id: %s) raise no permission Exception")
        result = todo_ctrl.unfinish_todo(todo_id)
        return self.render_json(result)
        
            
