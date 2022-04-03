#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :AttendanceService
# @CreatTime    :2022/3/20 19:25 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import datetime

from django.db import transaction

from app.models.Attendance import AttendanceView


def getAttendanceList(time):
    try:
        with transaction.atomic():
            if time == "today":
                today = datetime.datetime.now()
                tomorrow = today + datetime.timedelta(days=1)
                attendanceList = AttendanceView.objects.filter(start_time__gt = datetime.date(today.year, today.month, today.day)).filter(start_time__lt=datetime.date(tomorrow.year,tomorrow.month,tomorrow.day)).values()
                return 1,list(attendanceList)
            elif time == "all":
                attendanceList = AttendanceView.objects.all().values()
                return 1,list(attendanceList)
    except Exception as e:
        print(e)
        return 0,None

def getExceptAttendanceList(time):
    try:
        with transaction.atomic():
            if time == "today":
                today = datetime.datetime.now()
                tomorrow = today + datetime.timedelta(days=1)
                attendanceList = AttendanceView.objects.filter(start_time__gt = datetime.date(today.year, today.month, today.day)).filter(start_time__lt=datetime.date(tomorrow.year,tomorrow.month,tomorrow.day))
                attendanceList = attendanceList.filter(tempture__gte = 37).values()
                return 1,list(attendanceList)
            elif time == "all":
                attendanceList = AttendanceView.objects.filter(tempture__gte = 37).values()
                return 1,list(attendanceList)
    except Exception as e:
        print(e)
        return 0,None
# 创建函数addAttendanceInfo，参数为uid，tempture
def addAttendanceInfo(uid,tempture):
    try:
        with transaction.atomic():
            attendance = AttendanceView(uid=uid,tempture=tempture)
            attendance.save()
            return 1,None
    except Exception as e:
        print(e)
        return 0,None