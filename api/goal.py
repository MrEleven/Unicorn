#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-24
# Author: Master Yumi
# Email : yumi@meishixing.com

from api.base import BaseHandler

class GoalUIHandler(BaseHandler):
    """目标"""
    def get(self):
        return self.render("goal_ui.html", result={})
