#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :StaffService
# @CreatTime    :2022/3/30 18:56 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import transaction

from app.models.Staff import StaffView
import logging

logger = logging.getLogger('log')

def getStaffList():
    try:
        with transaction.atomic():
            staff = StaffView.objects.all().values()
            logger.debug("获取职工列表")
            return 1,list(staff)
    except Exception as e:
        logger.exception(e)
        return 0,None
def writeCardService(id,uid):
    try:
        with transaction.atomic():
            staff = StaffView.objects.filter(id=id).update(uid=uid)
            logger.debug("录入卡数据")
        return 1
    except Exception as e:
        logger.exception(e)
        return 0