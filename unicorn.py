#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-09-28
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import os, config
from importlib import import_module
from api.apibase import APIHandler
from page.pagebase import PageHandler

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

def get_handlers():
    """获取url映射关系,包括页面和api"""
    from page.marker import ListHandler
    handlers = [("/", ListHandler)]
    # API接口
    api_list = ["marker", "comment", "goal"]
    for bussiness_name in api_list:
        bussiness_module = import_module("api." + bussiness_name)
        for attr in dir(bussiness_module):
            if attr.endswith("Handler"):
                handler_cls = getattr(bussiness_module, attr)
                if issubclass(handler_cls, APIHandler) and (handler_cls != APIHandler):
                    url = "/a/" + bussiness_name + "/" +  attr.replace("Handler", "").lower()
                    handlers.append((url, handler_cls))
    # 网页接口
    page_list = ["marker", "user", "comment", "goal"]
    for bussiness_name in page_list:
        bussiness_module = import_module("page." + bussiness_name)
        for attr in dir(bussiness_module):
            if attr.endswith("Handler"):
                handler_cls = getattr(bussiness_module, attr)
                if issubclass(handler_cls, PageHandler) and (handler_cls != PageHandler):
                    url = "/" + bussiness_name + "/" +  attr.replace("Handler", "").lower()
                    handlers.append((url, handler_cls))
    print handlers
    return handlers

def get_ui_modules():
    """获取UI模块"""
    ui_modules = {}
    ui_list = ["nav", "add_marker", "fullscreen_bg"]
    for ui_module_name in ui_list:
        ui_module = import_module("ui_module." + ui_module_name)
        for attr in dir(ui_module):
            if attr.endswith("UIModule"):
                ui_cls = getattr(ui_module, attr)
                if issubclass(ui_cls, tornado.web.UIModule):
                    ui_modules[ui_module_name] = ui_cls
    return ui_modules


if __name__ == "__main__":
    tornado.options.parse_command_line()
    handlers = get_handlers()
    ui_modules = get_ui_modules()
    app = tornado.web.Application(
        handlers=handlers,
        ui_modules=ui_modules,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        xsrf_cookies=True,
        login_url="/user/login",
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
