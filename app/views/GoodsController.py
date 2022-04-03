#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :GoodsController
# @CreatTime    :2022/3/20 16:02 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import json

from django.http import HttpResponse

from app.service.GoodService import getGoodsList, addGood, deleteGood, getApplicationList, applyGood, approveGood
from app.utils.DateEncoder import DateEncoder


def getGoods(request):
    if request.method == "GET":
        status, goodsList = getGoodsList()
        res = {
            "status":status,
            "data": goodsList
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def addGoods(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        name = postBody["name"]
        specification = postBody["specification"]
        amount = postBody["amount"]
        operator = postBody["operator"]
        status = addGood(name,specification,amount,operator)
        res = {
            "status":status
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")

def deleteGoods(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status = deleteGood(id)
        res = {
            "status":status
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")

def getApplication(request):
    if request.method == "GET":
        status, applicationList = getApplicationList()
        res = {
            "status":status,
            "data": applicationList
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8",cls=DateEncoder), content_type="application/json")

def applyGoods(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        amount = postBody["amount"]
        sectorId = postBody["sectorId"]
        status = applyGood(id,amount,sectorId)
        res = {
            "status":status
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")

def approveGoods(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["goodId"]
        isApprove = postBody["isApprove"]
        status = approveGood(id,isApprove)
        res = {
            "status":status
        }
    return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")