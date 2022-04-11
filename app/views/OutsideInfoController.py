#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :OutsideInfoController
# @CreatTime    :2022/3/29 20:02 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import json

from django.http import HttpResponse

from app.utils.DateEncoder import DateEncoder
from app.service.OutsideInfoService import getOutsideInfo, getOutsideNumber, approve, getRiskArea, \
    updateRiskArea, addRiskArea, updateRiskLevelService, deleteRiskRegionService, getOutsideInfoForApprove, \
    applyOutsideService


def getOutside(request):
    if request.method == "GET":
        status, infoList = getOutsideInfo()
    res = {
        "status":status,
        "data": infoList
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def getOutsideForApprove(request):
    if request.method == "GET":
        status, infoList = getOutsideInfoForApprove()
    res = {
        "status":status,
        "data": infoList
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def applyOutside(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        province = postBody["province"]
        city = postBody["city"]
        district = postBody["district"]
        date = postBody["date"]
        status = applyOutsideService(id,province,city,district,date)
        res = {
            "status":status
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def getNumber(request):
    if request.method == "GET":
        status, number = getOutsideNumber()
    res = {
        "status":status,
        "data": number
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def approveOutside(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        isApprove = postBody["isApprove"]
        status = approve(id,isApprove)
    res = {
        "status":status
    }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

# creat a view to get riskRegion data
def getRiskRegion(request):
    if request.method == "GET":
        status, infoList = getRiskArea()
        res = {
            "status":status,
            "data": infoList
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

# creat a view to delete riskRegion
def deleteRiskRegion(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status = deleteRiskRegionService(id)
        res = {
            "status":status
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

# creat a view to update riskLevel data
def updateRiskLevel(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        riskLevel = postBody["riskLevel"]
        status = updateRiskLevelService(id,riskLevel)
        res = {
            "status":status
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

# creat a view to add riskRegion
def addRiskRegion(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        province = postBody["province"]
        city = postBody["city"]
        district = postBody["district"]
        level = postBody["level"]
        status = addRiskArea(province,city,district,level)
        res = {
            "status":status
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")
