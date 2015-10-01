#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-01
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import db

def get_marker_list(page=1, page_size=10):
    start = (page-1) * page_size
    sql = "select * from marker order by id desc limit %s, %s;"
    return db.query(sql, start, page_size)

    
