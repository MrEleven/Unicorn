#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-11
# Author: Master Yumi
# Email : yumi@meishixing.com

from base import BaseHandler

class APIHandler(BaseHandler):
    """api基础类型"""
    @classmethod
    def is_api(self):
        return True
