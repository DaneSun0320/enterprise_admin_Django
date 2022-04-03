#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :__init__.py
# @CreatTime    :2022/2/19 16:36 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import logging

from app.models import Attendance,Staff,Goods,Sector,Application,OutsideInfo,GoodApply,RiskRegion
logger = logging.getLogger('log')
try:
    Sector.Sector.objects.create(id = 0,name="待分配")
except Exception as e:
    logger.info("{}=>Sector表已初始化".format(e))