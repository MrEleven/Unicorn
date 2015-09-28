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
import os

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class ListHandler(tornado.web.RequestHandler):
    """签到列表"""
    def get(self):
        self.render("marker_list.html")

class AddHandler(tornado.web.RequestHandler):
    """增加新签到"""
    def post(self):
        print "hello world"



class OrderHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("order_test.html")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/list", ListHandler), (r'/add', AddHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
