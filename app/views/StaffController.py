#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :StaffController
# @CreatTime    :2022/3/30 18:56 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import json

from django.http import HttpResponse

from app.service.StaffService import getStaffList, writeCardService
from app.utils.DateEncoder import DateEncoder
from app.utils.readCard import readCard

def getStaff(request):
    if request.method == "GET":
        status, staffList = getStaffList()
        res = {
            "status":status,
            "data": staffList
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")


def writeCard(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status,cardId = readCard()
        if status == 1:
            writeCardService(id,cardId)
        res = {
            "status":status
            }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

