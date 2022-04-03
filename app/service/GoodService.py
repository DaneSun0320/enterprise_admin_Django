#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :GoodService
# @CreatTime    :2022/3/20 16:03 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import datetime
import time

from django.db import transaction

from app.models.Application import Application, ApplicationView
from app.models.Goods import Goods
import logging

logger = logging.getLogger('log')

def getGoodsList():
    try:
        with transaction.atomic():
            goodList = Goods.objects.values()
            logger.debug("请求库存列表")
            return 1,list(goodList)
    except Exception as e:
        logger.exception(e)
        return 0,None

def addGood(name,specification,amount,operator):
    try:
        with transaction.atomic():
            Goods.objects.create(name=name,specification=specification,amount=amount,operator=operator)
            logger.debug("添加库存{}".format(name))
            return 1
    except Exception as e:
        logger.exception(e)
        return 0

def deleteGood(id):
    try:
        with transaction.atomic():
            Goods.objects.filter(id=id).delete()
            logger.debug("删除库存，id={}".format(id))
            return 1
    except Exception as e:
        logger.exception(e)
        return 0
def getApplicationList():
    try:
        with transaction.atomic():
            applicationList = ApplicationView.objects.values()
            return 1,list(applicationList)
    except Exception as e:
        logger.exception(e)
        return 0

def applyGood(id,amount,sectorId):
    try:
        with transaction.atomic():
            good = list(Goods.objects.filter(id = id).values())[0]
            # 申请数不大于库存总数的10%
            if good['amount']*0.1 >= amount:
                # 本部门该物资未申请过
                if len(Application.objects.filter(sectorId = sectorId,goodId=id,status=0)) == 0:
                    Application.objects.create(goodId=id,sectorId=sectorId,amount=amount)
                    # 锁定库存
                    good = Goods.objects.filter(id = id).get()
                    good.amount -= amount
                    good.save()
                    return 1
                # 本部门该物资申请过未批复
                else:
                    return 2

            # 申请数大于库存总数的10%
            else:
                return -1
    except Exception as e:
        logger.exception(e)
        return 0

def approveGood(id,isApprove):
    try:
        with transaction.atomic():
            application = Application.objects.filter(goodId = id,status = 0).get()
            # 库存余额充足
            if isApprove:
                application.status = 1
            else:
                application.status = -1
                good = Goods.objects.filter(id=application.goodId).get()
                good.amount += application.amount
                good.save()
            application.approveTime = datetime.datetime.now()
            application.save()
            return 1
    except Exception as e:
        logger.exception(e)
        return 0