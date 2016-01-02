#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-11
# Author: Master Yumi
# Email : yumi@meishixing.com

from base import BaseHandler

class PageHandler(BaseHandler):
    """网页的基类型"""
    def render(self, template_name, result={}):
        if self.is_mobile():
            template_name = "mobile/" + template_name
        super(BaseHandler, self).render(template_name, result=result)
        
