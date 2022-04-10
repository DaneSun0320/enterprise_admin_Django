#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :Attendance
# @CreatTime    :2022/3/20 19:27 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import json

from django.http import HttpResponse

from app.service import AttendanceService
from app.service.AttendanceService import getAttendanceList, getExceptAttendanceList
from app.utils.DateEncoder import DateEncoder


def getTodayAttendance(request):
    if request.method == "GET":
        status, attendanceList = getAttendanceList("today")
    res = {
        "status":status,
        "data": attendanceList
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def getAllAttendance(request):
    if request.method == "GET":
        status, attendanceList = getAttendanceList("all")
    res = {
        "status":status,
        "data": attendanceList
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def getTodayExceptAttendance(request):
    if request.method == "GET":
        status, attendanceList = getExceptAttendanceList("today")
    res = {
        "status":status,
        "data": attendanceList
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def getAllExceptAttendance(request):
    if request.method == "GET":
        status, attendanceList = getExceptAttendanceList("all")
    res = {
        "status":status,
        "data": attendanceList
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def checkTempture(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        tempture = postBody["tempture"]
        operator = postBody["operator"]
        print(id,tempture,operator)
        status = AttendanceService.updateCheckTempture(id, tempture, operator)
        res = {
            "status":status
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")