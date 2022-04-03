#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :OutsideInfo
# @CreatTime    :2022/3/29 19:58 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import logging
import datetime

from django.db import transaction

from app.models.OutsideInfo import  OutsideInfoView
from app.models.RiskRegion import RiskRegion

logger = logging.getLogger('log')

def getOutsideInfo():
    try:
        with transaction.atomic():
            today = datetime.datetime.now()
            goodList = OutsideInfoView.objects.filter(startDate__lte=datetime.date(today.year, today.month, today.day),endDate__gte=datetime.date(today.year, today.month, today.day)).values()
            logger.debug("出差列表")
            return 1,list(goodList)
    except Exception as e:
        logger.exception(e)
        return 0,None

def getOutsideNumber():
    try:
        with transaction.atomic():
            today = datetime.datetime.now()
            outsideList = OutsideInfoView.objects.filter(startDate__lte=datetime.date(today.year, today.month, today.day),endDate__gte=datetime.date(today.year, today.month, today.day),approveStatus=1)
            logger.debug("获取出差人数")
            return 1,len(outsideList)
    except Exception as e:
        logger.exception(e)
        return 0,None
def approve(id,isApprove):
    try:
        with transaction.atomic():
            OutsideInfoView.objects.filter(id=id).update(approveStatus = 1 if isApprove else -1)
            logger.debug("出差审批")
            return 1
    except Exception as e:
        logger.exception(e)
        return 0
# 创建一个方法，用来查询风险地区
def getRiskArea():
    try:
        with transaction.atomic():
            riskAreaList = RiskRegion.objects.all().values()
            logger.debug("风险地区")
            return 1,list(riskAreaList)
    except Exception as e:
        logger.exception(e)
        return 0,None
# creat a function use to add a riskRegion, param is province,city,district,riskLevel
def addRiskArea(province,city,district,riskLevel):
    try:
        with transaction.atomic():
            RiskRegion.objects.create(province=province,city=city,district=district,riskLevel=riskLevel)
            logger.debug("添加风险地区")
            return 1
    except Exception as e:
        logger.exception(e)
        return 0
# creat a function use to delete a riskRegion, param is id
def deleteRiskArea(id):
    try:
        with transaction.atomic():
            RiskRegion.objects.filter(id=id).delete()
            logger.debug("删除风险地区")
            return 1
    except Exception as e:
        logger.exception(e)
        return 0
# creat a function use to update a riskRegion, param is id,riskLevel
def updateRiskArea(id,riskLevel):
    try:
        with transaction.atomic():
            # if the riskLevel is 0, then delete the riskRegion
            if riskLevel == 0:
                RiskRegion.objects.filter(id=id).delete()
            else:
                RiskRegion.objects.filter(id=id).update(riskLevel=riskLevel)
            logger.debug("修改风险地区等级")
            return 1
    except Exception as e:
        logger.exception(e)
        return 0