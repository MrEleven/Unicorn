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

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

def get_handlers():
    """获取url映射关系"""
    handlers = []
    api_list = ["marker", "member"]
    for bussiness_name in api_list:
        bussiness_module = import_module("api." + bussiness_name)
        for attr in dir(bussiness_module):
            if attr.endswith("Handler"):
                handler_cls = getattr(bussiness_module, attr)
                if issubclass(handler_cls, tornado.web.RequestHandler):
                    url = "/" + bussiness_name + "/" +  attr.replace("Handler", "").lower()
                    handlers.append((url, handler_cls))
    print handlers
    return handlers


if __name__ == "__main__":
    tornado.options.parse_command_line()
    handlers = get_handlers()
    app = tornado.web.Application(
        handlers=handlers,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
