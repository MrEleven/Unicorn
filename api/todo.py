#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-11-13
# Author: Master Yumi
# Email : yumi@meishixing.com

from api.apibase import APIHandler
import tornado.web
import service.todo_service as todo_service

class AddHandler(APIHandler):
    """增加TODO"""
    @tornado.web.authenticated
    def post(self):
        user_id = self.get_current_user()
        goal_id = self.get_argument("goal_id", 0)
        name = self.get_argument("name", "")
        note = self.get_argument("note", "")
        todo_id = todo_service.add_todo(user_id, goal_id, name, note)
        return self.render_json(todo_id)


class ListHandler(APIHandler):
    """获取todo列表"""
    def get(self):
        goal_id = self.get_argument("goal_id", 0)
        if not goal_id:
            return self.render_json([])
        todo_list = todo_service.get_todo_list(goal_id)
        return self.render_json(todo_list)

class UpdateHandler(APIHandler):
    """更新todo"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/update msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_service.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to update todo(id: %s) raise no permission Exception")
        goal_id = self.get_argument("goal_id", 0)
        name = self.get_argument("name", "")
        note = self.get_argument("note", "")
        result = todo_service.update_todo(todo_id, goal_id, name, note)
        return self.render_json(result)

class DeleteHandler(APIHandler):
    """删除TODO"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/delete msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_service.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to delete todo(id: %s) raise no permission Exception")
        result = todo_service.delete_todo(todo_id)
        return self.render_json(result)

class FinishHandler(APIHandler):
    """完成某个TODO"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/finish msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_service.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to finish todo(id: %s) raise no permission Exception")
        result = todo_service.finish_todo(todo_id)
        return self.render_json(result)

class UnfinishHandler(APIHandler):
    """将某个TODO设置成未完成"""
    @tornado.web.authenticated
    def post(self):
        todo_id = self.get_argument("todo_id", 0)
        if not todo_id:
            raise Exception("todo/unfinish msg: todo_id cant be %s" % todo_id)
        user_id = self.get_current_user()
        if not todo_service.check_owner(user_id, int(todo_id)):
            raise Exception("user_id: %s want to unfinish todo(id: %s) raise no permission Exception")
        result = todo_service.unfinish_todo(todo_id)
        return self.render_json(result)
        
class RecentHandler(APIHandler):
    """获取最近完成的TODO列表"""
    def get(self):
        user_id = self.get_argument("user_id", 0)
        if not user_id:
            raise Exception("todo/recent msg: user_id cant be %s" % user_id)
        last_time = self.get_argument("last_time", "")
        tododata = todo_service.recent_finish_todo(user_id, last_time)
        if not tododata:
            return self.render_json({})
        result = self._sort_by_date(tododata)
        return self.render_json(result)

class PostcardHandler(APIHandler):
    """TODO完成广播"""
    def get(self):
        result = todo_service.postcard()
        return self.render_json(result)
