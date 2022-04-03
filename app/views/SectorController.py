#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :SectorController
# @CreatTime    :2022/3/22 20:01 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import json

from django.http import HttpResponse

from app.service.SectorService import getSectorList,addSectorService,deleteSectorService


def getSector(request):
    if request.method == "GET":
        status, sectorList = getSectorList()
        res = {
            "status":status,
            "data": sectorList
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")

def addSector(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        name = postBody["name"]
        status = addSectorService(name)
        res = {
            "status":status,
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")

def deleteSector(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status = deleteSectorService(id)
        res = {
            "status":status,
        }
        return HttpResponse(json.dumps(res,ensure_ascii="utf-8"), content_type="application/json")