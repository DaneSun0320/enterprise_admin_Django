#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :StaffService
# @CreatTime    :2022/3/30 18:56 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from hashlib import md5

from django.db import transaction

from app.models.Staff import StaffView, Staff
import logging
from app.models.User import User

logger = logging.getLogger('log')


def getStaffList():
    try:
        with transaction.atomic():
            staff = StaffView.objects.all().values()
            logger.debug("获取职工列表")
            return 1, list(staff)
    except Exception as e:
        logger.exception(e)
        return 0, None


def writeCardService(id, uid):
    try:
        with transaction.atomic():
            staff = StaffView.objects.filter(id=id).update(uid=uid)
            logger.debug("录入卡数据")
        return 1
    except Exception as e:
        logger.exception(e)
        return 0
def addStaffService(name, sex ,age, phone, email, sector, position):
    try:
        with transaction.atomic():
            Staff.objects.create(name = name,sex = sex, phone = phone, age = age, email = email,sector = sector, position = position,level=0)
            return 1
    except Exception as e:
        logger.exception(e)
        return 0

def deleteStaffService(id):
    try:
        with transaction.atomic():
            Staff.objects.filter(id = id).delete()
            return 1
    except Exception as e:
        return 0
def updateStaffService(id,name,age,sex,phone,email,sector,position):
    try:
        with transaction.atomic():
            logger.debug("更新员工信息")
            Staff.objects.filter(id = id).update(name = name,age = age, sex = sex, phone = phone,email = email, sector = sector, position = position)
            return 1
    except Exception as e:
        logger.exception(e)
        return 0

def updateLevelService(id, admin):
    try:
        with transaction.atomic():
            if admin:
                Staff.objects.filter(id=id).update(level=1)
            else:
                Staff.objects.filter(id=id).update(level=0)
            return 1
    except Exception as e:
        return 0


def loginService(id, password):
    try:
        with transaction.atomic():
            try:
                id = int(id)
            except ValueError as e:
                return -1, None
            logger.debug("登录信息=>id:{},password:{}".format(id, password))
            staff = list(Staff.objects.filter(id=id).values())
            logger.debug("查询职工表=>{}".format(staff))
            if len(staff) > 0 and staff[0]["level"] > 0:
                # 用户存在且具有权限
                staff = staff[0]
                user = list(User.objects.filter(id=id).values())
                logger.debug("查询用户登录表=>{}".format(user))
                if len(user) == 0:
                    # 新登录用户 创建用户
                    origin_password = md5(str(staff["phone"]).encode("utf-8")).hexdigest()
                    User.objects.create(id=id, password=origin_password)
                    if password == origin_password:
                        return 1, staff
                    else:
                        return 0, None
                else:
                    # 已经存在用户
                    right_password = user[0]["password"]
                    if password == right_password:
                        return 1, staff
                    else:
                        return 0, None
            else:
                # 无权限或者不存在
                return -1, None
    except Exception as e:
        logger.exception(e)
        return -2, None

def updatePasswordService(id, oldPassword, newPassword):
    try:
        with transaction.atomic():
            user = User.objects.filter(id=id)
            if len(list(user.values())) == 1:
                origin_password = user.get().password
                if oldPassword == origin_password:
                    user.update(password=newPassword)
                    return 1
                else:
                    # 原密码错误
                    return -1
            else:
                # 用户不存在
                return -2
    except Exception as e:
        logger.exception(e)
        return 0